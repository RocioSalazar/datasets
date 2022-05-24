import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/datasets/adult_data.csv')

df['gender'] = df['gender'].replace('Male', 'M')
df['gender'] = df['gender'].replace('Female', 'F')
df['income'] = df['income'].replace('<=50K', 49)
df['income'] = df['income'].replace('>50K', 51)

#Crear una figura de 15x15
plt.figure(figsize=(15,15))

#Generar 2 columnas para renderizar varias gráficas
plt.subplot2grid((2,3),(0,0))

#Count de sobrevivientes y renderizarlo en tipo barra
t = df['income'].value_counts().plot(kind='bar')
plt.title('Ingresos total')
plt.xlabel('Ingresos')
plt.ylabel('Cantidad de ingresos')

for barra in t.containers:
     t.bar_label(barra, label_type='edge')

plt.show()

df.to_csv('adult_modify.csv', index=False)
