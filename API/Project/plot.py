######################################
# Libraries
######################################

import numpy as np
from wordcloud import WordCloud
import plotly.graph_objects as go

######################################
# Functions
######################################

def create_word_cloud(df,coefficients,feature_names):

    word_coeff_dict_class1,word_coeff_dict_class2,word_coeff_dict_class3 = {},{}, {}

    for text, prediction in zip(df['Textos_espanol'], df['sdg']):
        words = text.split()
        for word in words:
            if word in feature_names:
                index = list(feature_names).index(word)
                
                max_coeff = float('-inf')
                max_class = None
                for i in range(coefficients.shape[0]):
                    if coefficients[i, index] > max_coeff:
                        max_coeff = coefficients[i, index]
                        max_class = i + 3
                
                if max_class == prediction:
                    if prediction == 3:
                        word_coeff_dict_class1[word] = max_coeff
                    elif prediction == 4:
                        word_coeff_dict_class2[word] = max_coeff
                    elif prediction == 5:
                        word_coeff_dict_class3[word] = max_coeff

    
    wordcloud_class1 = WordCloud(background_color='white', width = 900, height = 600).generate_from_frequencies(word_coeff_dict_class1)
    wordcloud_class2 = WordCloud(background_color='white', width = 900, height = 600).generate_from_frequencies(word_coeff_dict_class2)
    wordcloud_class3 = WordCloud(background_color='white', width = 900, height = 600).generate_from_frequencies(word_coeff_dict_class3)

    
    wordcloud_array_class1 = np.array(wordcloud_class1)
    wordcloud_array_class2 = np.array(wordcloud_class2)
    wordcloud_array_class3 = np.array(wordcloud_class3)

    fig3 = go.Figure(data=go.Image(z=wordcloud_array_class1),layout=go.Layout(width=500, height=400))
    fig3.update_layout(title={
        'text': "Top palabras representativas ODS: 3",
        'x':0.50,
        'xanchor': 'center'
    },margin=dict(l=0, r=0,b=0),
                       xaxis=dict(showticklabels=False),
    yaxis=dict(showticklabels=False))

    fig4 = go.Figure(data=go.Image(z=wordcloud_array_class2),layout=go.Layout(width=500, height=400))
    fig4.update_layout(title={
        'text': "Top palabras representativas ODS: 4",
        'x':0.5,
        'xanchor': 'center',
        
    },margin=dict(l=0, r=0,b=0),
                       xaxis=dict(showticklabels=False),
    yaxis=dict(showticklabels=False))

    fig5 = go.Figure(data=go.Image(z=wordcloud_array_class3),layout=go.Layout(width=500, height=400))
    fig5.update_layout(title={
        'text': "Top palabras representativas ODS: 5",
        'x':0.5,
        'xanchor': 'center'
    },margin=dict(l=0, r=0,b=0),
                       xaxis=dict(showticklabels=False),
    yaxis=dict(showticklabels=False))

    return fig3,fig4,fig5

