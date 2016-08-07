import requests
import json
from collections import OrderedDict
#from couchbase.bucket import Bucket
from couchbaseCRUD import addAPIResponseToDatabase

#cb = Bucket('couchbase://localhost/default')
#documentKey = "trn:pulse:company:id:"

# authentication information & other request parameters
params_gd = OrderedDict({
    "v": "1",
    "format": "json",
    "t.p": "79119", #Please change this
    "t.k": "hXV3myqMKQM", #Please change this
    "action": "employers",
#    "q": "retail",
    "l": "india",
    "pn": "1",
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
data = response_gd.json()
# check the response code (should be 200)  & the content
print("Total Number of Pages is " + str(data['response']['totalNumberOfPages']))
# print(response_gd.status_code)
# print(response_gd.content)


for pageNumber in range(3544, data['response']['totalNumberOfPages']+1):
    params_gd["pn"] = str(pageNumber)
    response_gd = requests.get(basepath_gd, params=params_gd, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"})
    print("Current Page Number is " + str(response_gd.json()['response']['currentPageNumber']))
    addAPIResponseToDatabase(response_gd.json())
#    for index in response_gd.json()['response']['employers']:
#        #print(str(index['id']) + " - " + str(index['name']))
#        cb.upsert(documentKey + str(index['id']), index)

