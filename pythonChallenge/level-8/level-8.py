import bz2

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

username = 'username: ' + bz2.decompress(un)
password = 'password: ' + bz2.decompress(pw)
print username
print password


# Another solution
username = 'username: ' + un.decode('bz2')
password = 'password: ' + pw.decode('bz2')
print username
print password

print 'Use username and password at "http://www.pythonchallenge.com/pc/def/integrity.html"'
