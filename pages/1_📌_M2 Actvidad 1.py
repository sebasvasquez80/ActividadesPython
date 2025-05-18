import streamlit as st
import pandas as pd
import sqlite3
import numpy as np


# Configuración de la página
st.set_page_config(   
    page_icon="📌",
    layout="wide"
)

st.title("Momento 2 - Actividad 1")

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

st.header("Solución actividad 1")

soccer = { "Club" : ["FC Barcelona", "Real Madrid CF", "Atletico Madrid", "Valencia", "Sevilla"],
          "Ganados": ["10","8","6","4","2"],
          "Empatados": ["0","1","2","3","5"],
          "Perdidos": ["0","1","2","3","3"],
          "Puntos":["30","25","20","15","10"],}

table = pd.DataFrame(soccer)
table.index = range(1, len(table) + 1)

st.subheader ("Creación de DataFrame con diccionario")
st.code("""
    soccer = { "Club" : ["FC Barcelona", "Real Madrid CF", "Atletico Madrid", "Valencia", "Sevilla"],
          "Ganados": ["10","8","6","4","2"],
          "Empatados": ["0","1","2","3","5"],
          "Perdidos": ["0","1","2","3","3"],
          "Puntos":["30","25","20","15","10"],}

table = pd.DataFrame(soccer)
table.index = range(1, len(table) + 1)

st.dataframe(table)
""", language='python')

st.dataframe(table)

st.subheader ("Creación de DataFrame con lista de diccionarios")

st.code("""
    ciudades = [
    {"nombre": "Bogotá", "población": 7743955, "país": "Colombia"},
    {"nombre": "Ciudad de México", "población": 9209944, "país": "México"},
    {"nombre": "Madrid", "población": 3223334, "país": "España"},
    {"nombre": "Buenos Aires", "población": 2890151, "país": "Argentina"}
]

df_ciudades = pd.DataFrame(ciudades)

st.dataframe(df_ciudades)
""", language='python')

ciudades = [
    {"nombre": "Bogotá", "población": 7743955, "país": "Colombia"},
    {"nombre": "Ciudad de México", "población": 9209944, "país": "México"},
    {"nombre": "Madrid", "población": 3223334, "país": "España"},
    {"nombre": "Buenos Aires", "población": 2890151, "país": "Argentina"}
]

df_ciudades = pd.DataFrame(ciudades)

st.dataframe(df_ciudades)

st.subheader ("Creación de DataFrame con lista de listas")

st.code("""
    productos = [
    ["PC", 3500.00, 10],
    ["Mouse", 50.00, 150],
    ["Teclado", 120.00, 75],
    ["Monitor", 800.00, 25]
]

columnas = ["Producto", "Precio", "Stock"]

df_productos = pd.DataFrame(productos, columns=columnas)

st.dataframe(df_productos)
""", language='python')

productos = [
    ["PC", 3500.00, 10],
    ["Mouse", 50.00, 150],
    ["Teclado", 120.00, 75],
    ["Monitor", 800.00, 25]
]

columnas = ["Producto", "Precio", "Stock"]

df_productos = pd.DataFrame(productos, columns=columnas)

st.dataframe(df_productos)

st.subheader ("Creación de DataFrame con Series")

st.code("""
    nombres = pd.Series(["Ana", "Luis", "María", "Carlos"])
    edades = pd.Series([28, 34, 22, 45])
    ciudades = pd.Series(["Bogotá", "Medellín", "Cali", "Barranquilla"])

datos = {
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
}

df_personas = pd.DataFrame(datos)

st.dataframe(df_personas)
""", language='python')

nombres = pd.Series(["Ana", "Luis", "María", "Carlos"])
edades = pd.Series([28, 34, 22, 45])
ciudades = pd.Series(["Bogotá", "Medellín", "Cali", "Barranquilla"])

datos = {
    "Nombre": nombres,
    "Edad": edades,
    "Ciudad": ciudades
}

df_personas = pd.DataFrame(datos)

st.dataframe(df_personas)

st.subheader ("Creación de DataFrame con Archivo CSV")

st.code("""
    df_csv = pd.read_csv("assets/datos.csv")

st.title("Datos desde CSV")
st.dataframe(df_csv)
""", language='python')

df_csv = pd.read_csv("assets/datos.csv")

st.dataframe(df_csv)

st.subheader ("Creación de DataFrame con Archivo Excel")

st.code("""
    df_excel = pd.read_excel("assets/datos.xlsx", engine="openpyxl")

st.dataframe(df_excel)
""", language='python')

df_excel = pd.read_excel("assets/datos.xlsx", engine="openpyxl")

st.dataframe(df_excel)

st.subheader ("Creación de DataFrame con Archivo JSON")

st.code("""
    df_json = pd.read_json("assets/datos.json")

st.dataframe(df_json)
""", language='python')

df_json = pd.read_json("assets/datos.json")

st.dataframe(df_json)

st.subheader ("Creación de DataFrame con URL")

st.code("""
    df_url = pd.read_csv("./assets/student_habits_performance.csv")

st.dataframe(df_url)
st.dataframe(df_url.head(10))
""", language='python')

df_url = pd.read_csv("./assets/student_habits_performance.csv")

st.dataframe(df_url.head(10))

st.subheader ("Creación de DataFrame con SQLite")

st.code("""
    conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        calificacion REAL
    )
''')

cursor.execute("SELECT COUNT(*) FROM estudiantes")
if cursor.fetchone()[0] == 0:
    datos = [
        ('Juan Pérez', 4.5),
        ('María Gómez', 3.8),
        ('Carlos Díaz', 4.2)
    ]
    cursor.executemany("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", datos)
    conexion.commit()

df = pd.read_sql("SELECT * FROM estudiantes", conexion)

st.dataframe(df)

conexion.close()
""", language='python')

conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS estudiantes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        calificacion REAL
    )
''')

cursor.execute("SELECT COUNT(*) FROM estudiantes")
if cursor.fetchone()[0] == 0:
    datos = [
        ('Juan Pérez', 4.5),
        ('María Gómez', 3.8),
        ('Carlos Díaz', 4.2)
    ]
    cursor.executemany("INSERT INTO estudiantes (nombre, calificacion) VALUES (?, ?)", datos)
    conexion.commit()

df = pd.read_sql("SELECT * FROM estudiantes", conexion)

st.dataframe(df)

conexion.close()

st.subheader ("Creación de DataFrame con NumPy")

st.code("""
    array = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [75, 80, 70]
])

columnas = ["Matemáticas", "Ciencias", "Inglés"]
df_numpy = pd.DataFrame(array, columns=columnas)

st.dataframe(df_numpy)
""", language='python')

array = np.array([
    [85, 90, 78],
    [92, 88, 95],
    [75, 80, 70]
])

columnas = ["Matemáticas", "Ciencias", "Inglés"]
df_numpy = pd.DataFrame(array, columns=columnas)

st.dataframe(df_numpy)