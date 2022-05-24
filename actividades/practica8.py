import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv('movie_metadata.csv')

# df.drop_duplicates(keep='last', subset=['director_name','actor_1_name','actor_3_name','title_year'])


# df['color'] = df['color'].fillna('Color')
# df['director_name'] = df['director_name'].fillna('S/N')
# df['num_critic_for_reviews'] = df['num_critic_for_reviews'].fillna('0')
# df['duration'] = df['duration'].fillna('Desconocida')
# df['director_facebook_likes'] = df['director_facebook_likes'].fillna('0')
# df['actor_3_facebook_likes'] = df['actor_3_facebook_likes'].fillna('0')
# df['actor_1_facebook_likes'] = df['actor_1_facebook_likes'].fillna('0')
# df['gross'] = df['gross'].fillna('0')
# df['genres'] = df['genres'].fillna('Desconocido')
# df['actor_1_name'] = df['actor_1_name'].fillna('S/N')
# df['movie_title'] = df['movie_title'].fillna('Desconocido')
# df['num_voted_users'] = df['num_voted_users'].fillna('0')
# df['cast_total_facebook_likes'] = df['cast_total_facebook_likes'].fillna('0')
# df['actor_3_name'] = df['actor_3_name'].fillna('S/N')
# df['facenumber_in_poster'] = df['facenumber_in_poster'].fillna('0')
# df['plot_keywords'] = df['plot_keywords'].fillna('NA')
# df['movie_imdb_link'] = df['movie_imdb_link'].fillna('http://www.imdb.com/title')
# df['num_user_for_reviews'] = df['num_user_for_reviews'].fillna('0')
# df['language'] = df['language'].fillna('Desconocido')
# df['country'] = df['country'].fillna('Desconocido')
# df['content_rating'] = df['content_rating'].fillna('Desconocido')
# df['budget'] = df['budget'].fillna('0')
# df['title_year'] = df['title_year'].fillna('Desconocido')
# df['actor_2_facebook_likes'] = df['actor_2_facebook_likes'].fillna('0')
# df['imdb_score'] = df['imdb_score'].fillna('0')
# df['aspect_ratio'] = df['aspect_ratio'].fillna('0')
# df['movie_facebook_likes'] = df['movie_facebook_likes'].fillna('0')


# df.to_csv('movie_metadatas_modify.csv', index=False)

df = pd.read_csv('movie_metadatas_modify.csv')


plt.figure(figsize=(100,100))


#Count de lenguaje y renderizarlo en tipo barra
t = df['language'].value_counts().plot(kind='bar')
plt.title('Lenguaje de peliculas')
plt.xlabel('Lenguajes')
plt.ylabel('Cantidad de lenguajes')

for barra in t.containers:
     t.bar_label(barra, label_type='edge')

plt.show()






