#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 21:12:24 2017

@author: gabmarr
"""

from collections import Counter
import codecs
    
def find_ttr():
    #Initialize i to loop through list of 1000-word lists
    i=0
    #Initialize number to find average ttr 
    ttr_mean=0
    with codecs.open('agatha.txt',encoding='utf-8', errors='ignore') as ac:
        tokens = []
        #Read the text file and split by spaces into words
        text = ac.read().split()
        #Clean each word in the list: remove punctuation, convert to lower case
        for word in text:
            word = "".join(x for x in word if x.isalnum()).lower()
            #Append each formatted word to a list of tokens
            tokens.append(word)
        #Create a list of lists based on length of book divided by 1000
        tokens_list=[[] for i in range((len(tokens)//1000)+1)]
        #Beginning with the first list in tokens_list
        for word in tokens:
            #Append word to sub-list until it contains 1000 words
            if len(tokens_list[i])< 1001:
                tokens_list[i].append(word)
            #When list has 1000 items, increase i to fill next sub-list
            if len(tokens_list[i]) ==1000:
                i+=1
        #For each 1000-word chunk
        for item in tokens_list:
            #Use Counter function to count instances of words in each list
            types = Counter(item)
            #Find ttr 
            ttr = len(types)/len(item)
            #Add ttr to mean to use to calculate average over the 75 lists 
            ttr_mean=ttr_mean+ttr
        #Calculate average mean over the 75 lists
        ttr_mean=ttr_mean/len(tokens_list)
        return ttr_mean

find_ttr()
#TTR = 0.4389