import nltk
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from flask import Flask, render_template, request
from scipy import spatial
from flask import Flask, session
from flask_session import Session
import datetime
import db_connection as db

# nlp = spacy.load('en_core_web_md')
nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load('{en_core_web_md}')


def removestop_words(string1, string2):
    example_sent1 = string1
    example_sent2 = string2
    print(example_sent1)
    print(example_sent2)
    stop_words = set(stopwords.words('english'))

    word_tokens1 = word_tokenize(example_sent1)
    word_tokens2 = word_tokenize(example_sent2)

    filtered_sentence1 = [w for w in word_tokens1 if not w in stop_words]

    filtered_sentence1 = []

    for w in word_tokens1:
        if w not in stop_words:
            filtered_sentence1.append(w)
    print(example_sent1)
    print(word_tokens1)
    print(filtered_sentence1)
    filtered_sentence2 = [w for w in word_tokens2 if not w in stop_words]

    filtered_sentence2 = []

    for w in word_tokens2:
        if w not in stop_words:
            filtered_sentence2.append(w)
    print(example_sent2)
    print(word_tokens2)
    print(filtered_sentence2)
    return {"f1": filtered_sentence1, "f2": filtered_sentence2}


def get_cosine_similarity(str1, str2):
    # wordlist1 = list(str1.split(" "))
    # wordlist2 = list(str2.split(" "))
    c1 = len(str1)
    c2 = len(str2)
    vector1 = []
    vector2 = []
    if c1 == c2:
        for word in str1:
            print("str 1", word)
            vector1 = vector1 + (list(nlp(word).vector))
        for word in str2:
            print("str 2", word)
            vector2 = vector2 + list(nlp(word).vector)
    elif c1 < c2:
        for i in range(c1, c2):
            str1.append('none')
        for word in str1:
            print("str 1", word)
            vector1 = vector1 + (list(nlp(word).vector))
        for word in str2:
            print("str 2", word)
            vector2 = vector2 + list(nlp(word).vector)
    elif c2 < c1:
        for i in range(c2, c1):
            str2.append('none')
        for word in str1:
            print("str 1", word)
            vector1 = vector1 + (list(nlp(word).vector))
        for word in str2:
            print("str 2", word)
            vector2 = vector2 + list(nlp(word).vector)

    result = 1 - spatial.distance.cosine(vector1, vector2)
    print("Similarity", result)

    return result
# string1 = "class is defined as the number of entities present in it."
# string2 = "Class is a blue print which reflects the entities attributes and actions. Technically defining a class is designing an user defined data type."
# a=removestop_words(string1,string2)
# print(a)
# print(a["f1"])
# print(a["f2"])
# get_cosine_similarity(a["f1"],a["f2"])
