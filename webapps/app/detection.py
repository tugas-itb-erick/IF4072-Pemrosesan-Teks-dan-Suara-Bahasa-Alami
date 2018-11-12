import numpy as np
import re, nltk, os, string, pickle
from keras import models
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from sklearn.externals import joblib

def build_Word_Vector(tokens, size):
    vec = np.zeros(size).reshape((1, size))
    count = 0.
    for word in tokens:
        print(word)
        try:
            vec += model_w2v[word].reshape((1, size)) * tfidf[word]
            count += 1.
        except (KeyError, IndexError): 
            continue
    if count != 0:
        vec /= count
    return vec

def expand_contractions(text) :
    pattern = re.compile("({})".format("|".join(CONTRACTION_MAP.keys())),flags = re.DOTALL| re.IGNORECASE)
    
    def replace_text(t):
        txt = t.group(0)
        if txt.lower() in CONTRACTION_MAP.keys():
            return CONTRACTION_MAP[txt.lower()]
        
    expand_text = pattern.sub(replace_text,text)
    return expand_text

def cleanhtml(text):
    cleanr = re.compile('&#[0-9]+;')
    cleantext = re.sub(cleanr, '', text)
    return cleantext

def clean_emoji(text):
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)
    
def normalizer(text):
    stop_words = set(stopwords.words('english'))
    wordnet_lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()
    text = re.sub(r"http\S+", "", text.lower(), flags=re.MULTILINE) #remove url
    text = re.sub('@[^\s]+','',text) #remove username
    text = clean_emoji(text)
    text = cleanhtml(text)
    expand = expand_contractions(text)
    pattern = re.compile("[{}]".format(re.escape(string.punctuation)))
    filter_char =  filter(None,[pattern.sub('' ,expand)])
    text_filter_char =  " ".join(filter_char)
    tokens = nltk.WhitespaceTokenizer().tokenize(text_filter_char)
    lemmas = [wordnet_lemmatizer.lemmatize(t) for t in tokens]
    stems = [stemmer.stem(t) for t in lemmas]
    filtered_result = list(filter(lambda l: l not in stop_words, stems))
    concate = ' '.join(filtered_result)
    return concate

def predict_aspect(text):
    # 0: not given
    # 1: exist
    text = normalizer(text)
    tokens = nltk.WhitespaceTokenizer().tokenize(text)
    vecs = build_Word_Vector(tokens, 200)
    vecs = vecs.reshape((1, 1, 200))
    aspect = {}
    aspect['physic'] = int(round(model_ad_physics.predict(vecs)[0][0]))
    aspect['race'] = int(round(model_ad_race.predict(vecs)[0][0]))
    aspect['religion'] = int(round(model_ad_religion.predict(vecs)[0][0]))
    return aspect

def predict_hate(text):
    # 0: no hate
    # 1: hate
    text = normalizer(text)
    tokens = nltk.WhitespaceTokenizer().tokenize(text)
    vecs = build_Word_Vector(tokens, 200)
    vecs_reshape = vecs.reshape((1, 1, 200))
    aspect = {}
    aspect['physic'] = int(round(model_hd_physics.predict(vecs_reshape)[0][0]))
    aspect['race'] = int(round(model_hd_race.predict(vecs)[0]))
    aspect['religion'] = int(round(model_hd_religion.predict(vecs)[0]))
    print(model_hd_physics.predict(vecs_reshape)[0][0])
    print(model_hd_race.predict(vecs)[0])
    print(model_hd_religion.predict(vecs)[0])
    return aspect

