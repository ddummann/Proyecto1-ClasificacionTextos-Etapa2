import pickle
import re
from pathlib import Path



BASE_DIR = Path(__file__).resolve(strict=True).parent

# Open joblib pipeline file

with open(f"{BASE_DIR}/pipeline.jlib", "rb") as f:
    model = pickle.load(f)

classes = ["3","4","5"]


def predict_pipeline(text):
    text = re.sub(r'[!@#$(),\n"%^*?\:;~`0-9]', " ", text)
    text = re.sub(r"[[]]", " ", text)
    text = text.lower()
    pred = model.predict([text])
    pass