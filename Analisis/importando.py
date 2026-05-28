import pandas as pd

#Importando csv
df=pd.read_csv("latin_music_features_dataset.csv")

print("OKEY! Archivo cargado correctamente")

print(df.head())

#filas,columnas = df.shape
#print(f"El dataframe tiene {filas} filas y {columnas} columnas")

#total_anios = df['year'].count() #referencio columna de mi datafram
#print(f"Cantidad de filas con año valido: {total_anios}")
