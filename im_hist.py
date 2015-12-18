#-*-coding:utf-8-*-
__author__ = 'Lenovo'


from PIL import Image
from pylab import *
from imtools import *

figure()
im = array(Image.open(get_imlist(os.getcwd())[0]).convert('L'))
gray()
contour(im,origin = 'image')
axis('equal')
axis('off')

figure()
hist(im.flatten(),128)
show()

figure()
imshow(im)
print 'Please click 3 points'
x = ginput(3)
print 'you clicked:',x
show()