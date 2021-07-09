from bs4 import BeautifulSoup
import requests

URL = "https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512"

# scrap titles, score and links
response = requests.get(URL)
site_data = response.text

soup = BeautifulSoup(site_data, "html.parser")
film_title = soup.find_all(class_="list-item__title")

all_films = [film.getText() for film in film_title]

# slice operator, [start:stop:step]
# films = all_films[::-1]

with open("movies.txt", mode="w") as file:
    for film in all_films:
        file.write(f"{film}\n")
