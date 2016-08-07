from couchbase.bucket import Bucket

cb = Bucket('couchbase://localhost/default')
documentKey = "trn:pulse:company:id:"

def addAPIResponseToDatabase(data):

    for index in data['response']['employers']:
        #print(str(index['id']) + " - " + str(index['name']))
        cb.upsert(documentKey + str(index['id']), index)
    return
