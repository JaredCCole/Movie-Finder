import requests
import pprint

class IMDbConnector:

	def __init__(self, titleType = "feature", releaseMinMax = None, userRatingMinMax = "7.5,10", numOfVotesMinMax = "1000,", genre = None, count = "250"):
		#add parameters into advanced search url if parameter is not None

		self.titleType = "title_type=" + titleType
		self.releaseMinMax = "&release_date=" + releaseMinMax if releaseMinMax is not None else ""
		self.userRatingMinMax = "&user_rating=" + userRatingMinMax if userRatingMinMax is not None else ""
		self.numOfVotesMinMax = "&num_votes=" + numOfVotesMinMax if numOfVotesMinMax is not None else ""
		self.genre = "&genres=" + genre if genre is not None else ""
		self.count = "&count=" + count if count is not None else ""

	def getURL(self):
		#concatenate the url together
		return "https://imdb-api.com/API/AdvancedSearch/k_2y7947d4?" + self.titleType + self.releaseMinMax + self.userRatingMinMax + self.numOfVotesMinMax + self.genre + self.count


	def getJSON(url):
		#returns the json of the page searched
		r = requests.get(url)
		return r.json()

