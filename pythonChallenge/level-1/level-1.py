
s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
decoded = ""
for c in s:
	if c.isalpha():
		decoded = decoded + chr(ord('a') + (ord(c)-ord('a')+2)%(ord('z')-ord('a')+1))
	else:
	    decoded = decoded + c

print decoded

s = "http://www.pythonchallenge.com/pc/def/map.html"
decoded = ""
for c in s:
	if c.isalpha():
		decoded = decoded + chr(ord('a') + (ord(c)-ord('a')+2)%(ord('z')-ord('a')+1))
	else:
	    decoded = decoded + c

print decoded
