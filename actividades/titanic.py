import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('datasets/datasets/titanic.csv')

#Previsualiación
#print(df.head())


#Dimensión del df
#print(df.shape)

#Contabilizar cada columna
#print(df.count())

#Obtener los datos nulos de cada columna
# col_names= df.columns.tolist()

# for column in col_names:
#     print("Valores nulos en <" + column + ">: " + str(df[column].isnull().sum()))


#Reemplazar 

d = {'male': 'M', 'female':'F'}

#Utilizar un lambda para el reemplazo en una sola línea 
#df['Sex']= df['Sex'].apply(lambda x:d[x])

#Checar el cambio
#print(df['Sex'].head())

#Cruce de tablas
# ct = pd.crosstab(df['Survived'],df['Sex']).plot(kind='bar')

# plt.xlabel('Sobrevivió')
# plt.ylabel('Cantidad se sobrevivientes')

# for barra in ct.containers:
#     ct.bar_label(barra, label_type='edge')

# plt.show()

# Agrupar clase y sexo la suma de los sobrevivientes
pclass_survived = df.groupby(['Pclass','Sex'])['Survived'].sum()
print(pclass_survived)


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