import nltk
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import random
import string

f = open('chatbot.txt','r',errors='ignore')
raw = f.read()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)

lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remov_pun = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remov_pun)))

GREETING_INPUTS = ("hello", "hi", "greetings","wassup","hey")
GREETING_RESPONSES = ["hi","hey","Hi There","I'm glad that you are talking to me"]

def greetCheck(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def responseText(user_response):
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1],tfidf)
    idx = vals.argsort()[0][-2]
    sent_tokens.remove(user_response)
    return sent_tokens[idx]