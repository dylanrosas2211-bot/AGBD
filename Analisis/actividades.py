#Trabajo Práctico: Filtros Avanzados y Reportes (con nuestro .csv ya cargado)

import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

#Importando csv

df=pd.read_csv("latin_music_features_dataset.csv")

print("OKEY! Archivo cargado correctamente")

#Ejercicio 1 

filas,columnas = df.shape

print(f"El dataframe tiene {filas} filas y {columnas} columnas")

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

df_seleccionado = df[filtro_avanzado][['genre', 'fragment_start_sec']]

print(df_seleccionado.head())

#Ejercicio 5

agrupado = (

    df.groupby("genre")["fragment_start_sec"]

    .sum()

    .sort_values(ascending=False)

)

print("Resumen agrupado:")

print(agrupado)

print()


#Ejercicio 6

UMBRAL = 1000

if (total := df_seleccionado["fragment_start_sec"].sum()) > UMBRAL:

    print(f"ALERTA: Prioridad Alta - Total = {total}")

else:

    print(f"Estado Normal - Total = {total}")

#ejercicio 7


plt.figure(figsize=(12, 6))

sns.barplot(

    data=df,

    x="genre",

    y="fragment_start_sec",

    estimator=sum,

    errorbar=None,

    palette="viridis"

)

plt.title("Comparacion por Categorias")

plt.xlabel("Categoria")

plt.ylabel("Total")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(

    "reporte_barras.png",

    dpi=300,

    bbox_inches="tight"

)

plt.close()

#ejercicio 8 

top_categorias = agrupado.nlargest(5)

plt.figure(figsize=(8, 8))

plt.pie(

    top_categorias,

    labels=top_categorias.index,

    autopct="%1.1f%%",

    wedgeprops={

        "edgecolor": "white",

        "linewidth": 2

    }

)

plt.title("Distribucion de Categorias")

plt.savefig(

    "reporte_torta.png",

    dpi=300,

    bbox_inches="tight"

)

plt.close()

print("\nReportes generados correctamente:")

print("- reporte_barras.png")

print("- reporte_torta.png")

#Ejercicio 9

condicion_extra = df["fragment_start_sec"] > 100

resultado = df.loc[

    filtro_avanzado & condicion_extra,

    ["genre", "fragment_start_sec", "artist"]

]

print(resultado)

print(f"\nFilas seleccionadas: {len(resultado)}")

