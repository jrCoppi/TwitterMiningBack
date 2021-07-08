#Import reading module
#From Folder.File import Class
from Reader.Read import Read
from Filter.Filtering import Filtering
from Data.Operation import Operation

#Runner Class
class Runner():
    def __init__(self):
        #Initialize all the class
        self.operation = Operation()
        self.read = Read()
        self.filtering = Filtering()

    def search(self,term):
        #Executes the reading
        inputData = self.read.execute(term)

        #Logs
        self.operation.logSearch(term,inputData)
        
        inputData = self.filtering.execute(inputData)

        #Saves the result
        searchId = self.operation.saveSearch(inputData,term)

        # Data to serve with our API
        listSearch = {
            "searchId": searchId
        }
        
        return listSearch

    def getResults(self,searchId):
        results = self.operation.getResults(searchId)

        # Data to serve with our API
        listSearch = {
            "postList": results
        }
        
        return listSearch

    def getMostSearched(self):
        results = self.operation.getMostSearched()

        # Data to serve with our API
        listSearch = {
            "termList": results
        }
        
        return listSearch

    def getLatestSearchs(self):
        results = self.operation.getLatestSearchs()

        # Data to serve with our API
        listSearch = {
            "termList": results
        }
        
        return listSearch

    def getLog(self,term):
        baseLogs = self.operation.getLog(term)

        listSearch = {}

        for baseLog in baseLogs:
            listSearch.update(baseLog.get('log'))

        return listSearch

    def saveFile(self,file):
        fileClient = self.operation.getFile()
        fileID = fileClient.put( open( file, 'rb')  )
        out = fileClient.get(fileID)

        print(fileID)

        return fileID
    
    def restoreFile(self,file):
        fileClient = self.operation.getFile()
        cursor = fileClient.find().sort("uploadDate", -1).limit(2)

        i=0 
        while(i < cursor.count()):
            fi=cursor.next()
            with open("D:\\Dev\\Python\\TwitterMiningBack\\documents.rar","wb") as f:
                f.write(fi.read())
                f.closed
                i=i+1