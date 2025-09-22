import pandas as pd
import matplotlib.pyplot as plt

df_netflix = pd.read_csv("netflix_titles.csv")

print(df_netflix.info())

# Visualisation of the distribution of ratings
plt.figure(figsize=(10,6))
df_netflix['rating'].value_counts().plot(kind='bar', color='skyblue')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.xticks(rotation=-45)
plt.show()

# Distribution between Movie and TV Show
plt.figure(figsize=(8,6))
df_netflix['type'].value_counts().plot(kind='bar', color=['orange', 'green'])
plt.title('Distribution of Content Type')
plt.xlabel('Content Type (Movie or TV Show)')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Analyze the number of movies and TV shows released each year
df_netflix['release_year'] = pd.to_numeric(df_netflix['release_year'], errors='coerce')

release_counts = df_netflix.groupby('release_year').size()

plt.figure(figsize=(12,6))
release_counts.plot(kind='line', color='purple')
plt.title('Number of Netflix Releases Over Time')
plt.xlabel('Release Year')
plt.ylabel('Number of Releases')
plt.grid()
plt.show()

# Count the top 10 actors
plt.figure(figsize=(12,6))
top_actors = df_netflix['cast'].dropna().str.split(', ').explode().value_counts().head(10)
bars = top_actors.plot(kind='bar', color='teal')
plt.title('Top 10 Actors')
plt.xlabel('Actor')
plt.ylabel('Number of Movies/TV Shows')
plt.xticks(rotation=90)
plt.show()

# Summary of Movies vs TV Shows
total_movies = df_netflix[df_netflix['type'] == 'Movie'].shape[0]
total_tv_shows = df_netflix[df_netflix['type'] == 'TV Show'].shape[0]

total_content = len(df_netflix)

movies_percentage = (total_movies / total_content) * 100
tv_shows_percentage = (total_tv_shows / total_content) * 100

summary_table = pd.DataFrame({
    'Type': ['Movies', 'TV Shows', 'Total'],
    'Count': [total_movies, total_tv_shows, total_content],
    'Percentage': [f"{movies_percentage:.2f}%", f"{tv_shows_percentage:.2f}%", "100%"]
})

print(summary_table)
