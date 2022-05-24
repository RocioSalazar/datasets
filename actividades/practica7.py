import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/datasets/titanic.csv')

#Reemplazar 

d = {'male': 'M', 'female':'F'}

#Crear una figura de 15x15
plt.figure(figsize=(15,15))

#Generar 2 columnas para renderizar varias gráficas
plt.subplot2grid((2,3),(0,0))

#Count de sobrevivientes y renderizarlo en tipo barra
t = df['Survived'].value_counts().plot(kind='bar')
plt.title('Sobrevivieron - Cuenta total')
plt.xlabel('Sobrevivió')
plt.ylabel('Cantidad de Sobrevivientes')

for barra in t.containers:
     t.bar_label(barra, label_type='edge')

plt.show()