#-*-coding:utf-8-*-
__author__ = 'Lenovo'
from PIL import Image
from numpy import *

def pca(X):
    """主成分分析：
       输入：矩阵X，其中该矩阵中存储训练数据，每一行为一条训练数据
       返回：投影矩阵（按照维度的重要性排序）、方差和均值
    """
    num_data,dim = X.shape

    #数据中心化
    mean_X = X.mean(axis = 0)
    X = X -mean_X

    if dim >num_data:
        # PCA使用紧致技巧？
        M = dot(X,X.T) #协方差矩阵
        e,EV = linalg.eigh(M) #特征值和特征向量
        tmp = dot(X.T,EV).T ##紧致技巧？
        V = tmp[::-1] ##需要最后的特征向量，将其逆转
        S = sqrt(e)[::-1] ##由于特征值是按照递增顺序排列的，所以将其逆转

        for i in range(V.shape[1]):
            V[:,i] /= S
            print(i)

    else:
        ##PCA使用SVD方法
        U,S,V = linalg.svd(X)
        V = V[:num_data] ##仅仅返回前num_data个数据

    ##返回投影矩阵，方差和均值
    return  V,S,mean_X