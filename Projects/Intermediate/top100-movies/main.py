from bs4 import BeautifulSoup
import requests

resp = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(resp.text, "html.parser")
top_movies = [film.getText() for film in soup.find_all(name="h3", class_="title")]

top_movies.reverse()

with open("Projects/Intermediate/top100-movies/movies.txt", "w", encoding="utf-8") as file:
    for movie in top_movies:
        file.write(f"{movie}\n")