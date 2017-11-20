from __future__ import division
from nltk.tokenize import RegexpTokenizer
from cursesmenu import *
from cursesmenu.items import *
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
import math
import csv
import re
from nltk.util import ngrams

d = cmudict.dict()

def countSyllables(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]


def SmogIndex(text):
    words =  nltk.wordpunct_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    
    sentence_count = len(sentences)
    polysyllable_count = 0

    for w in words :
        try :
            if max(countSyllables(w)) >= 3:
                polysyllable_count += 1               
        except :
            pass     
    
    index = math.sqrt( polysyllable_count * (30/sentence_count)) + 3.1291
    
    return index


if __name__ == "__main__":

    name_lst = [" "]
    index_lst = [" "]
    sentence_lst = [" "]

    for i in range(13):
        d_feature = open("dsm5_chapt17diagnosis"+str(i+1)+".txt","r",encoding="utf-8")
        d_feature = d_feature.read()
        d_feature = re.sub('[^A-Za-z0-9.]+', ' ', d_feature)
        sentences = nltk.sent_tokenize(d_feature)

        for s in sentences:
            index_lst.append(SmogIndex(s))
            sentence_lst.append(s)
            name_lst.append(str(i+1))

        
    with open('smog_index_chapt17_new_by_sentence.csv', 'w', encoding="utf-8", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(zip(name_lst,sentence_lst,index_lst))
