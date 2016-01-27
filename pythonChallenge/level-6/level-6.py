import re, zipfile

inFile  = zipfile.ZipFile('channel.zip')
index   = '90052'
surfix  = '.txt'
message = ''
while True:
    text = inFile.read(index + surfix)
    message += inFile.getinfo(index + surfix).comment
    print text
    index    = re.search('nothing is ([0-9]+)', text)
    if index:
    	index = index.group(1)
    else:
    	break

print message
