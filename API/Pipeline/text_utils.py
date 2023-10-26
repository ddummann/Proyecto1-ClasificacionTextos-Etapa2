# %%
from joblib import load
import pandas as pd
from nltk.tokenize import word_tokenize

# %%
textes = ["ienferm hospit", "encan traba", "mujer hombres"]

data = pd.DataFrame({'Textos':textes})

data

# %%
data.iloc[2]

# %%
def tokenizer(text):
    return word_tokenize(text, language="spanish")

# %%
pipeline = load('thePipeline.joblib')

# %%
y = pipeline.predict(data['Textos'])
y

# %%
df = pd.read_excel('../data/SinEtiquetatest_cat_345.xlsx')
df.shape

# %%
df.head()


