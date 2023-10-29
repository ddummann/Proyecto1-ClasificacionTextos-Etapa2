import re
import sys
import os
import pandas as pd
import joblib as jb

from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize.casual import casual_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import pandas as pd
import datetime
import logging
logging.basicConfig(filename='modele_journal.log', level=logging.INFO)

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)

from clean import Pipeline

def tokenizer(text):
    return word_tokenize(text, language="spanish")

class Model:

    def __init__(self):
        self.model = None
        self.result = None
        self.df = None

    def tokenizer(self, text):
        return word_tokenize(text, language="spanish")
    
    def make_predictions(self, data):
        logging.info("Inicio de prediccion")
        self.model = Pipeline()
        self.result = self.model.predict(data['Textos_espanol'])
        logging.info("Finalizacion de transformacion con TF-IDF")
        logging.info("Prediccion finalizada")
        df = pd.DataFrame(self.result, columns=['sdg'])
        self.df = pd.concat([data, df], axis=1)
        return df
        