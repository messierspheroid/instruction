import os
import requests
import base64
import datetime
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import json
import lxml

client_id = "cb49c27cc3484970bf86469706dc8ff2"
client_secret = "075c8e86c50840d2ad575dff1aee742d"
spotify_user_id = "cebjorn?si=zjLOhFPrShifCgIs1OQnkw"


class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = True
    client_id = None
    client_secret = None
    spotify_user_id = spotify_user_id
    token_url = "https://accounts.spotify.com/api/token"

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_client_credentials(self):
        """
        returns a base64 encoded string
        """
        client_id = self.client_id
        client_secret = self.client_secret
        if client_secret is None or client_id is None:
            raise Exception("You must set client_id and client_secret")
        client_creds = f"{client_id}:{client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())
        return client_creds_b64.decode()

    def get_token_headers(self):
        client_creds_b64 = self.get_client_credentials()
        return {
            "Authorization": f"Basic {client_creds_b64}"
        }

    def get_token_data(self):
        return {
            "grant_type": "client_credentials"
        }

    def perform_auth(self):
        token_url = self.token_url
        token_data = self.get_token_data()
        token_headers = self.get_token_headers()
        r = requests.post(token_url, data=token_data, headers=token_headers)

        if r.status_code not in range(200, 299):
            raise Exception("Could not authenticate client")
            # return False

        data = r.json()
        now = datetime.datetime.now()
        access_token = data["access_token"]
        expires_in = data["expires_in"]
        expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token = access_token
        self.access_token_expires = expires
        self.access_token_did_expire = expires < now
        return True

    def get_access_token(self):
        token = self.access_token
        expires = self.access_token_expires
        now = datetime.datetime.now()
        if expires < now:
            self.perform_auth()
            return self.get_access_token()
        elif token is None:
            self.perform_auth()
            return self.get_access_token()
        return token

    def get_resource_header(self):
        access_token = self.get_access_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {access_token}"
        }
        return headers

    def get_resource(self, lookup_id, resource_type="albums", version="v1"):
        endpoint = f"https://api.spotify.com/{version}/{resource_type}/{lookup_id}"
        headers = self.get_resource_header()
        r = requests.get(endpoint, headers=headers)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def get_album(self, _id):
        return self.get_resource(_id, resource_type="albums")

    def get_artists(self, _id):
        return self.get_resource(_id, resource_type="artists")

    def base_search(self, query_params):
        headers = self.get_resource_header()
        endpoint = "https://api.spotify.com/v1/search"
        lookup_url = f"{endpoint}?{query_params}"
        # print(lookup_url)
        r = requests.get(lookup_url, headers=headers)
        print(r.json())
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def search(self, query=None, operator=None, operator_query=None, search_type="track"):
        if query == None:
            raise Exception("A query is required")
        if isinstance(query, dict):
            # turn a dict into a list, %20 = space
            query = " ".join([f"{k}:{v}" for k, v in query.items()])
        if operator is not None and operator_query is not None:
            if operator.lower() == "or" or operator.lower() == "not":
                operator = operator.upper()
                if isinstance(operator_query, str):
                    query = f"{query} {operator} {operator_query}"
        # urlencode will convert dict from json to url pathtype
        query_params = urlencode({"q": query, "type": search_type.lower()})
        print(query_params)
        return self.base_search(query_params)

    def get_bs4_list_gen(self):
        user_date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

        requested_date_URL = f"https://www.billboard.com/charts/hot-100/{user_date_input}"
        response = requests.get(requested_date_URL)
        full_site_HTML = response.text

        soup = BeautifulSoup(full_site_HTML, "lxml")
        song_title = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")
        song_title_l = [title.getText() for title in song_title]
        pass

    def create_playlist(self):
        self.get_bs4_list_gen()

        request_body = json.dumps({
            "name": "playlist",
            "description": "List generated playlist from BeautifulSoup API",
            "public": True,
        })
        headers = self.get_resource_header()
        query = "https://api.spotify.com/v1/users/{}/playlists".format(
            spotify_user_id
        )
        response = requests.post(query, data=request_body, headers=headers)
        print(response.json())
        if response.status_code not in range(200, 299):
            return {}
        return response.json()

    def get_spotify_uri(self, song_name, artist):
        headers = self.get_resource_header()
        query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
            song_name,
            artist,
        )
        response = requests.get(
            query,
            headers=headers,
        )
        response_json = response.json()
        songs = response_json["tracks"]["items"]

        # only use the first song
        uri = songs[0]["uri"]
        return uri


# TODO bs4 info
# TODO grab bs4 info
# TODO create a new playlist in spotify
# TODO search for the song in spotify
# TODO add song(s) into the new spotify playlist

spotify = SpotifyAPI(client_id, client_secret)
spotify.search(query=song_title_l, search_type="track")
