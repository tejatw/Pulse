import urllib.request as request
import requests
import json
from collections import OrderedDict

# authentication information & other request parameters
params_gd = OrderedDict({
    "v": "1",
    "format": "json",
    "t.p": "76180", #Please change this
    "t.k": "h6KBkeNW8xG", #Please change this
    "action": "employers",
    "employerID": "11111",
	"userip": "192.168.0.104", #Please change this

    "useragent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"
})

# construct the URL from parameters
basepath_gd = 'http://api.glassdoor.com/api/api.htm'

# request the API
response_gd = requests.get(basepath_gd,
                           params=params_gd,
                           headers={
                               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"
                           })
# check the response code (should be 200)  & the content
response_gd
response_gd.content
data = response_gd.json()
print (type(data))
# print(data['totalNumberOfPages'])
print(data)
# print(response_gd.status_code)
# print(response_gd.content)
