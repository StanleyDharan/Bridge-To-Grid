import requests

parameters = {'key': '94e4f86021169ee84b3fac03a466638f', 'q': 'shredded%20chicken'}

response = requests.get{'http://food2fork.com/api/search', params=parameters)

# this is gonna show the json response, its hella long lol
print(response.content)
