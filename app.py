from flask import Flask, request, redirect
import twilio.twiml
import json


#Wiki Imports
from Wiki import Wiki_feature
from Json import Json_Data

#Weather Imports
from forcast import Weather
import forecastio

#Finance Imports
from yahoo_finance import Share
from finance import Finance

#Hacker News Imports
from hackernews import HackerNews
from hacknews import HackNews

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():

    #receving text
    rec_text = request.form['Body']
    resp = twilio.twiml.Response()

    #parsing text
    txt_msg = str(rec_text).split()
    json_type = ""
    json_result = 0
    temp_mem = ""

    if txt_msg[0] == "WIKI-FIND:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)
        #Returns possible results for query
        try:
            search_res = Wiki_feature.search(search_query)
            json_type = "find"
        except:
            resp.message("Error occured please try again.")
        else:
            if(len(search_res) > 0):
                resp.message("Possible Search results for '"+ search_query +"': \n" + ", \n".join(search_res))

    elif txt_msg[0] == "WIKI-FIND:APP:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)
        try:
            search_res = Wiki_feature.search(search_query)
            json_type = "find"
        except:
            resp.message("Error occured please try again.")
        else:
            if(len(search_res) > 0):
                json_result = 2
                resp.message(Json_Data.search_results_json(item=", \n".join(search_res), function=json_type, result=json_result))
            else:
                json_result = 0
                resp.message(Json_Data.search_results_json(item="There is no wiki pages related to your query.", function=json_type, result=json_result))

    elif txt_msg[0] == "WIKI-SEARCH:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)
            #Returns possible results for query
        try:
            summary_res = Wiki_feature.summary(search_query)
            json_type = "search"
        except:
            resp.message("Your query was not an exisiting wiki page, please use 'WIKI-FIND:' to retrieve the correct title and type it EXACTLY AS SHOWN")
        else:
            resp.message(summary_res)

    elif txt_msg[0] == "WIKI-SEARCH:APP:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)
            #Returns possible results for query
        try:
            summary_res = Wiki_feature.summary(search_query)
            json_type = "search"
        except:
            json_result = 0
            resp.message(Json_Data.search_results_json(item="Your query was not an exisiting wiki page, please use 'WIKI-FIND:' to retrieve the correct title and type it EXACTLY AS SHOWN", function=json_type, result=json_result))
        else:
            json_result = 1
            resp.message(Json_Data.search_results_json(item=summary_res, function=json_type, result=json_result))

    elif txt_msg[0] == "WEATHER:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)

        weatherObj = Weather(31.967819, 115.87718)
        resp.message(weatherObj.displayWeather(txt_msg[0])) #timeframe


    elif txt_msg[0] == "WEATHER:APP:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)

        weatherObj = Weather(31.967819, 115.87718)
        weatherObj.displayWeather(txt_msg[0])
        resp.message(str(json.dumps(weatherObj.convertToJson())))

    elif txt_msg[0] == "FINANCE:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)

        try:
            financeObj = Finance(txt_msg[0]) #companyCode
            resp.message(financeObj.displayFinance(txt_msg[1], txt_msg[2])) #yearStart, yearEnd
        except:
            resp.message("The company code you chose doesn't exist, try YHOO, GOOG, AAPL, TWTR, AMZN\nText us: FINANCE: companyCode startYear endYear")

    elif txt_msg[0] == "FINANCE:APP:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)

        try:
            financeObj = Finance(txt_msg[0]) #companyCode
            financeObj.displayFinance(txt_msg[1], txt_msg[2]) #yearStart, yearEnd
            resp.message(str(json.dumps(financeObj.convertToJson())))
        except:
            resp.message("The company code you chose doesn't exist, try YHOO, GOOG, AAPL, TWTR, or AMZN")


    elif txt_msg[0] == "HACKNEWS:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)

        hackNewsObj = HackNews()
        resp.message(str(hackNewsObj.displayHackNews(txt_msg[0])))


    elif txt_msg[0] == "HACKNEWS:APP:":
        del txt_msg[0]
        search_query = " ".join(txt_msg)

        hackNewsObj = HackNews()
        hackNewsObj.displayHackNews(txt_msg[0])
        resp.message(str(json.dumps(hackNewsObj.convertToJson())))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
