from hackernews import HackerNews

class HackNews:

	def __init__(self):
		self.hn = HackerNews()
		self.jsonObj = []

	def displayHackNews(self, jobsOrHeadlines):
		if jobsOrHeadlines == "headlines":
			return self.topStories()

		elif jobsOrHeadlines == "jobs":
			return self.jobAds()

		else:
			resp.message("Oops, wrong catagory! Text us: 'HACKNEWS: jobs' or 'HACKNEWS: headlines'")

	def topStories(self):
		uncleanHeadline = ""
		cleanHeadline = ""

		textReturn = ""

		for story_id in self.hn.top_stories(limit=10):
			uncleanHeadline = str(self.hn.get_item(story_id))
			uncleanHeadline = uncleanHeadline.split(' - ', 1 )
			cleanHeadline = uncleanHeadline[1][:-1]

			textReturn += cleanHeadline + '\n\n'

			self.jsonObj.append({ "title" : cleanHeadline })

		if(cleanHeadline and cleanHeadline != ""):
			self.jsonObj.append({ "sucess" : "true" })
		else:
			self.jsonObj.append({ "sucess" : "false" })

		return textReturn

	def jobAds(self):

		textReturn = ""

		numLoops = 0
		maxLoops = 10

		for story_id in self.hn.top_stories():
			numLoops += 1

			story = self.hn.get_item(story_id)

			if numLoops >= 10:
				break

			if story.item_type == 'job':

				uncleanHeadline = str(story)
				uncleanHeadline = uncleanHeadline.split(' - ', 1 )

				cleanHeadline = uncleanHeadline[1][:-1]

				textReturn += cleanHeadline + '\n'

				if cleanHeadline and cleanHeadline != "":
					self.jsonObj.append({ "title" : cleanHeadline })




		if textReturn == "":
			textReturn += "No jobs have been posted in Top Stories, try again tomorrow!"
			self.jsonObj.append({ "sucess" : "false" })
		else:
			self.jsonObj.append({ "sucess" : "true" })

		return textReturn

	def convertToJson(self):

		return self.jsonObj
