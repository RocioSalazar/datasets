import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('adult_data.csv')

df['gender'] = df['gender'].replace('Male', 'M')
df['gender'] = df['gender'].replace('Female', 'F')
df['income'] = df['income'].replace('<=50K', 49)
df['income'] = df['income'].replace('>50K', 51)

df.to_csv('adult_data_modify.csv', index=False)

df = pd.read_csv('adult_data_modify.csv')

plt.figure(figsize=(15,15))

plt.subplot2grid((2,3),(0,0))

t = df['income'].value_counts().plot(kind='bar')
plt.title('Cuenta total')
plt.xlabel('Income')
plt.ylabel('Cantidad de income')

for barra in t.containers:
     t.bar_label(barra, label_type='edge')

plt.show()
