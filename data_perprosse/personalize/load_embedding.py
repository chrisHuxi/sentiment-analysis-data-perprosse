# -*- coding: utf-8 -*-
#===========================����Ҫ�õ��ĸ���ģ��=========================#
#����numpy��Ϊ��ʹ��np.array�ͼ���ŷʽ����
import numpy as np

#=============���ز�ͬ������=============#
'''     �ɶ���      '''
####����word embedding����####
#���룺��
#��������غõĴ������ֵ䣬��ͨ��model['s']�����ʴ�������ÿһ��������Ϊ50ά��ndarray
def loadEmbedding():
    model = dict()
    #function: ���ж�ȡ���ļ�
    try:
        file = open(r'glove.twitter.27B.50d.txt', 'r')
        for line in file:
            vec = line.strip().split(' ')
            try:
                model[vec[0]] = np.array(map(float,vec[1:]))
            except UnicodeError:
                continue
    except IOError as err:
        print('File error: ' + str(err))
    finally:
        if 'file' in locals():
            file.close()
    return model
    
####����vec��Ŀ��vec��ŷʽ���룬������####
#���룺aim_vec:Ŀ��������vec:���Ƚϵ�����
#���������������ŷʽ����
def calcuEuclidDist(aim_vec,vec):
    return np.linalg.norm(aim_vec - vec)
    
    
if __name__ == '__main__':
    #���Դ��룺����ͨ��
    model = loadEmbedding()
    '''
    print model['create']
    print model['sound']
    print model['/']
    print model['dear']
    print model['great']
    '''
    #��ӡ����bad�������50���ʣ���Զ����һ��better...˵������������������õ�...
    aim_vec = model['bad']
    sortedResult = sorted(model.items(),key = lambda item : cauEDist(aim_vec,item[1]))[0:51]
    for _tuple in sortedResult:
        print _tuple[0]
    
    