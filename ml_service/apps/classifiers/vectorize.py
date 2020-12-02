from sklearn.feature_extraction.text import HashingVectorizer
import joblib
import re

stop = joblib.load('stopword.joblib')
def tokenize(review):
    text = re.sub('[^a-zA-Z0-9]',' ',review)
    text = re.sub('\W+','',text)
    tokenize =list( filter(lambda x:x if x not in stop,text))
    return tokenize

vect = HashingVectorizer(n_features=2**21,preprocessor=None,decode_error='ignore',teokenizer=tokenize)


