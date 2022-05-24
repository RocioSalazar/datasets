import pandas as pd
import matplotlib.pyplot as plt

# # leer el archivo csv
# df = pd.read_csv('datasets/datasets/movie_metadata.csv')

# # rellenar las filas nulas de la columna
# df['color'] = df['color'].fillna('Color')
# df['director_name'] = df['director_name'].fillna('Desconocido')
# df['num_critic_for_reviews'] = df['num_critic_for_reviews'].fillna('0')
# df['duration'] = df['duration'].fillna('0')
# df['director_facebook_likes'] = df['director_facebook_likes'].fillna('0')
# df['actor_3_facebook_likes'] = df['actor_3_facebook_likes'].fillna('0')
# df['actor_1_facebook_likes'] = df['actor_1_facebook_likes'].fillna('0')
# df['gross'] = df['gross'].fillna('0')
# df['genres'] = df['genres'].fillna('Desconocido')
# df['actor_1_name'] = df['actor_1_name'].fillna('Desconocido')
# df['movie_title'] = df['movie_title'].fillna('Desconocido')
# df['num_voted_users'] = df['num_voted_users'].fillna('0')
# df['cast_total_facebook_likes'] = df['cast_total_facebook_likes'].fillna('0')
# df['actor_3_name'] = df['actor_3_name'].fillna('Desconocido')
# df['facenumber_in_poster'] = df['facenumber_in_poster'].fillna('0')
# df['plot_keywords'] = df['plot_keywords'].fillna('Sin clave')
# df['movie_imdb_link'] = df['movie_imdb_link'].fillna('http://www.imdb.com/')
# df['num_user_for_reviews'] = df['num_user_for_reviews'].fillna('0')
# df['language'] = df['language'].fillna('Subtitulada')
# df['country'] = df['country'].fillna('Otro')
# df['content_rating'] = df['content_rating'].fillna('S/N')
# df['budget'] = df['budget'].fillna('0')
# df['title_year'] = df['title_year'].fillna('Indefinido')
# df['actor_2_facebook_likes'] = df['actor_2_facebook_likes'].fillna('0')
# df['imdb_score'] = df['imdb_score'].fillna('0')
# df['aspect_ratio'] = df['aspect_ratio'].fillna('0')
# df['movie_facebook_likes'] = df['movie_facebook_likes'].fillna('0')

# # Eliminar los registros duplicados donde coincida lo que esta en apostrofe 
# df.drop_duplicates(keep='last', subset=['color','director_name','num_critic_for_reviews','duration'])

# # guardar una copia con las columnas modificadas
# df.to_csv('movie_modify.csv', index=False)


df = pd.read_csv('datasets/actividades/movie_modify.csv')


plt.figure(figsize=(50,50))


#Count de lenguaje y renderizarlo en tipo barra
t = df['actor_1_name'].value_counts().plot(kind='bar')
plt.title('Actores participantes')
plt.xlabel('Actores')
plt.ylabel('Cantidad de actores')

for barra in t.containers:
     t.bar_label(barra, label_type='edge')

plt.show()

