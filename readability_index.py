from __future__ import division
from nltk.tokenize import RegexpTokenizer
from cursesmenu import *
from cursesmenu.items import *
from curses.ascii import isdigit
import nltk
from nltk.corpus import cmudict
import math

d = cmudict.dict()

def countSyllables(word):
    return [len(list(y for y in x if isdigit(y[-1]))) for x in d[word.lower()]]

def FleschReadingEaseIndex(text):
    words =  nltk.wordpunct_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    
    sentence_count = len(sentences)
    word_count = 0
    syllable_count = 0
    
    for w in words :
        try :
            syllable_count = syllable_count + max(countSyllables(w))
            word_count += 1            
        except :
            pass

    index =  206.835 - 1.015 * (word_count/sentence_count) - 84.6 * (syllable_count/word_count)

    status = ""
    if index >= 90 :
        status = "very easy"
    elif index >= 80 :
        status = "easy"
    elif index >= 70 :
        status = "fairly easy"
    elif index >= 60 :
        status = "standard"
    elif index >= 50 :
        status = "fairly difficult"
    elif index >= 30 :
        status = "difficult"
    else :
        status = "very confusing"
    
    print("Flesch Reading Ease index : ", index , " Status : ", status)      


def GunningFogIndex(text):
    words =  nltk.wordpunct_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    
    sentence_count = len(sentences)
    word_count = 0
    complex_word_count = 0

    for w in words :
        try :
            if max(countSyllables(w)) >= 3:
                complex_word_count += 1
            word_count += 1            
        except :
            pass
        
    index = 0.4 * ((word_count/sentence_count) + 100 * (complex_word_count/word_count))
    
    print("Gunning Fog index : ", index)
    
    
def ColemanLiauIndex(text):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)    
    sentences = nltk.sent_tokenize(text)

    sentence_count = len(sentences)
    word_count = -1
    character_count = 0
    
    for w in words :
        character_count += len(w)
        word_count += 1       
          
    index = (5.88 * (character_count/word_count)) - (29.5 * (sentence_count/word_count)) - 15.8
    print("Coleman Liau index : ", index)
    

def AutomatedReadabilityIndex(text):
    tokenizer = RegexpTokenizer(r'\w+')
    words = tokenizer.tokenize(text)    
    sentences = nltk.sent_tokenize(text)

    sentence_count = len(sentences)
    word_count = 0
    character_count = 0
    
    for w in words :
        character_count += len(w)
        word_count += 1       
          
    index = (4.71 * (character_count/word_count)) + (0.5 * (word_count/sentence_count)) - 21.43
    print("Automated Readability index : ", index)


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
          
    index = math.sqrt( polysyllable_count * ( 30/sentence_count)) + 3.1291
    print("Smog index : ", index)


def PowerSumnerKearl(text):
    words =  nltk.wordpunct_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    
    sentence_count = len(sentences)
    syllable_count = 0

    for w in words :
        try :
            syllable_count += max(countSyllables(w))              
        except :
            pass     
          
    index = 0.0778 * (word_count/sentence_count) + 100 * 0.0455 * (syllable_count/word_count) - 2.2029
    print("PowerSumnerKearl : ", index)
    
    
if __name__ == "__main__":
    
    for i in range(20):
        paragraph = open("dsm5"+str(i)+".txt","r",encoding="utf-8")
        paragraph = paragraph.read()
        print("dsm5"+str(i))
        FleschReadingEaseIndex(paragraph)
        GunningFogIndex(paragraph)
        ColemanLiauIndex(paragraph)
        AutomatedReadabilityIndex(paragraph)
        SmogIndex(paragraph)
        print("\n")
    
    
