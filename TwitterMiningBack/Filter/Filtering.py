import re

class Filtering():
    htmlPatern = ''
    htmlEntityPatern = ''

    def __init__(self):
        self.htmlPatern = re.compile('<(.+?)>')
        self.htmlEntityPatern = re.compile('&(.+?);')

    def execute(self,newData):
        arrPosts = []
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

            #removes promoted content
            if cleanData.find('Promoted') == -1:
                arrPosts.append(cleanData)

            #Removes the current data from the string
            newData = newData[endPos:len(newData)]

        return arrPosts
    
    def cleanData(self,data):
        #removes html
        cleanData = re.sub(self.htmlPatern, '', data)
        cleanData = re.sub(self.htmlEntityPatern, '', cleanData)
  
        cleanData = re.sub(re.compile(':'), '', cleanData)
        cleanData = re.sub(re.compile(';'), '', cleanData)
        cleanData = re.sub(re.compile('/'), '', cleanData)
        cleanData = re.sub(re.compile('\t'), '', cleanData)
        cleanData = re.sub(re.compile('\n'), '', cleanData)
        cleanData = re.sub(re.compile('\\...'), '', cleanData)
        cleanData = re.sub(re.compile('\\}'), '', cleanData)
        cleanData = re.sub(re.compile('\\{'), '', cleanData)
        cleanData = re.sub(re.compile('\\)'), '', cleanData)
        cleanData = re.sub(re.compile('\\('), '', cleanData)
        cleanData = re.sub(re.compile('\\.'), '', cleanData)
        
        return cleanData.strip()
