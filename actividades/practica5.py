# publicidad javier
# mineria rocio


from numpy import product
import pandas as pd
import matplotlib.pyplot as plt

#agregar el csv al dataframe
df = pd.read_csv('users_modify.csv')

#selecciona  columnas para analisis
df = df[['gender','role']]
#print(df.head())

#agrupar gender y role del dataframe
group=df.groupby(["gender","role"])
# print(group)

# print(group.size().reset_index(name='counts'))

df['role'].value_counts().plot(kind = 'bar')
plt.show()
