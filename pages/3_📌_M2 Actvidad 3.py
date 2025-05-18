import streamlit as st
import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, date


# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 3")

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

st.subheader("Actividad 1: Practica de filtrado en Pandas (Google Colab)")

st.markdown("""
https://colab.research.google.com/drive/1v5dOffbnKGwVEFzuQ9EiR3kzeVsNuq_t?usp=sharing.
""")

st.subheader("Actividad 2: Desarrollar una aplicación de filtros dinámicos en Streamlit.")

fake = Faker('es_CO')
np.random.seed(123)
random.seed(123)
fake.seed_instance(123)

n = 50
data = {
    'id': range(1, n + 1),
    'nombre_completo': [fake.name() for _ in range(n)],
    'edad': np.random.randint(15, 76, n),
    'region': random.choices(
        ['Caribe', 'Andina', 'Pacífica', 'Orinoquía', 'Amazonía'],
        weights=[0.3, 0.4, 0.15, 0.1, 0.05],
        k=n
    ),
    'municipio': random.choices(
        [
            'Barranquilla', 'Santa Marta', 'Cartagena',
            'Bogotá', 'Medellín', 'Tunja', 'Manizales',
            'Cali', 'Quibdó', 'Buenaventura',
            'Villavicencio', 'Yopal',
            'Leticia', 'Puerto Inírida'
        ],
        k=n
    ),
    'ingreso_mensual': np.random.randint(800000, 12000001, n),
    'ocupacion': random.choices(
        [
            'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
            'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
            'Emprendedor', 'Obrero'
        ],
        k=n
    ),
    'tipo_vivienda': random.choices(['Propia', 'Arrendada', 'Familiar'], k=n),
    'fecha_nacimiento': [
        fake.date_of_birth(minimum_age=15, maximum_age=75) for _ in range(n)
    ],
    'acceso_internet': random.choices([True, False], weights=[0.7, 0.3], k=n)
}
df_nuevo = pd.DataFrame(data)
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

df_filtrado = df_nuevo.copy()

st.sidebar.header("Filtros")

if st.sidebar.checkbox("Filtrar por rango de edad"):
    min_edad, max_edad = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (18, 60))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

if st.sidebar.checkbox("Filtrar por municipios"):
    municipios = [
        'Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja',
        'Manizales', 'Cali', 'Quibdó', 'Buenaventura',
        'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'
    ]
    municipios_seleccionados = st.sidebar.multiselect("Selecciona municipios", municipios)
    if municipios_seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios_seleccionados)]

if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_minimo = st.sidebar.slider("Ingreso mensual mínimo", 800000, 12000000, 2000000, step=100000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_minimo]

if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = [
        'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
        'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
        'Emprendedor', 'Obrero'
    ]
    ocupaciones_seleccionadas = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones)
    if ocupaciones_seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones_seleccionadas)]

if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Ingresa texto a buscar en el nombre")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    año = st.sidebar.selectbox("Selecciona el año", list(range(1949, 2010)))
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == año]

if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])
    df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == (acceso == "Sí")]

if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", date(1950, 1, 1))
    fecha_fin = st.sidebar.date_input("Fecha de fin", date(2009, 12, 31))
    if fecha_inicio <= fecha_fin:
        fecha_inicio_dt = pd.to_datetime(fecha_inicio)
        fecha_fin_dt = pd.to_datetime(fecha_fin)
        df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(fecha_inicio_dt, fecha_fin_dt)]

st.subheader("Resultados del filtro")
st.write(f"Número de registros encontrados: {len(df_filtrado)}")
st.dataframe(df_filtrado)

st.markdown("Codigo")

st.code("""
    df_nuevo = pd.DataFrame(data)
df_nuevo.loc[3:5, 'ingreso_mensual'] = np.nan
df_nuevo.loc[15:17, 'ocupacion'] = np.nan
df_nuevo['fecha_nacimiento'] = pd.to_datetime(df_nuevo['fecha_nacimiento'])

df_filtrado = df_nuevo.copy()

st.sidebar.header("Filtros")

if st.sidebar.checkbox("Filtrar por rango de edad"):
    min_edad, max_edad = st.sidebar.slider("Selecciona el rango de edad", 15, 75, (18, 60))
    df_filtrado = df_filtrado[df_filtrado['edad'].between(min_edad, max_edad)]

if st.sidebar.checkbox("Filtrar por municipios"):
    municipios = [
        'Barranquilla', 'Santa Marta', 'Cartagena', 'Bogotá', 'Medellín', 'Tunja',
        'Manizales', 'Cali', 'Quibdó', 'Buenaventura',
        'Villavicencio', 'Yopal', 'Leticia', 'Puerto Inírida'
    ]
    municipios_seleccionados = st.sidebar.multiselect("Selecciona municipios", municipios)
    if municipios_seleccionados:
        df_filtrado = df_filtrado[df_filtrado['municipio'].isin(municipios_seleccionados)]

if st.sidebar.checkbox("Filtrar por ingreso mensual mínimo"):
    ingreso_minimo = st.sidebar.slider("Ingreso mensual mínimo", 800000, 12000000, 2000000, step=100000)
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'] > ingreso_minimo]

if st.sidebar.checkbox("Filtrar por ocupación"):
    ocupaciones = [
        'Estudiante', 'Docente', 'Comerciante', 'Agricultor',
        'Ingeniero', 'Médico', 'Desempleado', 'Pensionado',
        'Emprendedor', 'Obrero'
    ]
    ocupaciones_seleccionadas = st.sidebar.multiselect("Selecciona ocupaciones", ocupaciones)
    if ocupaciones_seleccionadas:
        df_filtrado = df_filtrado[df_filtrado['ocupacion'].isin(ocupaciones_seleccionadas)]

if st.sidebar.checkbox("Filtrar personas sin vivienda propia"):
    df_filtrado = df_filtrado[~(df_filtrado['tipo_vivienda'] == 'Propia')]

if st.sidebar.checkbox("Filtrar por nombre"):
    texto = st.sidebar.text_input("Ingresa texto a buscar en el nombre")
    if texto:
        df_filtrado = df_filtrado[df_filtrado['nombre_completo'].str.contains(texto, case=False, na=False)]

if st.sidebar.checkbox("Filtrar por año de nacimiento"):
    año = st.sidebar.selectbox("Selecciona el año", list(range(1949, 2010)))
    df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].dt.year == año]

if st.sidebar.checkbox("Filtrar por acceso a internet"):
    acceso = st.sidebar.radio("¿Tiene acceso a internet?", ["Sí", "No"])
    df_filtrado = df_filtrado[df_filtrado['acceso_internet'] == (acceso == "Sí")]

if st.sidebar.checkbox("Filtrar por ingresos nulos"):
    df_filtrado = df_filtrado[df_filtrado['ingreso_mensual'].isnull()]

if st.sidebar.checkbox("Filtrar por rango de fechas de nacimiento"):
    fecha_inicio = st.sidebar.date_input("Fecha de inicio", date(1950, 1, 1))
    fecha_fin = st.sidebar.date_input("Fecha de fin", date(2009, 12, 31))
    if fecha_inicio <= fecha_fin:
        df_filtrado = df_filtrado[df_filtrado['fecha_nacimiento'].between(fecha_inicio, fecha_fin)]

st.subheader("Resultados del filtro")
st.write(f"Número de registros encontrados: {len(df_filtrado)}")
st.dataframe(df_filtrado)
""", language='python')