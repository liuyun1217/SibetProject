#-*-coding:utf-8-*-
__author__ = 'Lenovo'
from PIL import Image
from pylab import *
from imtools import *
figure()
im = array(Image.open(get_imlist(os.getcwd())[0]).convert('L'))
imshow(im)

x = [100,100,400,400]
y = [200,500,200,500]

plot(x,y,'r*')

plot(x[:2],y[:2])


title('zebrafish plotting')

show()
