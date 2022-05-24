import pandas as pd

# Para el archivo de usuario incompletos hacer lo siguiente:
# Company agregar Other
# Car agregar company
# Favorite_app agregar WhatsApp
# Avatar agregar default
# Activo agregar false
# is_admin agregar false
# Department agregar Other
# Gender agregar O
# Nombre del archivo usuarios_completo
# Enviar los dos archivos(.csv y .py)

# empezar a leer el archivo csv
df = pd.read_csv('usuarios_completo.csv')
# Eliminar los registros duplicados donde coincida lo que esta en apostrofe 
df.drop_duplicates(keep='last', subset=['first_name','last_name','email','company'])
# Imprimir los duplicados del CSV
print(df.duplicated().sum())

# rellenar las filas nulas de la columna lenguaje
# df['gender'] = df['gender'].replace('Other', 'O')
# df['active'] = df['active'].replace('false', False)
# df['is_admin'] = df['is_admin'].replace('false', False)

# guardar una copia con las columnas modificadas
df.to_csv('usuarios_completo.csv', index=False)