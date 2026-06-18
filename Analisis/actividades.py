#Trabajo Práctico: Filtros Avanzados y Reportes (con nuestro .csv ya cargado)

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Importando csv
df=pd.read_csv("latin_music_features_dataset.csv")

print("OKEY! Archivo cargado correctamente")

#Ejercicio 1 

#filas,columnas = df.shape
#print(f"El dataframe tiene {filas} filas y {columnas} columnas")

#Ejercicio 2

#filtro_avanzado = df['genre'] == 'Bachata'
#df_filtrado = df[filtro_avanzado]


#Bachata
#filtro_avanzado=df['genre'].str.startswith('Regga', na=False)
#df_filtrado=df[filtro_avanzado]

#Ejercicio 3

filtro_avanzado=df['genre'].str.contains('gae', na=False)
print(filtro_avanzado)

#Ejercicio 4
#fragment_start_sec
#df_seleccionado = df[['genre', 'fragment_start_sec']]
#print(df_seleccionado.head())

#Ejercicio 5

resumen = df.groupby('genre')['fragment_start_sec'].sum()
print(resumen)