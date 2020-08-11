import re

class Filtering():
    htmlPatern = ''

    def __init__(self):
        self.htmlPatern = re.compile('<(.+?)>')

    def execute(self,newData):
        #Loop while there is data
        while True:
            #Finds the first ocourence and replaces the data
            dataPos = newData.find('<tr class="tweet-container">')

            if dataPos == -1:
                break;
            
            #finds the positions
            newData = newData[dataPos:len(newData)] 
            endPos = newData.find('</tr>') + 5

            #Cleans the data
            cleanData = self.cleanData(newData[0:endPos])

            #Removes the current data from the string
            newData = newData[endPos:len(newData)]
    
    def cleanData(self,data):
        #removes html
        cleanData = re.sub(self.htmlPatern, '', data)
        print(cleanData)
        return cleanData
