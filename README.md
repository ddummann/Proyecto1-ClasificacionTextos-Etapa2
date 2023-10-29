# :stethoscope: :orange_book:	 Proyecto1-ClasificacionTextos 

Este es el proyecto de la etapa 1 de analítica de textos del curso de Inteligencia de Negocios. Este proyecto hace parte del grupo 37.Los datos etiquetados se encuentran en la carpeta data y los integrantes son:

Antonin Bouillaud – 202325830 
Ernesto José Duarte Mantilla – 202014279 
Lina María Gómez Mesa – 201923531 

## Deployment

1. Antes de ejecutar la API, se deben instalar las librerías usadas. Esto se puede hacer corriendo la siguiente línea en una consola:

```bash
pip install -r requirements.txt
```
2. Luego, ingrese dentro de la siguiente ruta:
```bash
cd API/Project
```
3. Ejecute el siguiente comando para instalar las dependencias  de nltk:

```bash
python installations.py
```
4. Ejecute el siguiente comando para instalar las dependencias  de spacy:
```bash
python -m spacy download es_core_news_sm
```
5. Corra el proyecto con el siguiente comando

```bash
python -m uvicorn main:app --reload
```

6. Ingrese a la URL que se muestra a continuación en su buscador de preferencia:

[         LINK PROYECTO](http://127.0.0.1:8000)

7. Si desea detener la ejecución de la API, presione las teclas **Ctrl + C** en la consola donde se está ejecutando la API.

## Funcionalidades :hammer_and_wrench:

Este _deployment_ tiene dos funcionalidades específicas: 

1. La primera es cargar un archivo. Esta está dirigida a usuarios de la organización que deseen clasificar un archivo .xlsx y obtener el archivo clasificado. Hay archivos para que se pruebe en la carpeta **API/Data** tienen la inicial **SinEtiquetasTest**.
  
2. La segunda funcionalidad es escribir un comentario en el cuadro de texto que se presenta en la página. Esta puede funcionar para cualquier ciudadano. 

Nota: Sea paciente con la API, ya que puede tardar un poco en cargar el archivo y en clasificarlo.


## Log 
En la carpeta **API/Project** se encuentra el archivo **uvicorn.log** que contiene el log de la ejecución de la API. Hay dos archivos log:

1. **modele_journal.log** contiene el log de la ejecución de los inputs del usuario.
2. **uvicorn.log** contiene el log de la ejecución de la API.

## Documentación

[Documento](https://uniandes-my.sharepoint.com/:w:/g/personal/l_gomez1_uniandes_edu_co/EVw6ihN8RldBhNl3dIRPwf0BtF0ba_XmWGu58bwDN7WPmw?e=Nzcc2z)

[PresentacionFinal](https://www.canva.com/design/DAFyLVKBK4I/RxqTe5s_oyTBGpJ2mF8wPw/edit?utm_content=DAFyLVKBK4I&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)
