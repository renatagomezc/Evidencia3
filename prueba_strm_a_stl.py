# -*- coding: utf-8 -*-
"""prueba strm a stl.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1K5Gv-RSuHtN4EEIZ_bxZG9wiNMKL21dM
"""

import pandas as pd
from pandas import Series, DataFrame
import numpy as np
from datetime import date, time, datetime, timedelta
import altair as alt
import streamlit as st

saldos = pd.read_excel('https://docs.google.com/spreadsheets/d/1dSha-aNdhL2X4GEDXpVEi42MM-7wzEHf/edit?usp=drive_link&ouid=105604475892839273410&rtpof=true&sd=true')

Principal = '#ba1424'
Complemento = '#746c6c'
Calor =['#ba1424', '#c52f31','#680c09','#746c6c', '#8a0e1a', '#444441']

actual= datetime(2023, 3, 26, 21, 57, 54, 615623) #datetime.now()
actual

saldos['FECHA_ACT']=actual
saldos['FECHA_ACT']

saldos['TIPO'] = np.where(saldos['FECHA_VENCIMIENTO'] >= saldos['FECHA_ACT'], 'CLIENTES CRÉDITO', 'CARTERA VENCIDA')

saldos['dias'] = saldos['FECHA_VENCIMIENTO'] - saldos['FECHA_FACTURA']

saldos['TIPO_DIAS'] = np.where(saldos['dias'] <= '30 days' , '1-30', '31-60 o 30<')

cobranza = pd.DataFrame()
cobranza['MONTO ADEUDADO'] = saldos.groupby(['TIPO','TIPO_DIAS'])['MONTO ADEUDADO'].sum()

cobranza = cobranza.reset_index()

cobranza['TIPO CARTERA'] = cobranza['TIPO'] + ' ' + cobranza['TIPO_DIAS']

saldos_1=saldos[['NOMBRE', 'FACTURA','MONTO ADEUDADO', 'TIPO', 'TIPO_DIAS']]

saldos_1['TIPO CARTERA'] = saldos_1['TIPO'] + ' ' + saldos_1['TIPO_DIAS']

click=alt.selection_multi(encodings=['color'])
graf1 = alt.Chart(cobranza).mark_bar().encode(
    x= alt.X('TIPO CARTERA',title='TIPO CARTERA',axis=alt.Axis(labelAngle=45)),
    y= 'MONTO ADEUDADO',
    color=alt.condition(click,'TIPO CARTERA',alt.value('#ffe7e7'),)
).properties(height=300,width=300,title='Cobranza').add_selection(click)

graf1_2=alt.Chart(cobranza).mark_text(
    color='#913127',
    font='gothic',
    fontSize=13,
    dy=-8,
).encode(
    x=alt.X('TIPO CARTERA'),
    y=alt.Y('MONTO ADEUDADO'),
    text=alt.Text('MONTO ADEUDADO'),
).properties(height=300,width=300)

graf1_1=alt.layer(graf1,graf1_2)

graf = alt.Chart(saldos_1).mark_bar().encode(
    x= alt.X('NOMBRE',title='CLIENTE',axis=alt.Axis(labelAngle=45)),
    y= 'MONTO ADEUDADO',
    color=alt.Color('TIPO CARTERA', scale=alt.Scale(range=['#ba1424','#ba1424','#a4a4a4','#a4a4a4'])) #ffb999
).properties(title='Clientes deudores').transform_filter(click)

graf_cobranza= graf1_1 | graf
graf_cobranza

st.altair_chart(graf_cobranza, use_container_width=True)

