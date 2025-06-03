import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response=requests.get(URL)
movie_link = response.text

movie_list  =[]
soup = BeautifulSoup(movie_link, 'html.parser')
names = soup.find_all("h3",class_="title")
for name in names:
    movie_list.append(name.text)
movie_list.reverse()

with open("movies.txt","a", encoding="utf-8") as file:
    for i in movie_list:
        file.write(i + "\n")



