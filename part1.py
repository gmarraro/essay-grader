#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:12:24 2017

@author: gabmarr
"""

from collections import Counter
import codecs
    
def find_ttr():
    i=0
    ttr_mean=0
    with codecs.open('agatha.txt',encoding='utf-8', errors='ignore') as ac:
        tokens = []
        text = ac.read().split()
        #Clean each word in the list: remove punctuation, convert to lower case
        for word in text:
            word = "".join(x for x in word if x.isalnum()).lower()
            tokens.append(word)
        tokens_list=[[] for i in range((len(tokens)//1000)+1)]
        for word in tokens:
            #Create series of 1000-word lists
            if len(tokens_list[i])< 1001:
                tokens_list[i].append(word)
            if len(tokens_list[i]) ==1000:
                i+=1
        for item in tokens_list:
            #Use Counter function to count instances of words in each list
            types = Counter(item)
            #Find ttr 
            ttr = len(types)/len(item)
            #Calculate average over the 75 lists 
            ttr_mean=ttr_mean+ttr
        ttr_mean=ttr_mean/len(tokens_list)
        return ttr_mean

find_ttr()
