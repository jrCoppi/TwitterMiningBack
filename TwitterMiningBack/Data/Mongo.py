from pymongo import MongoClient
import pymongo

class Mongo():
    client = ''

    #Validate, change user data for pc and also twitter for get the "last ones"
    def __init__(self):
        CONNECTION_STRING = "mongodb://localhost:27017/?readPreference=primary"
        self.client = MongoClient(CONNECTION_STRING)
        #collection
        self.client = self.client['minning']
        #database
        self.client = self.client['twittermining']