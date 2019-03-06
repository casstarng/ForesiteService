import pymongo
#
# client = MongoClient('ec2-3-95-155-210.compute-1.amazonaws.com', 27017,
#              ssl=True, ssl_keyfile='C:\\Users\Cassidy Tarng\mongodb.pem')
#
# db = client.foresite
#
# collection = db.user.find()
#
# print(collection)
# for document in collection:
#     print(document)

client = pymongo.MongoClient("mongodb://admin:admin@3.95.155.210/foresite") # defaults to port 27017

db = client.foresite

cursor = db.user.find()

for doc in cursor:
    print(doc)

#3.95.155.210