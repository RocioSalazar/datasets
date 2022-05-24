import pandas as pd
import matplotlib.pyplot as plt

#empezar a leer el archivo csv
df = pd.read_csv('datasets/datasets/users_data.csv')


print(df.head())

#imprimir los nulos de dataframe
print(df.isnull())

#rellenar las filas nulas de la columna lenguaje
df['lenguage'] = df['lenguage'].fillna('Other')

#guardar una copia con las columnas modificadas
df.to_csv('users_modify.csv', index=False)