#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:47:01 2017

@author: gabmarr
"""

import codecs
from nltk.tokenize import sent_tokenize
import spacy
import weak_words as ww
from collections import Counter

def format_text(filename):
    nlp = spacy.load('en')
    tokens=[]
    #Read and clean file
    text = codecs.open(filename, encoding='utf-8', errors='ignore').read()
    text=text.split()
    for word in text:
        word = "".join(x for x in word if x.isalnum()).lower()
        tokens.append(word) 
    tokens = ' '.join(tokens)
    #Convert tokens to readable spaCy type spacy.tokens.doc.Doc
    doc=nlp(tokens)
    return doc

def quotes(filename):
    score_list=[]
    essay = codecs.open(filename, encoding='utf-8', errors='ignore').read()
    essay=essay.split('\n')
    for paragraph in essay:
        score=1
        count=0
        paragraph=paragraph.split()
        for word in paragraph:
            if "(" in word:
                count+=1
        #Decrease score by 0.3 if paragraph has less than 3 quotes
        if count< 3:
            score-=0.3
            score_list.append(score)
        else:
            score=1
            score_list.append(score)
    #Only consider scores other than the intro and conclusion paragraphs
    score_list=score_list[1:-1]
    #Find average score, which counts for 30% of grade
    score=0.3*(sum(i for i in score_list)/len(score_list))
    return score

def ttr(filename):
    i=0
    ttr_mean=0
    ttr_score=0
    with codecs.open(filename,encoding='utf-8', errors='ignore') as ac:
        tokens = []
        text = ac.read().split()
        for word in text:
            word = "".join(x for x in word if x.isalnum()).lower()
            tokens.append(word)
        #Create 500-word lists
        tokens_list=[[] for i in range((len(tokens)//500)+1)]
        for word in tokens:
            if len(tokens_list[i])< 501:
                tokens_list[i].append(word)
            if len(tokens_list[i]) ==500:
                i+=1
        #Count the word types and ratio for each list
        for item in tokens_list:
            score=0
            types = Counter(item)
            ttr = len(types)/len(item)
            #Give score based on TTR 
            if ttr >0.5:
                score =1
            elif 0.4<=ttr<=0.5:
                score=0.8
            else:
                score=0.6
            ttr_mean=ttr_mean+score
        #Find the average TTR over all the 500-word lists  
        ttr_mean=ttr_mean/len(tokens_list)
        #TTR score counts for 25% of grade
        ttr_score=0.25*ttr_mean
        return ttr_score
    
def weak_words(filename):
    ww_final=0
    essay = codecs.open(filename, encoding='utf-8', errors='ignore').read()
    essay=essay.split('\n')
    for paragraph in essay:
        score=0
        count=0
        paragraph=sent_tokenize(paragraph)
        for sentence in paragraph:
            sentence=sentence.split()
            for word in sentence:
                #If a word is listed in the weak_words module, increase count
                word = "".join(x for x in word if x.isalnum()).lower()
                if str(word) in ww.weak_adjs or str(word) in ww.weak_nouns or str(word) in ww.weak_verbs:
                    count+=1
        #Give each paragraph a score based on the number of words in paragraph
        score=1-(count/len(str(paragraph).split()))
        ww_final+=score
    #Find average score, counts for 15% of grade
    ww_final=0.15*(ww_final/len(essay))
    return ww_final

def paragraph_length(filename):
    score_avg=0
    essay = codecs.open(filename, encoding='utf-8', errors='ignore').read()
    essay=essay.split('\n')
    for paragraph in essay:
        score=0
        paragraph=sent_tokenize(paragraph)
        #Calculate deviation from ideal length based on deviation under 5
        if len(paragraph)<5:
            deviation=abs(len(paragraph)-5)
            score=1-(deviation/len(paragraph))
        #Calculate deviation from ideal length based on deviation over 10 
        elif len(paragraph)>10:
            deviation=abs(len(paragraph)-10)
            score=1-(deviation/len(paragraph))
        #If paragraph has 5-10 sentences, give full credit
        else:
            score=1
        score_avg=score_avg+score
    #Find average score, counts for 15% of grade
    score_avg=0.15*(score_avg/len(essay))
    return score_avg


def passive_voice(filename):
    count=0
    score=0
    doc=format_text(filename)
    #Use spaCy's .dep_ to find words in passive voice
    for token in doc:
        if token.dep_=="nsubjpass":
            count+=1
    #Find ratio of passive voice to number of words
    score=.15*(1-(count/len(doc)))
    return score


def grade_paper(*filename):
    outfile = open('grades.txt', 'w')
    for paper in filename:
        ww=weak_words(paper)
        type_token=ttr(paper)
        pv=passive_voice(paper)
        quote=quotes(paper)
        para=paragraph_length(paper)
        #Calculate total score and convert to grade out of 100 points
        total_score=(ww+type_token+pv+quote+para)*100
        #Write the file and grade to grades.txt
        outfile.write(paper + "  " + "{:.2f}".format(total_score)+ '\n')
    outfile.close()
