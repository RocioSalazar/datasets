import pandas as pd
import matplotlib.pyplot as plt

# crosstab
# Agregar el archivo para analisis con pandas
df = pd.read_csv('users_modify.csv')
# Seleccionar las columnas a procesar
df = df[['gender', 'role']]
# Crear un cruce entre columnas y filas
ct = pd.crosstab(df['gender'], df['role']).plot(kind='bar')
plt.title('Grafica para cruce de genero y rol')
# x = plt.subplot()
# x.set_xlabel('Genero')
# x.set_ylabel('Cantidad de roles')
plt.legend(loc="upper right")
# 'best (la mejor posición según python)', 'upper right (arriba a la derecha)', 'upper left (arriba a la izquierda)', 'lower left (abajo a la izquierda)', 'lower right (abajo a la derecha)', 'right (derecha)', 'center left (centrado a la izquierda)', 'center right (centrado a la derecha)', 'lower center (centrado abajo)', 'upper center (centrado arriba)', 'center (centrado)'
plt.xlabel("Genero")
plt.ylabel("rol")

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')
plt.show()
