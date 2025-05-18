import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 4")

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

st.header("Solución")

data = {
    'producto': [
        'Manzanas', 'Bananas', 'Peras', 'Uvas', 'Naranjas',
        'Tomates', 'Zanahorias', 'Lechuga', 'Cebolla', 'Papas',
        'Arroz', 'Lentejas', 'Huevos', 'Pollo', 'Leche'
    ],
    'precio': [
        1200, 1500, 1800, 2000, 1600,
        1300, 1100, 1000, 900, 800,
        2500, 2200, 550, 7000, 3500
    ],
    'stock': [
        25, 40, 30, 15, 50,
        60, 70, 55, 80, 90,
        100, 85, 200, 45, 75
    ],
    'categoria': [
        'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta',
        'Verdura', 'Verdura', 'Verdura', 'Verdura', 'Verdura',
        'Grano', 'Grano', 'Proteína', 'Proteína', 'Lácteo'
    ]
}

df_original = pd.DataFrame(data)

df = df_original.copy()

st.subheader(" Tabla completa")
st.dataframe(df)

st.sidebar.header(" Opciones de modificación y exploración")

if st.sidebar.checkbox("Filtrar por precio mínimo"):
    precio_min = st.sidebar.slider("Precio mínimo", min_value=1000, max_value=3000, step=100, value=1500)
    df = df.loc[df['precio'] >= precio_min]

if st.sidebar.checkbox("Modificar stock con .loc"):
    producto_a_modificar = st.sidebar.selectbox("Seleccionar producto", df['producto'])
    nuevo_stock = st.sidebar.number_input("Nuevo stock", min_value=0, value=0, step=1)
    df.loc[df['producto'] == producto_a_modificar, 'stock'] = nuevo_stock
    st.success(f" Stock actualizado para {producto_a_modificar} a {nuevo_stock} unidades.")

if st.sidebar.checkbox("Mostrar fila por índice (iloc)"):
    index = st.sidebar.slider("Selecciona un índice", min_value=0, max_value=len(df_original)-1, value=0)
    st.subheader(f" Fila {index} usando `.iloc`")
    st.write(df_original.iloc[index])

if st.sidebar.checkbox("Mostrar fila por nombre (loc)"):
    producto = st.sidebar.selectbox("Seleccionar producto para ver (loc)", df_original['producto'])
    st.subheader(f" Información de {producto} usando `.loc`")
    st.write(df_original.loc[df_original['producto'] == producto])

st.subheader("Tabla final después de aplicar filtros o modificaciones")
st.dataframe(df)

st.markdown("Codigo")

st.code("""
    
data = {
    'producto': [
        'Manzanas', 'Bananas', 'Peras', 'Uvas', 'Naranjas',
        'Tomates', 'Zanahorias', 'Lechuga', 'Cebolla', 'Papas',
        'Arroz', 'Lentejas', 'Huevos', 'Pollo', 'Leche'
    ],
    'precio': [
        1200, 1500, 1800, 2000, 1600,
        1300, 1100, 1000, 900, 800,
        2500, 2200, 550, 7000, 3500
    ],
    'stock': [
        25, 40, 30, 15, 50,
        60, 70, 55, 80, 90,
        100, 85, 200, 45, 75
    ],
    'categoria': [
        'Fruta', 'Fruta', 'Fruta', 'Fruta', 'Fruta',
        'Verdura', 'Verdura', 'Verdura', 'Verdura', 'Verdura',
        'Grano', 'Grano', 'Proteína', 'Proteína', 'Lácteo'
    ]
}

df_original = pd.DataFrame(data)

df = df_original.copy()

st.subheader(" Tabla completa")
st.dataframe(df)

st.sidebar.header(" Opciones de modificación y exploración")

if st.sidebar.checkbox("Filtrar por precio mínimo"):
    precio_min = st.sidebar.slider("Precio mínimo", min_value=1000, max_value=3000, step=100, value=1500)
    df = df.loc[df['precio'] >= precio_min]

if st.sidebar.checkbox("Modificar stock con .loc"):
    producto_a_modificar = st.sidebar.selectbox("Seleccionar producto", df['producto'])
    nuevo_stock = st.sidebar.number_input("Nuevo stock", min_value=0, value=0, step=1)
    df.loc[df['producto'] == producto_a_modificar, 'stock'] = nuevo_stock
    st.success(f" Stock actualizado para {producto_a_modificar} a {nuevo_stock} unidades.")

if st.sidebar.checkbox("Mostrar fila por índice (iloc)"):
    index = st.sidebar.slider("Selecciona un índice", min_value=0, max_value=len(df_original)-1, value=0)
    st.subheader(f" Fila {index} usando `.iloc`")
    st.write(df_original.iloc[index])

if st.sidebar.checkbox("Mostrar fila por nombre (loc)"):
    producto = st.sidebar.selectbox("Seleccionar producto para ver (loc)", df_original['producto'])
    st.subheader(f" Información de {producto} usando `.loc`")
    st.write(df_original.loc[df_original['producto'] == producto])

st.subheader("Tabla final después de aplicar filtros o modificaciones")
st.dataframe(df)
""", language='python')