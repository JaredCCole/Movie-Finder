import requests
import pprint
import random
from APIConnector import IMDbConnector



main = IMDbConnector()

mainCount = main.count[7:]#gets the count not including the '&count='

randomNum = random.randrange(int(mainCount))

selected = IMDbConnector.getJSON(main.getURL())["results"][randomNum]


print(f"Title: {selected['title']} {selected['description']} {selected['contentRating']} IMDb Rating: {selected['imDbRating']}\n\n{selected['plot']}\n")

iD = selected["id"]

youTubeTrailer = "https://imdb-api.com/API/YouTubeTrailer/k_2y7947d4/" + iD

print(IMDbConnector.getJSON(youTubeTrailer)["videoUrl"])