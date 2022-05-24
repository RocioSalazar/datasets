import pandas as pd

# Para el archivo de usuario incompletos hacer lo siguiente:
# Company agregar Other
# Car agregar company
# Favorite_app agregar WhatsApp
# Avatar agregar default
# Activo agregar false
# is_admin agregar false
# Department agregar Other
# Gender agregar Other
# Nombre del archivo usuarios_completo
# Enviar los dos archivos(.csv y .py)

# empezar a leer el archivo csv
df = pd.read_csv('datasets/datasets/usuarios_incompleto.csv')

# rellenar las filas nulas de la columna lenguaje
df['company'] = df['company'].fillna('Other')
df['car'] = df['car'].fillna('Company')
df['favorite_app'] = df['favorite_app'].fillna('WhatsApp')
df['avatar'] = df['avatar'].fillna('https://robohash.org/default.png?size=50x50')
df['active'] = df['active'].fillna('false')
df['is_admin'] = df['is_admin'].fillna('false')
df['department'] = df['department'].fillna('Other')
df['gender'] = df['gender'].fillna('Other')

# guardar una copia con las columnas modificadas
df.to_csv('usuarios_completo.csv', index=False)