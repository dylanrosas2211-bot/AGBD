import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#Importando csv
df=pd.read_csv("latin_music_features_dataset.csv")

print("OKEY! Archivo cargado correctamente")

print(df.head())

#filas,columnas = df.shape
#print(f"El dataframe tiene {filas} filas y {columnas} columnas")

#total_anios = df['year'].count() #referencio columna de mi datafram
#print(f"Cantidad de filas con año valido: {total_anios}")

print ("----Analisis Avanzado de Datos----")

filtro_avanzado=df['genre'].str.startswith('Regga', na=False)
df_filtrado=df[filtro_avanzado]

total_registros = df_filtrado['bpm'].count()
#print(f"Cantidad de envios de tecnologia 'Regga': {total_registros}")

suma_dinero = df_filtrado['bpm'].sum()
#print(f"Valor total de este comercio: USD {suma_dinero:.2f} millones")

print("--Reporte Automatizado--")
print(f"Monto total. USD {suma_dinero:.2f} millones")

if Default_limite_alto:=(suma_dinero>500):
    print ("Alerta: El volumen de Mercado es Critico y de alta prioridad.")
    print("Requiere revision inmediata")

elif suma_dinero > 200:
    print("Aviso: volumen mercado moderado/alto")
    print("Monitorear comportamiento proximo trimestre")

else:
    print("Estado: volumen de mercado bajo o dentro del parametro")
    print("No se requiere accion adicional")

#---------------------------------------------
#  GRAFICO 1: Grafico de Barras (con Seaborn) 
#---------------------------------------------

print("\n Generando Grafico de Barras ")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(9,5))

sns.barplot(
    data=df,
    x="genre",
    y="bpm",
    estimator=sum,
    errorbar=None,
    palette="viridis",#magma, Blue_h
)

plt.title(
    "Distribucion economica de tecnologia avanzada", fontsize=14
)
plt.xlabel("Tipo de hardware", fontsize=11)
plt.ylabel("Total (millones USD)", fontsize=11)

plt.tight_layout()
plt.savefig("grafico_barras.png", dpi=300)
plt.close()
print("Grafico de barras guardado exitosamente.")

#--------------------------------------------------
# GRAFICO de Torta
#--------------------------------------------------
print("\nGenerando gráfico de torta...")

datos_torta = (
    df.groupby("genre")["fragment_start_sec"]
    .sum()
    .nlargest(5)
)

plt.figure(figsize=(7, 7))

plt.pie(
    datos_torta,
    labels=datos_torta.index,
    autopct="%1.1f%%",
    colors=sns.color_palette("Set2")[0:5],
    startangle=140,
    wedgeprops={
        "edgecolor": "white",
        "linewidth": 2
    }
)

plt.title("Distribución de las categorías")
plt.savefig("grafico_torta.png", dpi=300)
plt.close()

print("Gráfico de torta guardado exitosamente.")