# -*- coding: UTF-8 -*-
#===========================����Ҫ�õ��ĸ���ģ��=========================#
#����������ʽģ�飬Ϊ������ı��е��޹سɷ�
import re

#�����ı�����ģ�飬Ϊ�˷ִ���
import nltk

#����ͣ�ô�ģ�飬Ϊ��ȥͣ�ô���
from nltk.corpus import stopwords

#�����ַ���ģ�飬Ϊ��ʹ���ַ����еķ��ţ�'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
import string
#=============���ݲ�ͬ���Ͻ���Ԥ����=============#
'''     �ɶ���      '''


#def separateWordFromFile(fileName):

####�����ļ�������ϴ####
#���룺�ļ���������·������string��
#�������ϴ��� ��list����ȥ���˸��ַ���
def clearText(fileName):
    cleared_text_list = []
    with open(fileName, 'r') as f:
        for line in f:
            tweet = line.split('	')[2]
            URL_pattern=re.compile(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',re.S)
            try:
                text_without_URL =URL_pattern.sub("",tweet)     #'http://example.com'
            except:
                print tweet
                return -1
            At_mentions_pattern =  re.compile(r'(?:@[\w_]+)',re.S)
            text_without_At_mentions = At_mentions_pattern.sub("",text_without_URL)   #'@marcobonzanini'
            
            hash_tags_pattern = re.compile(r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",re.S)
            text_without_hash_tags = hash_tags_pattern.sub("",text_without_At_mentions)      # '#NLP'
            
            HTML_tags_pattern = re.compile(r'<[^>]+>',re.S)
            text_without_HTML_tags = HTML_tags_pattern.sub("",text_without_hash_tags)       #HTML
            
            emoticons_str_pattern = re.compile(r'(?:[:=;][oO\-]?[D\)\]\(\]/\\OpP])',re.S)
            text_without_emoticons = emoticons_str_pattern.sub("",text_without_HTML_tags)      #�����
            
            RT_str_pattern = re.compile(r'RT :',re.S)   #RT����"RT :"
            text_without_RT = RT_str_pattern.sub("",text_without_emoticons)
            
            emoji_pattern = re.compile(ur"u[\'\"]\\[Uu]([\w\"]{9}|[\w\"]{5})",re.S);#emoji����
            text_without_emoji = emoji_pattern.sub("",text_without_RT)
            
            reminder_text = text_without_emoji
            cleared_text_list.append(reminder_text.strip())
        return cleared_text_list
        
        
####���Ѿ���ϴ�����ı��б���зִ�####
#���룺��ϴ��� ��list��
#������ִʽ���б�ȫתΪСд���ҽ�������ȥ���ˣ�        
def separateWord(clearedTextList):
    regex_str = [
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:\S)' # anything else
    ]
    tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
    tokensList = []
    
    for sentence in clearedTextList:
        tokens = tokens_re.findall(sentence)
        tokens_lower = [token.lower() for token in tokens]
        tokensList.append(tokens_lower)
    return tokensList
 
####���Ѿ���ϴ�ķִ��б����ȥͣ�ô�####
#���룺�ִʽ�� ��list��
#�����ȥͣ�ô�֮��Ľ���б�����Ӣ�ĸ�Ƶ���Լ����÷��ţ�������һ��via��      
def deStopWord(tokensList):
    punctuation = list(string.punctuation)
    stop = stopwords.words('english') + punctuation + ['via']
    deStopList = []
    for sentence in tokensList:
        sentence_deStop = [term for term in sentence if term not in stop]
        deStopList.append(sentence_deStop)
    return deStopList
  
 
####Ԥ��������####
#���룺��ҪԤ������ļ���
#�����������ϴ���ִʣ�ȥͣ�ô�֮��İ����ӷֺõķ����б���άlist�� 
def preprocess(fileName):
    clearedTextList = clearText(fileName)#(r'D:\SCI_aim\experiment\training_set\twitter-2016train-A.txt')    #print clearedTextList[0:50]
    sepWordList = separateWord(clearedTextList)
    deStopList = deStopWord(sepWordList)
    return deStopList
    
#=============���ݲ�ͬ���Ͻ���Ԥ����=============#    
    
    
if __name__ == '__main__':
    #���Դ���
    clearedTextList = clearText(r'twitter-2016train-A.txt')
    #print clearedTextList[0:50]
    sepWordList = separateWord(clearedTextList)
    #print sepWordList[0:50]
    deStopList = deStopWord(sepWordList)
    print deStopList[0:50]
    #pass
    
    
    
    