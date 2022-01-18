import requests
import pprint
import random
from APIConnector import IMDbConnector

main = IMDbConnector()#change this line for different search parameters found in APIConnector.py

mainCount = main.count[7:]#gets the count not including the '&count='

randomNum = random.randrange(int(mainCount))#picks a random index from selected items of a certain count

selected = IMDbConnector.getJSON(main.getURL())["results"][randomNum]#selects the item


print(f"Title: {selected['title']} {selected['description']} {selected['contentRating']} IMDb Rating: {selected['imDbRating']}\n\n{selected['plot']}\n")

iD = selected["id"]

youTubeTrailer = "https://imdb-api.com/API/YouTubeTrailer/" + IMDbConnector.apiKey + "/" + iD

print(IMDbConnector.getJSON(youTubeTrailer)["videoUrl"])
print()