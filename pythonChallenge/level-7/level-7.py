# ref: https://teacode.wordpress.com/2013/06/27/level-7-oxygen/

from PIL import Image
import re

img = Image.open('oxygen.png')

#First find the grey area. For grey, r = g = b
y = 0
while True:
    r, g, b, a = img.getpixel((0, y)) #x is 0, where grey is apparent
    if r == g == b:
        break
    y += 1
#Each gray area is 7 pixels wide.
message = ''.join([chr(img.getpixel((x, y))[0]) for x in range(0, img.size[0], 7)])
out = re.findall('\d+', message)
print message
print ''.join(chr(int(i)) for i in out)
