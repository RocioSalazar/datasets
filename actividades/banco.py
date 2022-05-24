import collections
import pandas as pd

# Previsualizar datos
df = pd.read_csv('datasets/datasets/banco.csv')

# Dimensión
print(df.ndim)

# Datos faltantes, Valores nulos
print(df.isnull())

# Tipo de datos que tiene el dataset en
# General y por columna
print(df.dtypes)
for column in df:
    print(df[column].dtypes)

# Usar .info
print(df.info())

# Usar .describe
print(df.describe())

# Datos duplicados en suma
print(df.duplicated().sum())