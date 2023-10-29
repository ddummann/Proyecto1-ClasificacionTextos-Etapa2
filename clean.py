###############################################
# Librerias
###############################################
import pandas as pd
from joblib import load
import datetime
from nltk.stem import SnowballStemmer
import spacy
import re, unicodedata
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from num2words import num2words
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
pd.set_option('display.max_colwidth', None)
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import swifter
from joblib import dump, load
from sklearn.pipeline import Pipeline as SKPipeline
import logging
logging.basicConfig(filename='modele_journal.log', level=logging.INFO)
################################################
# Global Variables
################################################

X_train_clean = pd.read_excel("../data/cat_345_clean_con_lema.xlsx")
X_test_clean = pd.read_excel("../data/cat_345_clean_con_lema_test.xlsx")

################################################
# Funciones
################################################
def tokenizer(text):
    return word_tokenize(text, language="spanish")

##################################################
# Clase para limpieza de texto
##################################################

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
        logging.info("Inicio de preprocesamiento")
        logging.info(f"Entrada: {' '.join(map(str, words))}")
        words = Clean.to_lowercase(words)
        logging.info("Paso 1 de preprocesamiento lowercase finalizado")
        words = Clean.replace_numbers(words)
        logging.info("Paso 2 de preprocesamiento replace_numbers finalizado")
        words = Clean.remove_punctuation(words)
        logging.info("Paso 3 de preprocesamiento remove_punctuation finalizado")
        words = Clean.remove_non_ascii(words)
        logging.info("Paso 4 de preprocesamiento remove_non_ascii finalizado")
        words = Clean.remove_stopwords(words)
        logging.info("Paso 5 de preprocesamiento remove_stopwords finalizado")
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
        logging.info("Paso preprocesamiento stem_words finalizado")
        return stems
    @staticmethod
    def lemmatize_verbs(text):
        """Lemmatize verbs in text (Spanish)"""
        nlp = spacy.load("es_core_news_sm")
        doc = nlp(text)
        lemmas = [token.lemma_ if token.pos_ == "VERB" else token.text for token in doc]
        logging.info("Paso preprocesamiento lemmatize_verbs finalizado")
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
        logging.info("TODO preprocesamiento finalizado")
        return text

########################################################################
# Pipeline
########################################################################


"""                          Definición del Vectorizador TF-IDF                               """


class TextVectorizer:
    def __init__(self, X_train, X_test):
        self.vectorizer = TfidfVectorizer(
            sublinear_tf=True, 
            max_df=0.5, 
            min_df=5, 
            stop_words=stopwords.words('spanish'), 
            tokenizer=self.tokenizer
        )
        self.train_data = self.fit_transform(X_train)
        self.test_data = self.transform(X_test)

    def tokenizer(self, text):
        return word_tokenize(text, language="spanish")

    def fit_transform(self, X_train):
        return self.vectorizer.fit_transform(X_train)

    def transform(self, X_test):
        return self.vectorizer.transform(X_test)


class Pipeline:
    def __init__(self):
        self.cleaner = Clean()
        self.vectorizer = TextVectorizer(X_train_clean['texto_limpio'], X_test_clean['texto_limpio'])
        self.model = load('best_model.joblib')
        self.pipeline = SKPipeline([
            ('Cleaner', self.cleaner),
            ('Vectorizer', self.vectorizer),
            ('Model', self.model)
        ])

    def fit(self, X, y):
        self.pipeline.fit(X, y)

    def predict(self, X):
        return self.pipeline.predict(X)