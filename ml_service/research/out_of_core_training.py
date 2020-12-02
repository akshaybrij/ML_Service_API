import os
import re
import time
import pickle
import pyprind
import joblib
import numpy as np
import emoji
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.linear_model import SGDClassifier
from nltk.corpus import stopwords

stop = stopwords.words('english')

def tokenizer(text):
    text= re.sub('<[^>]*>','',text)
    text = re.sub('[^a-zA-Z0-9]',' ',text)
    text= re.sub('[\W+]','',text.lower())
    tokenized = [w for w in text.split() if w not in stop]
    return tokenized

def stream_docs(path):
    with open(path,'r',encoding='utf-8') as csv:
        next(csv)
        for line in csv:
            text,label = line[:-3],line[-2]
            yield text,label

def get_minibatch(doc_stream,size):
    docs,y = [],[]
    try:
        for _ in range(size):
            text,label = next(doc_stream)
            docs.append(text)
            y.append(label)
    except Exception as e:
        print(str(e))
    return docs,y

vect = HashingVectorizer(decode_error='ignore',n_features=2**21,preprocessor=None,tokenizer=tokenizer)
clf = SGDClassifier(loss='log',random_state=1,max_iter=1)
doc_stream = stream_docs('movie_data.csv')
pbar = pyprind.ProgBar(45)
classes = np.array([0,1])
for _ in range(45):
    xtrain,ytrain = get_minibatch(doc_stream,size=1000)
    if not xtrain: 
        break
    xtrain = vect.transform(xtrain)
    clf.partial_fit(xtrain,ytrain,classes=np.array(list(set(ytrain))))
    pbar.update()
xtest,ytest = get_minibatch(doc_stream,size=5000)
xtest = vect.transform(xtest)
print(clf.score(xtest,ytest))
clf.partial_fit(xtest,ytest)
joblib.dump(clf,'classifier.joblib')
joblib.dump(stop,'stopword.joblib')


