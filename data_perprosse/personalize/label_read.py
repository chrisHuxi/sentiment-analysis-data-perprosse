# -*- coding: UTF-8 -*-
#===========================����Ҫ�õ��ĸ���ģ��=========================#
import sys
sys.path.append("..")


#=============���ݲ�ͬlabel��ǩ����Ԥ����=============#
'''     �ɶ���      '''

####���ļ��ж���01label####
#���룺�ļ���
#�����labelList
def readLabel(fileName):
    #return Textrw.readFormFile1DList(fileName)
    cleared_label_list = []
    with open(fileName, 'r') as f:
        for line in f:
            label = line.split('	')[1]
            if label == 'negative':
                cleared_label_list.append(-1)
            elif label == 'neutral':
                cleared_label_list.append(0)
            elif label == 'positive':
                cleared_label_list.append(1)
            else:
                print "there are unexcepted label:" + label
                return -1
        return cleared_label_list
#=============���ݲ�ͬlabel��ǩ����Ԥ����=============#
        
        
        
if __name__ == '__main__':
    #���Դ���
    labelList = readLabel(r'twitter-2016train-A.txt')
    print labelList.count(-1)
    print labelList.count(0)
    print labelList.count(1)
    print labelList
    #����ͨ��
    #pass