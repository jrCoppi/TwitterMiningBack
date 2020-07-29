import urllib.parse
import urllib.request
import re

class Reader():
    userAgent = ''
    url = ''
    subject = ''
    
    #Validate, change user data for pc and also twitter for get the "last ones"
    def __init__(self):
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        self.url = 'https://twitter.com/search?q=replace%20lang%3Aen%20-filter%3Alinks%20-filter%3Areplies&src=typed_query&f=live&vertical=default'

    # Reads the data from the target site and return it's information
    def read(self,subject):
        self.subject = subject
        inputData = self.getSiteInput()
        return self.getInputData(inputData)
        
        
    # Get the data
    def getSiteInput(self):
        headers = {'User-Agent': self.userAgent}
        url = re.sub('replace',self.subject, self.url)

        req = urllib.request.Request(url, None, headers)
        inputLine = urllib.request.urlopen(req).read().decode('utf-8')
        return inputLine
    
    # Clean the data
    def getInputData(self, inputData):

        startPos = inputData.find('<body')
        endPos = inputData.find('body>')

        inputData = inputData[startPos:endPos-5]

        return inputData