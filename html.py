# -*- coding: utf-8 -*-
"""html.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1syhJxyV_WZexmBj7ICE1iqeHeOwjIno_
"""

import streamlit as st
# Abrir el archivo HTML y leer su contenido
with open('grafica.html', 'r') as file:
    html_content = file.read()

# Mostrar el contenido HTML en Streamlit utilizando st.markdown

st.markdown('<iframe src="grafica.html" height="500" width="800"></iframe>', unsafe_allow_html=True)