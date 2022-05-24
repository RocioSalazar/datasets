import pandas as pd
import matplotlib.pyplot as plt

#agregar el csv al dataframe
df = pd.read_csv('usuarios_completo.csv')

#selecciona  columnas para analisis
df = df[['company','car']]
#print(df.head())

#agrupar company y car del dataframe
group=df.groupby(["company","car"])
# print(group)

print(group.size().reset_index(name='counts'))

df['car'].value_counts().plot(kind = 'bar')
plt.show()
