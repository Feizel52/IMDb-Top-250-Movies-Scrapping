from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.imdb.com/chart/top/"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
movies = soup.find("tbody", class_="lister-list").find_all("tr")

with open("Top 250 Movies IMDb.csv", "w", encoding="utf8", newline="") as file:
  thewriter = writer(file)
  heading = ["Rank", "Name", "Year", "Rating"]
  thewriter.writerow(heading)

  for movie in movies:
    name = movie.find("td", class_="titleColumn").a.text
    rank = movie.find("td", class_="titleColumn").get_text(strip=True).split(".")[0]
    year = movie.find("td", class_="titleColumn").span.text.strip("()")
    rating = movie.find("td", class_="ratingColumn imdbRating").strong.text
    info = [rank, name, year, rating]
  
    thewriter.writerow(info)

  



