import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/datasets/exportacion_importacion_minera.csv', encoding="ISO-8859-1")

# df['Continente_exportacion'] = df['Continente_exportacion'].replace('Asiático','Asiatico')
# df['Continente_exportacion'] = df['Continente_exportacion'].replace('Oceanía','Oceania')

# df['Continente_importacion'] = df['Continente_importacion'].replace('Asiático','Asiatico')

# df['Pais_exportacion'] = df['Pais_exportacion'].replace('Bélgica','Belgica')
# df['Pais_exportacion'] = df['Pais_exportacion'].replace('Canadá','Canada')
# df['Pais_exportacion'] = df['Pais_exportacion'].replace('Japón','Japon')
# df['Pais_importacion'] = df['Pais_importacion'].replace('Canadá','Canada')


# Agrupar y graficar por país de exportación en dolares de exportación
# colores = ['#ed5e62']
# exportacion = df.groupby(
#     ["Pais_exportacion", "Exportacion_dolares"]).size().reset_index()
# e = exportacion.plot(x='Pais_exportacion', y='Exportacion_dolares', kind='bar', color=colores)

# for barra in e.containers:
#     e.bar_label(barra, label_type='edge')


# # Obtener la cantidad maxima de dolares en exportacion
# exportacion_maxima = df['Exportacion_dolares'].max()
# print(f"Cantidad máxima en millones de dolares en exportación: ${exportacion_maxima}")

# print(
#     f"Cantidad promedio en millones de dolares en exportación: ${promedio_exportacion}")


# # Agrupar y graficar por país de importacion en dolares de importacion
# colores = ['#eedc38']
# importacion = df.groupby(
#     ["Pais_importacion", "Importacion_dolares"]).size().reset_index()
# e = importacion.plot(x='Pais_importacion', y='Importacion_dolares', kind='bar', color=colores)

# for barra in e.containers:
#     e.bar_label(barra, label_type='edge')


# # Obtener la cantidad maxima de dolares en importacion
# importacion_maxima = df['Importacion_dolares'].max()
# print(f"Cantidad máxima en millones de dolares en importacion: ${importacion_maxima}")

# print(
#     f"Cantidad promedio en millones de dolares en exportación: ${promedio_importacion}")

plt.show()

# df.to_csv('exportacion_importacion_copia.csv',index=False)
