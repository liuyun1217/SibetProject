#-*-coding:utf-8-*-
__author__ = 'Lenovo'
from PIL import Image
from numpy import *

def pca(X):
    """���ɷַ�����
       ���룺����X�����иþ����д洢ѵ�����ݣ�ÿһ��Ϊһ��ѵ������
       ���أ�ͶӰ���󣨰���ά�ȵ���Ҫ�����򣩡�����;�ֵ
    """
    num_data,dim = X.shape

    #�������Ļ�
    mean_X = X.mean(axis = 0)
    X = X -mean_X

    if dim >num_data:
        # PCAʹ�ý��¼��ɣ�
        M = dot(X,X.T) #Э�������
        e,EV = linalg.eigh(M) #����ֵ����������
        tmp = dot(X.T,EV).T ##���¼��ɣ�
        V = tmp[::-1] ##��Ҫ��������������������ת
        S = sqrt(e)[::-1] ##��������ֵ�ǰ��յ���˳�����еģ����Խ�����ת

        for i in range(V.shape[1]):
            V[:,i] /= S
            print(i)

    else:
        ##PCAʹ��SVD����
        U,S,V = linalg.svd(X)
        V = V[:num_data] ##��������ǰnum_data������

    ##����ͶӰ���󣬷���;�ֵ
    return  V,S,mean_X