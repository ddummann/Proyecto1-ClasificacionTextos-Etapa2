from joblib import load
import pandas as pd
from nltk.tokenize import word_tokenize

pipeline = load('thePipeline.joblib')