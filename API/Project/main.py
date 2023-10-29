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
from nltk.tokenize import word_tokenize
from PredictionModel import Model
import html_contents as hc
import numpy as np
from wordcloud import WordCloud
from plot import create_word_cloud
import logging
import datetime

logging.basicConfig(filename='modele_journal.log', level=logging.INFO)
#########################################################
# Funciones Adicionales
#########################################################

def tokenizer(self, text):
        return word_tokenize(text, language="spanish")

def get_image_url(ods_value):
    if ods_value == 3:
        return "https://raw.githubusercontent.com/Lina-go/PROYECTO_ECG/main/Imagenes/S_SDG_Icons_Inverted_Transparent_WEB-03.png"
    elif ods_value == 4:
        return "https://raw.githubusercontent.com/Lina-go/PROYECTO_ECG/main/Imagenes/S_SDG_Icons_Inverted_Transparent_WEB-04.png"
    elif ods_value == 5:
        return "https://raw.githubusercontent.com/Lina-go/PROYECTO_ECG/main/Imagenes/S_SDG_Icons_Inverted_Transparent_WEB-05.png"


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

    logging.info("=====================================================")
    logging.info("Iniciando el proceso de prediccion para UN solo texto")
    logging.info(f'{datetime.datetime.now()} - Entrada : {input}')

    # Crear un DataFrame con los datos
    df = pd.DataFrame(data={'Textos_espanol': [input]})
    model = Model()
    prediction = model.make_predictions(df)
    df['sdg'] = prediction['sdg']
    df.to_excel(filename, index=False)
    image_url = get_image_url(prediction['sdg'].values[0])
    logging.info(f'{datetime.datetime.now()} - Salida : {prediction["sdg"].values[0]}')
    logging.info("=====================================================")
    return templates.TemplateResponse('index.html', {"request": request, "prediction": prediction['sdg'].replace({3: "Salud y bienestar", 4: "Educación de calidad", 5:"Igualdad de género"}), "image_url": image_url})

@app.post("/predict-file")
async def predict_from_file(request: Request, file: UploadFile):
    # Leer el archivo Excel en un DataFrame
    contents = await file.read()
    df = read_excel(BytesIO(contents))
    df = df[['Textos_espanol']]
    
    logging.info("=====================================================")
    logging.info("Iniciando el proceso de prediccion para MULTIPLES textos")
    logging.info(f'{datetime.datetime.now()} - Df con tamanio : {df.shape}')
    logging.info(f'{datetime.datetime.now()} - Entrada Columnas: {df.columns}')
    # Hacer predicciones en los datos Excel usando el modelo de aprendizaje automático
    model = Model()

    predictions = model.make_predictions(df)
    # Unir el Excel de entrada y las predicciones en un único DataFrame
    results_df = concat([df, predictions["sdg"]], axis=1)
    logging.info(f'{datetime.datetime.now()} - Salida : {results_df["sdg"].value_counts()}')
    logging.info(f"Porcentajes de cada clase: {results_df['sdg'].value_counts(normalize=True) * 100}")


    logging.info("Inicio de la creacion de nubes de palabras")
    feature_names =model.model.vectorizer.vectorizer.get_feature_names_out()
    coefficients = model.model.model.coef_

    fig3,fig4,fig5 = create_word_cloud(results_df,coefficients,feature_names)
    fig3,fig4,fig5 = fig3.to_json(),fig4.to_json(),fig5.to_json()

    # Guardar el DataFrame de resultados en un archivo Excel en la carpeta "assets"

    results_df.to_excel("uploaded/reviews_result.xlsx", index=False)
    custom_colors = ["#C5192D", "#4C9F38","#FF3A21"] 
    logging.info("Inicio de la creacion de grafica de pie")
    fig = go.Figure(
        data=[go.Pie(
            labels=results_df['sdg'].copy().replace({3: "3:Salud y bienestar", 4: "4:Educación de calidad", 5:"5:Igualdad de género"}).value_counts().index,
            values=results_df['sdg'].copy().replace({3: "3:Salud y bienestar", 4: "4:Educación de calidad", 5:"5:Igualdad de género"}).value_counts().values,
            marker=dict(colors=custom_colors),
            
        )],
        layout=go.Layout(width=500, height=400),
    )
    
    logging.info("Fin de la creación de gráfica de pie con los valores\n" +
    "{}".format(results_df['sdg'].copy().replace({3: '3:Salud y bienestar', 4: '4:Educacion de calidad', 5: '5:Igualdad de genero'}).value_counts()))


    
    fig.update_layout(
        title="Gráfica de Pie: Objetivos de Desarrollo Sostenible",
        legend_title="ODS",
    )
    html_content = hc.html_content_pie_graph()%(fig.to_json(),fig3,fig4,fig5)
    logging.info("=====================================================")
    return HTMLResponse(content=html_content, status_code=200)

@app.get("/download")
async def get_data():
   # Devolver el archivo como respuesta
   logging.info("=====================================================")
   logging.info("Descargando el archivo de resultados")
   logging.info(f'{datetime.datetime.now()} - Archivo : {filename}')
   logging.info("=====================================================")
   return FileResponse(filename, filename="reviews_result.xlsx")
