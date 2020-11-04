#Import reading module
#From Folder.File import Class
from Reader.Read import Read
from Filter.Filtering import Filtering
from Data.Operation import Operation

#Initialize all the class
operation = Operation()
read = Read()
filtering = Filtering()

def search(term):

    #Executes the reading
    inputData = read.execute(term)
    inputData = filtering.execute(inputData)

    #Saves the result
    searchId = operation.saveSearch(inputData,term)

    # Data to serve with our API
    listSearch = {
        "searchId": searchId
    }
    
    return listSearch

def getResults(searchId):
    results = operation.getResults(searchId)

     # Data to serve with our API
    listSearch = {
        "postList": results
    }
    
    return listSearch

def getMostSearched():
    results = operation.getMostSearched()

     # Data to serve with our API
    listSearch = {
        "termList": results
    }
    
    return listSearch

def getLatestSearchs():
    results = operation.getLatestSearchs()

     # Data to serve with our API
    listSearch = {
        "termList": results
    }
    
    return listSearch
