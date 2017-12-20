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


def SmogIndex(text, words):
    words = words
    polysyllable_count = 0
    #print(words)

    for w in words :
        try :
            if max(countSyllables(w)) >= 3:
                #print(w)
                polysyllable_count += 1               
        except :
            pass     

    index = polysyllable_count / len(words)
    return index


if __name__ == "__main__":

    name_lst = [" "]
    index_lst = [" "]
    sentence_lst = [" "]

    for i in range(12):
        d_feature = open("dsm5_chapt18diagnosis"+str(i+1)+".txt","r",encoding="utf-8")
        d_feature = d_feature.read()
        sentences = nltk.sent_tokenize(d_feature)
        
        for s in sentences:
            s = s.replace("e.g.","eg")
            s = re.sub('[^A-Za-z0-9]+', ' ', s)
            words = nltk.word_tokenize(s)
            lenth = len(words)
            index_lst.append(SmogIndex(s, words))
            sentence_lst.append(s)
            name_lst.append(str(i+1))

        
    with open('smog_index_chapt18_latest_by_sentence.csv', 'w', encoding="utf-8", newline='') as myfile:
        wr = csv.writer(myfile)
        wr.writerows(zip(name_lst,sentence_lst,index_lst))
