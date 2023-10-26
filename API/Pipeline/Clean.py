from joblib import load

import logging
import datetime

from nltk.stem import SnowballStemmer
import spacy
import re, unicodedata

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from num2words import num2words
from sklearn.base import BaseEstimator, TransformerMixin

class Clean(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.stop_words = stopwords.words('spanish')
    
    def fit(self, X, y=None):
        print('Fitting ...')
        return self
    
    def transform(self, X, y=None):
        print('Transforming ...')
        X = X.apply(self.clean_text)
        return X
    
    ########################################
    # Funciones para limpieza de texto
    ########################################
    @staticmethod
    def tokenizer(text):
        return word_tokenize(text, language="spanish")

    @staticmethod
    def remove_non_ascii(words):
        """Remove non-ASCII characters from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
            new_words.append(new_word)
        return new_words

    @staticmethod
    def to_lowercase(words):
        """Convert all characters to lowercase from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = word.lower()
            new_words.append(new_word)
        return new_words

    @staticmethod
    def remove_punctuation(words):
        """Remove punctuation from list of tokenized words"""
        new_words = []
        for word in words:
            new_word = re.sub(r'[^\w\s]', '', word)
            if new_word != '':
                new_words.append(new_word)
        return new_words

    @staticmethod
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

    @staticmethod
    def remove_stopwords(words):
        """Remove stop words from list of tokenized words"""
        new_words = []
        for word in words:
            if word not in set(stopwords.words('spanish')):
                new_words.append(word)
        return new_words

    @staticmethod
    def join_words(words):
        """Join a list of words into a single string"""
        return ' '.join(map(str, words))
    
    @staticmethod
    def preprocessing(words):
        words = Clean.to_lowercase(words)
        words = Clean.replace_numbers(words)
        words = Clean.remove_punctuation(words)
        words = Clean.remove_non_ascii(words)
        words = Clean.remove_stopwords(words)
        words = Clean.join_words(words)
        return words
    
    ############################################################
    # Preprocesamiento Funciones: LEMATIZACIÓN
    ############################################################
    @staticmethod
    def stem_words(text):
        """Stem words in a text (Spanish)"""
        stemmer = SnowballStemmer("spanish")
        words = word_tokenize(text, language="spanish")
        stems = [stemmer.stem(word) for word in words]
        return stems
    @staticmethod
    def lemmatize_verbs(text):
        """Lemmatize verbs in text (Spanish)"""
        nlp = spacy.load("es_core_news_sm")
        doc = nlp(text)
        lemmas = [token.lemma_ if token.pos_ == "VERB" else token.text for token in doc]
        return lemmas
    
    @staticmethod
    def stem_and_lemmatize(words):
        stems = Clean.stem_words(words)
        lemmas = Clean.lemmatize_verbs(words)
        return Clean.join_words(stems + lemmas)
    
    ############################################################
    # Preprocesamiento entero
    ############################################################
    def clean_text(self, text):
        text = word_tokenize(text, language="spanish")
        text = Clean.preprocessing(text)
        text = Clean.stem_and_lemmatize(text)
        return text