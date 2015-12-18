#-*-coding:utf-8-*-
__author__ = 'Lenovo'
from PIL import Image
from numpy import  *
from pylab import *
from imtools import *
import pca
path = 'F:\\python\\SibetProject\\3d'
imlist = get_imlist(path)
im = array(Image.open(imlist[0]))
m,n = im.shape[0:2]
imnbr = len(imlist)

##创建矩阵，保存所有压平后的图像数据
immatrix = array([array(Image.open(im)).flatten() for im in imlist],'f')

V,S,immean = pca.pca(immatrix)

figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))

show()
