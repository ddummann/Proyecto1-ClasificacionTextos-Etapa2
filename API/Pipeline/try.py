from API.Pipeline.limpiar import Pipeline
import pandas as pd

""" Crear pipeline """

pipeline = Pipeline()

""" Crear una horación y convertir en df"""

sentence = pd.DataFrame({'texto': ['las mujeres son fuertes.']})

""" Predecir """

prediction = pipeline.predict(sentence["texto"])
""" Mostrar predicción """

print(prediction)
