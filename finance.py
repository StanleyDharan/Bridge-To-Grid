
from yahoo_finance import Share

class Finance:

	#companyCodeVal must be a string
	def __init__(self, companyCodeVal):
		self.companyCode = companyCodeVal #YHOO
		self.jsonObj = [{}]

	def displayFinance(self, yearStart, yearEnd):
		yahoo = Share(self.companyCode)

		#declare
		textReturn = ""

		textReturn += "Opening price: " + str(yahoo.get_open()) + '\n'

		textReturn += "Current price: " + str(yahoo.get_price()) + '\n'

		textReturn += "Dividend Share: " + str(yahoo.get_dividend_share()) + '\n'
		
		textReturn += "Year High: " + str(yahoo.get_year_high()) + '\n'
		
		textReturn += "Year Low: " + str(yahoo.get_year_low()) + '\n'

		self.jsonObj.append({ "openPrice" : str(yahoo.get_open()) , "currPrice" : str(yahoo.get_price()), "dividendPrice" : str(yahoo.get_dividend_share()), "yearHigh" : str(yahoo.get_year_high()), "yearLow" : str(yahoo.get_year_low()) })


		#historical data returns a jSON object
		jsonHistorical = yahoo.get_historical(str(yearStart) + '-04-25', str(yearEnd) + '-04-29')

		textReturn += "Historical Data: " + '\n'

		#To limit the number of historical datapoints sent
		numHist = 0
		maxHist = 10

		for dict in jsonHistorical:
			numHist += 1

			if numHist < maxHist:
				textReturn += "For year " + dict['Date'] + " High was: " + dict['High'] + " Low was: " + dict['Low'] + '\n'
				#self.jsonObj[0][dict['Date'] + "High"] = dict['High']
				#self.jsonObj[0][dict['Date'] + "Low"] = dict['Low']

				self.jsonObj.append({ "Highd" : dict['Date'] , "Lowd" : dict['Date'], "Highp" : dict['High'], "Lowp" : dict['Low'] })


		if textReturn == "":
			self.jsonObj.append({ "success" : "false" })

		else:
			self.jsonObj.append({ "success" : "true" })

		return textReturn

	def convertToJson(self):

		return self.jsonObj
