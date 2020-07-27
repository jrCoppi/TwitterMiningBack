import urllib.parse
import urllib.request
import re


url = 'https://twitter.com/search?q=hamilton%20lang%3Aen%20-filter%3Alinks%20-filter%3Areplies&src=typed_query&f=live&vertical=default'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}

req = urllib.request.Request(url, None, headers)
inputLine = urllib.request.urlopen(req).read().decode('utf-8')


inputLine = re.sub("<(.+?)>",'',inputLine)
print(inputLine)