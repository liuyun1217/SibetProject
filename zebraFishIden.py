#-*-coding:utf-8-*-
__author__ = 'LiuYun'
import numpy as np
from PIL import Image

im = Image.open('zebrafishImage.jpeg')
imGrey = im.convert('L')
mtr = np.array(imGrey)

lx,ly = mtr.shape
print(ly)

fx = sum(mtr)
fnx = fx*range(ly)

CM = sum(fnx)/sum(fx)

print(CM)