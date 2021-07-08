from pymongo import MongoClient
import pymongo
import gridfs

class Mongo():
    client = ''
    fileClient = ''

    #Validate, change user data for pc and also twitter for get the "last ones"
    def __init__(self):
        CONNECTION_STRING = "mongodb://localhost:27017/?readPreference=primary"
        self.client = MongoClient(CONNECTION_STRING)

        self.fileClient = gridfs.GridFS(self.client['documents'],collection="documents")
        self.client = self.client['twittermining']

    def insertData(self,collection, item):
        self.client[collection].insert_many([item])

    def findMany(self,collection, query):
        return self.client[collection].find( query )
