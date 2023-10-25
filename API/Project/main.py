import os
import sys
import csv
import pandas as pd
import plotly.graph_objects as go
from unidecode import unidecode
from io import StringIO, BytesIO
#from django.http import FileResponse
from fastapi import FastAPI, UploadFile, Request
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, FileResponse
from pandas import read_excel
from pandas import concat

from PredictionModel import Model
import html_contents as hc

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(os.path.dirname(current))
sys.path.append(parent)


app = FastAPI()


# ========= #
# TEMPLATES #
# ========= #

templates = Jinja2Templates(directory="templates")

# ========== #
# CONTROLLER #
# ========== #

filename = 'uploaded/reviews_result.xlsx'

@app.get("/")
async def root(request: Request):
    # Devuelve la plantilla index.html
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/predict-text")
async def predict_from_textarea(request: Request, input: str):
    # Nombre del archivo Excel que se va a escribir
    filename = 'uploaded/review.xlsx'
    input = unidecode(input)

    # Crear un DataFrame con los datos
    df = pd.DataFrame(data={'Textos_espanol': [input]})
    model = Model()
    prediction = model.make_predictions(df)
    df['sdg'] = prediction['sdg']
    df.to_excel(filename, index=False)
    return templates.TemplateResponse('index.html', {"request": request, "prediction": prediction['sdg'].replace({1: "negativo", 0: "positivo"})})

@app.post("/predict-file")
async def predict_from_file(request: Request, file: UploadFile):
    # Leer el archivo Excel en un DataFrame
    contents = await file.read()
    df = read_excel(BytesIO(contents))
    df = df[['Textos_espanol']]
    print(df.columns)
    # Hacer predicciones en los datos Excel usando el modelo de aprendizaje automático
    model = Model()
    predictions = model.make_predictions(df)

    # Unir el Excel de entrada y las predicciones en un único DataFrame
    results_df = concat([df, predictions['sdg'].replace({1: "negativo", 0: "positivo"})], axis=1)

    # Guardar el DataFrame de resultados en un archivo Excel en la carpeta "assets"

    results_df.to_excel("uploaded/reviews_result.xlsx", index=False)
    custom_colors = ["#C5192D", "#4C9F38"] 
    # Graficar:
    fig = go.Figure(
        data=[go.Pie(
            labels=results_df['sdg'].replace({1: "negativo", 0: "positivo"}).value_counts().index,
            values=results_df['sdg'].replace({1: "negativo", 0: "positivo"}).value_counts().values,
            marker=dict(colors=custom_colors),
        )],
        layout=go.Layout(width=400, height=400),
    )

    fig.update_layout(
        title="Gráfica de Pie: Sentimento de reviews",
        legend_title="Sentimiento",
    )
    
    html_content = hc.html_content_pie_graph() % fig.to_json() #.format(plot_div)

    return HTMLResponse(content=html_content, status_code=200)

@app.get("/download")
async def get_data():
   # Devolver el archivo como respuesta
   return FileResponse(filename, filename="reviews_result.xlsx")
