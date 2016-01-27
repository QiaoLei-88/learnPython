import urllib2
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request('http://www.pythonchallenge.com/pc/def/ocr.html', None, headers)
response = urllib2.urlopen(req)
page = response.read()

# Filter out characters.
filtered = ""
for c in page:
	if c.isalpha():
		filtered += c

# cut off leading statements and output.
statement = "find rare characters in the mess below"
statement = statement.replace(" ", "")
print filtered[filtered.find(statement)+len(statement):]
