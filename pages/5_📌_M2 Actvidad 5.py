import streamlit as st
import pandas as pd


# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 5")

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
st.subheader(" Operaciones de Agregar, Agrupar y Fusionar en Pandas")

df_ventas = pd.DataFrame({
    'id_venta': [1, 2, 3, 4, 5, 6],
    'producto': ['Manzanas', 'Bananas', 'Manzanas', 'Uvas', 'Bananas', 'Uvas'],
    'cantidad': [10, 5, 3, 8, 6, 4],
    'precio_unitario': [1200, 1500, 1200, 2000, 1500, 2000],
    'vendedor': ['Ana', 'Luis', 'Ana', 'Pedro', 'Luis', 'Pedro']
})
df_ventas['total'] = df_ventas['cantidad'] * df_ventas['precio_unitario']

df_vendedores = pd.DataFrame({
    'vendedor': ['Ana', 'Luis', 'Pedro'],
    'region': ['Centro', 'Norte', 'Sur'],
    'experiencia': [2, 4, 3]
})

df_productos = pd.DataFrame({
    'producto': ['Manzanas', 'Bananas', 'Uvas'],
    'categoria': ['Fruta', 'Fruta', 'Fruta'],
    'stock': [100, 80, 50]
})

st.subheader(" DataFrame de Ventas")
st.dataframe(df_ventas)

st.subheader(" DataFrame de Vendedores")
st.dataframe(df_vendedores)

st.subheader(" DataFrame de Productos")
st.dataframe(df_productos)


df_ventas_info = pd.merge(df_ventas, df_vendedores, on='vendedor')
df_completo = pd.merge(df_ventas_info, df_productos, on='producto')

st.subheader(" DataFrame Fusionado")
st.dataframe(df_completo)


st.subheader(" Agregaciones")

col1, col2 = st.columns(2)

with col1:
    st.write(" Total de ventas por producto:")
    st.dataframe(df_ventas.groupby('producto')['total'].sum())

    st.write(" Total de productos vendidos por región:")
    st.dataframe(df_completo.groupby('region')['cantidad'].sum())

with col2:
    st.write(" Promedio de ventas por vendedor:")
    st.dataframe(df_ventas.groupby('vendedor')['total'].mean())

    st.write(" Total recaudado por región:")
    st.dataframe(df_completo.groupby('region')['total'].sum())

st.markdown("Codigo")

st.code("""
   df_ventas = pd.DataFrame({
    'id_venta': [1, 2, 3, 4, 5, 6],
    'producto': ['Manzanas', 'Bananas', 'Manzanas', 'Uvas', 'Bananas', 'Uvas'],
    'cantidad': [10, 5, 3, 8, 6, 4],
    'precio_unitario': [1200, 1500, 1200, 2000, 1500, 2000],
    'vendedor': ['Ana', 'Luis', 'Ana', 'Pedro', 'Luis', 'Pedro']
})
df_ventas['total'] = df_ventas['cantidad'] * df_ventas['precio_unitario']

df_vendedores = pd.DataFrame({
    'vendedor': ['Ana', 'Luis', 'Pedro'],
    'region': ['Centro', 'Norte', 'Sur'],
    'experiencia': [2, 4, 3]
})

df_productos = pd.DataFrame({
    'producto': ['Manzanas', 'Bananas', 'Uvas'],
    'categoria': ['Fruta', 'Fruta', 'Fruta'],
    'stock': [100, 80, 50]
})

st.subheader(" DataFrame de Ventas")
st.dataframe(df_ventas)

st.subheader(" DataFrame de Vendedores")
st.dataframe(df_vendedores)

st.subheader(" DataFrame de Productos")
st.dataframe(df_productos)


df_ventas_info = pd.merge(df_ventas, df_vendedores, on='vendedor')
df_completo = pd.merge(df_ventas_info, df_productos, on='producto')

st.subheader(" DataFrame Fusionado")
st.dataframe(df_completo)


st.subheader(" Agregaciones")

col1, col2 = st.columns(2)

with col1:
    st.write(" Total de ventas por producto:")
    st.dataframe(df_ventas.groupby('producto')['total'].sum())

    st.write(" Total de productos vendidos por región:")
    st.dataframe(df_completo.groupby('region')['cantidad'].sum())

with col2:
    st.write(" Promedio de ventas por vendedor:")
    st.dataframe(df_ventas.groupby('vendedor')['total'].mean())

    st.write(" Total recaudado por región:")
    st.dataframe(df_completo.groupby('region')['total'].sum())
""", language='python')