CONTRACTION_MAP = {"ain't": "is not", "aren't": "are not","can't": "cannot", 
                   "can't've": "cannot have", "'cause": "because", "could've": "could have", 
                   "couldn't": "could not", "couldn't've": "could not have","didn't": "did not", 
                   "doesn't": "does not", "don't": "do not", "hadn't": "had not", 
                   "hadn't've": "had not have", "hasn't": "has not", "haven't": "have not", 
                   "he'd": "he would", "he'd've": "he would have", "he'll": "he will", 
                   "he'll've": "he he will have", "he's": "he is", "how'd": "how did", 
                   "how'd'y": "how do you", "how'll": "how will", "how's": "how is", 
                   "I'd": "I would", "I'd've": "I would have", "I'll": "I will", 
                   "I'll've": "I will have","I'm": "I am", "I've": "I have", 
                   "i'd": "i would", "i'd've": "i would have", "i'll": "i will", 
                   "i'll've": "i will have","i'm": "i am", "i've": "i have", 
                   "isn't": "is not", "it'd": "it would", "it'd've": "it would have", 
                   "it'll": "it will", "it'll've": "it will have","it's": "it is", 
                   "let's": "let us", "ma'am": "madam", "mayn't": "may not", 
                   "might've": "might have","mightn't": "might not","mightn't've": "might not have", 
                   "must've": "must have", "mustn't": "must not", "mustn't've": "must not have", 
                   "needn't": "need not", "needn't've": "need not have","o'clock": "of the clock", 
                   "oughtn't": "ought not", "oughtn't've": "ought not have", "shan't": "shall not",
                   "sha'n't": "shall not", "shan't've": "shall not have", "she'd": "she would", 
                   "she'd've": "she would have", "she'll": "she will", "she'll've": "she will have", 
                   "she's": "she is", "should've": "should have", "shouldn't": "should not", 
                   "shouldn't've": "should not have", "so've": "so have","so's": "so as", 
                   "this's": "this is",
                   "that'd": "that would", "that'd've": "that would have","that's": "that is", 
                   "there'd": "there would", "there'd've": "there would have","there's": "there is", 
                   "they'd": "they would", "they'd've": "they would have", "they'll": "they will", 
                   "they'll've": "they will have", "they're": "they are", "they've": "they have", 
                   "to've": "to have", "wasn't": "was not", "we'd": "we would", 
                   "we'd've": "we would have", "we'll": "we will", "we'll've": "we will have", 
                   "we're": "we are", "we've": "we have", "weren't": "were not", 
                   "what'll": "what will", "what'll've": "what will have", "what're": "what are", 
                   "what's": "what is", "what've": "what have", "when's": "when is", 
                   "when've": "when have", "where'd": "where did", "where's": "where is", 
                   "where've": "where have", "who'll": "who will", "who'll've": "who will have", 
                   "who's": "who is", "who've": "who have", "why's": "why is", 
                   "why've": "why have", "will've": "will have", "won't": "will not", 
                   "won't've": "will not have", "would've": "would have", "wouldn't": "would not", 
                   "wouldn't've": "would not have", "y'all": "you all", "y'all'd": "you all would",
                   "y'all'd've": "you all would have","y'all're": "you all are","y'all've": "you all have",
                   "you'd": "you would", "you'd've": "you would have", "you'll": "you will", 
                   "you'll've": "you will have", "you're": "you are", "you've": "you have" } 

pwd = os.path.dirname(__file__)

model_ad_physics = pickle.load(open(pwd + '/trained_models/model_ad_physics.sav', 'rb'))
model_ad_race = pickle.load(open(pwd + '/trained_models/model_ad_race.sav', 'rb'))
model_ad_religion = pickle.load(open(pwd + '/trained_models/model_ad_religion.sav', 'rb'))

model_hd_physics = models.load_model(pwd + '/trained_models/model_hd_physics.sav')
model_hd_race = joblib.load(pwd + '/trained_models/model_hd_race.sav')
model_hd_religion = joblib.load(pwd + '/trained_models/model_hd_religion.sav')

model_w2v = pickle.load(open(pwd + '/trained_models/model_w2v.sav', 'rb'))
tfidf = pickle.load(open(pwd + '/trained_models/tfidf.sav', 'rb'))
