import pandas as pd
import matplotlib.pyplot as plt

#crear tablas sencillas con count
df = pd.read_csv('usuarios_completo.csv')

#selecciona solamente las columnas gender y favorite_app
df = df[['gender','favorite_app']]
# print(df.head())

df['gender'].value_counts().plot(kind = 'pie')
plt.show()

df['favorite_app'].value_counts().plot(kind = 'barh')
plt.show()


# df.plot(kind='scatter',x = 'first_name', y = 'car' )
# plt.show()