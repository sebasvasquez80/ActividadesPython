import streamlit as st
import pandas as pd
import io

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 2")

st.header("Descripción de la actividad")
st.markdown("""
Esta actividad es una introducción práctica a Python y a las estructuras de datos básicas.
En ella, exploraremos los conceptos fundamentales de Python y aprenderemos a utilizar variables,
tipos de datos, operadores, y las estructuras de datos más utilizadas como listas, tuplas,
diccionarios y conjuntos.
""")

st.header("Objetivos de aprendizaje")

st.markdown("""
- Comprender los tipos de datos básicos en Python
- Aprender a utilizar variables y operadores
- Dominar las estructuras de datos fundamentales
- Aplicar estos conocimientos en ejemplos prácticos
""")

st.header("Solución actividad 2")

st.subheader("CSV Estudiantes en Colombia")

df = pd.read_csv("assets/estudiantes_colombia.csv")

st.subheader("Primeras 5 filas del dataset")
st.dataframe(df.head())

st.subheader("Últimas 5 filas del dataset")
st.dataframe(df.tail())

st.subheader("Información general del dataset")

buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()

st.code(info_str, language='text')

st.subheader("Resumen estadístico")
st.dataframe(df.describe())

st.subheader("Seleccionar columnas específicas")
columnas_fijas = ["nombre", "edad", "promedio"]
st.dataframe(df[columnas_fijas])

st.subheader("Filtrar por promedio")
umbral = st.slider("Selecciona el promedio mínimo", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
df_filtrado = df[df["promedio"] >= umbral]
st.write(f"Mostrando estudiantes con promedio mayor o igual a {umbral}:")
st.dataframe(df_filtrado)

st.code("""
    df = pd.read_csv("assets/estudiantes_colombia.csv")

st.subheader("Primeras 5 filas del dataset")
st.dataframe(df.head())

st.subheader("Últimas 5 filas del dataset")
st.dataframe(df.tail())

st.subheader("Información general del dataset")

buffer = io.StringIO()
df.info(buf=buffer)
info_str = buffer.getvalue()

st.code(info_str, language='text')

st.subheader("Resumen estadístico")
st.dataframe(df.describe())

st.subheader("Seleccionar columnas específicas")
columnas_fijas = ["nombre", "edad", "promedio"]
st.dataframe(df[columnas_fijas])

st.subheader("Filtrar por promedio")
umbral = st.slider("Selecciona el promedio mínimo", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
df_filtrado = df[df["promedio"] >= umbral]
st.write(f"Mostrando estudiantes con promedio mayor o igual a {umbral}:")
st.dataframe(df_filtrado)
""", language='python')