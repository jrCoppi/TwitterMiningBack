class Filtering():

    def __init__(self):
        print('aaa')

    def execute(self,data):
        #Get the containers with tweets, TO-DO Foreach than removehtml and simbols
        startPos = data.find('<tr class="tweet-container">')
        endPos = (data[startPos:startPos+10000]).find('</tr>')

        data = data[startPos:startPos+endPos+5]

        print(data)
        print(startPos)
        print(endPos)
