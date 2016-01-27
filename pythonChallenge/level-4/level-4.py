import urllib2, re

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/601.4.4 (KHTML, like Gecko) Version/9.0.3 Safari/601.4.4'
headers = { 'User-Agent' : user_agent }
req = urllib2.Request('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345', None, headers)
response = urllib2.urlopen(req)
regex = re.compile("nothing is ([0-9]+)")

n_loop = 0
while response.getcode() == 200 :
	page = response.read()
	if regex.search(page.replace("\n", "")):
		next_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + regex.search(page.replace("\n", "")).group(1)
		n_loop += 1
		print "%3d %s" % (n_loop,next_url)
		req = urllib2.Request(next_url, None, headers)
		response = urllib2.urlopen(req)
	else:
		break
print page

# Yes. Divide by two and keep going.
n_loop += 1
next_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + str(int(re.search(r'[0-9]+', response.geturl()).group(0))//2)
print "%3d %s" % (n_loop,next_url)
req = urllib2.Request(next_url, None, headers)
response = urllib2.urlopen(req)

while response.getcode() == 200 :
	page = response.read()
	if regex.search(page.replace("\n", "")):
		next_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + regex.search(page.replace("\n", "")).group(1)
		n_loop += 1
		print "%3d %s" % (n_loop,next_url)
		req = urllib2.Request(next_url, None, headers)
		response = urllib2.urlopen(req)
	else:
		break
print page
