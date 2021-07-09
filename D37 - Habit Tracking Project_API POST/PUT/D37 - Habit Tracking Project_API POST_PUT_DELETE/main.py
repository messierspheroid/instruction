import requests
from datetime import datetime

# need to use strftime to modify the date, https://www.w3schools.com/python/python_datetime.asp
today = datetime.now()
# print(today.strftime("%Y%m%d"))

USERNAME = "meatball"
TOKEN = "&lK6jo9!JOh1tv$!"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# # only needed to create a username
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Time Coding",
    "unit": "min",
    "type": "int",
    "color": "shibafu",
}

# authenticate using a header
headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many minutes did you practice coding today? "),
}

update_pixel_data = {
    "quantity": input("What is the updated amount of minutes you coded today? "),
}stea

# # this is to create the graph, not part of final code
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)
# # preview = https://pixe.la/v1/users/meatball/graphs/graph1.html

# post a new pixel
response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
print(response.text)

# # edit a pixel post
# response = requests.put(url=UPDATE_ENDPOINT, json=update_pixel_data, headers=headers)
# print(response.text)

# # delete a pixel post
# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)
