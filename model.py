from joblib import load

import logging
import datetime

from nltk.stem import SnowballStemmer
import spacy
import re, unicodedata

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from num2words import num2words


classes = {
    3: 'Salud y bienestar',
    4: 'Educación de calidad',
    5: 'Igualdad de género'
}


############################################################
# Preprocesamiento Funciones: LIMPIEZA DE TEXTO
############################################################

def tokenizer(text):
    return word_tokenize(text, language="spanish")

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words

def replace_numbers(words):
    """Replace all integer occurrences in list of tokenized words with textual representation in Spanish"""
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = num2words(int(word), lang='es')
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    for word in words:
        if word not in set(stopwords.words('spanish')):
            new_words.append(word)
    return new_words
def join_words(words):
    """Join a list of words into a single string"""
    return ' '.join(map(str, words))

def preprocessing(words):
    words = to_lowercase(words)
    words = replace_numbers(words)
    words = remove_punctuation(words)
    words = remove_non_ascii(words)
    words = remove_stopwords(words)
    words = join_words(words)
    return words

############################################################
# Preprocesamiento Funciones: LEMATIZACIÓN
############################################################
def stem_words(text):
    """Stem words in a text (Spanish)"""
    stemmer = SnowballStemmer("spanish")
    words = tokenizer(text)
    stems = [stemmer.stem(word) for word in words]
    return stems
def lemmatize_verbs(text):
    """Lemmatize verbs in text (Spanish)"""
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(text)
    lemmas = [token.lemma_ if token.pos_ == "VERB" else token.text for token in doc]
    return lemmas

def stem_and_lemmatize(words):
    stems = stem_words(words)
    lemmas = lemmatize_verbs(words)
    return join_words(stems + lemmas)


############################################################
# Preprocesamiento entero
############################################################

def full_preprocessing(text):
    text = tokenizer(text)
    text = preprocessing(text)
    text = stem_and_lemmatize(text)
    return text


############################################################
# Pipeline
############################################################

pipeline = load('thePipeline.joblib')

logging.basicConfig(filename='modele_journal.log', level=logging.INFO)

text = str(input('Entra un texto : '))
current_time = datetime.datetime.now()

logging.info(f'{current_time} - Entrada : {text}')

## hay como un problema con stem_and_lemmatize
# print(full_preprocessing(text))


num = pipeline.predict([full_preprocessing(text)])[0]
logging.info(f'{current_time} - Salida : {classes[num]}')

print(f'Este texto es relacionado con : {classes[num]}')