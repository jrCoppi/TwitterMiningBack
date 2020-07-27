import urllib.parse
import urllib.request
import re

class Reader():
    userAgent = ''
    url = ''
    
    def __init__(self):
        self.userAgent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        self.url = 'https://twitter.com/search?q=replace%20lang%3Aen%20-filter%3Alinks%20-filter%3Areplies&src=typed_query&f=live&vertical=default'

    def read(self,subject):
        headers = {'User-Agent': self.userAgent}

        req = urllib.request.Request(self.url, None, headers)
        inputLine = urllib.request.urlopen(req).read().decode('utf-8')


        inputLine = re.sub("<(.+?)>",'',inputLine)
        print(inputLine)
