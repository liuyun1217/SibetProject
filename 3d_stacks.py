#-*-coding:utf-8-*-
__author__ = 'LiuYun'
import numpy as np
from PIL import Image

im = Image.open('151.tif')
imGrey = im.convert('L')
mtr = np.array(imGrey)

print(mtr)
im.histogram()
