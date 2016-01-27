import urllib2
import re

user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request('http://www.pythonchallenge.com/pc/def/equality.html', None, headers)
response = urllib2.urlopen(req)
page = response.read()

match_list = "".join(re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', page))
print match_list
