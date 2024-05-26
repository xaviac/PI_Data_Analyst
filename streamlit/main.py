import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import datetime as dt
import folium


# Título
st.title('Siniestros viales en la Ciudad de Buenos Aires (CABA)')

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv('https://github.com/xaviac/PI_Data_Analyst/raw/main/data/clean/hechos.csv')
    return data

url = 'https://cdn.buenosaires.gob.ar/datosabiertos/datasets/transporte-y-obras-publicas/victimas-siniestros-viales/homicidios.xlsx'


@st.cache_data
# funcion que ayuda a limpiar datos nulos y registros con 'SD'
def clean_data(data):
    data = data.replace('SD', np.nan)
    data = data.dropna()
    return data

data = load_data()

# mostrar el dataframe
st.write(data.head())

hechos = load_data()

# Filtrar los datos para eliminar los valores 'SD', 'No Especificada' y '0' en la columna 'comuna'
hechos_filtrados = hechos[~hechos['comuna'].isin(['SD', 'No Especificada', '0'])]

# Calcular la frecuencia de cada valor en 'comuna'
# frecuencias = hechos_filtrados['comuna'].value_counts()
frecuencias = hechos_filtrados.groupby('comuna').size()

# Ordenar de mayor a menor valores contados
frecuencias = frecuencias.sort_values(ascending=False)

# Configurar la visualización en Streamlit
st.title('Frecuencia de Víctimas por Comuna')

# Visualizar gráfico de barras
st.bar_chart(frecuencias, use_container_width=True)


# filtrar los datos para eliminar los valores 'SD', 'No Especificada' y '0' y '.' en la columna 'pos x' y 'pos y' y convertirlos a valores flotantes
# hechos_filtrados['pos x'] = hechos_filtrados['pos x'].replace(['SD', 'No Especificada', '0', '.'], np.nan).astype(float)
# hechos_filtrados['pos y'] = hechos_filtrados['pos y'].replace(['SD', 'No Especificada', '0', '.'], np.nan).astype(float)

# # Eliminar los registros con valores nulos en 'pos x' y 'pos y'
# hechos_filtrados = hechos_filtrados.dropna(subset=['pos x', 'pos y'])

# # Crear el mapa interactivo
# st.title('Mapa Interactivo de Lugares')

# # Coordenadas del centro de tu mapa
# latitud_centro = hechos_filtrados['pos y'].mean()
# longitud_centro = hechos_filtrados['pos x'].mean()

# # Crear el mapa centrado en las coordenadas calculadas
# mapa = folium.Map(location=[latitud_centro, longitud_centro], zoom_start=11)

# # Añadir marcadores al mapa
# for _, row in hechos_filtrados.iterrows():
#     folium.Marker(location=[row['pos y'], row['pos x']], popup=row['comuna']).add_to(mapa)

# # Mostrar el mapa en Streamlit
# st.write('Los marcadores muestran la ubicación de los lugares en el mapa.')
# st.write(mapa)


# Asegúrate de que 'h_hechos' es tu DataFrame y tiene las columnas 'longitud' y 'latitud'
# h_hechos = pd.read_csv('tu_archivo.csv')

st.title('Mi mapa')

# Añade un mapa con los puntos de 'h_hechos'
# Añade un mapa con los puntos de 'h_hechos'
hechos = hechos.dropna(subset=['lat', 'lon'])
hechos['lat'] = hechos['lat'].astype(float)
hechos['lon'] = hechos['lon'].astype(float)

st.map(hechos)