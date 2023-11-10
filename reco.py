import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset
data = {
    'Movie': ['Movie1', 'Movie2', 'Movie3', 'Movie4', 'Movie5'],
    'Genre': ['Action', 'Comedy', 'Action|Comedy', 'Drama', 'Drama|Romance']
}

movies_df = pd.DataFrame(data)

# Function to create a bag of words representation for each movie
def create_bag_of_words(data):
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(data['Genre'])
    return tfidf_matrix

# Function to get movie recommendations based on similarity
def get_recommendations(movie_title, data, tfidf_matrix):
    idx = data[data['Movie'] == movie_title].index[0]
    cosine_similarities = linear_kernel(tfidf_matrix[idx], tfidf_matrix).flatten()
    related_movies = list(enumerate(cosine_similarities, start=1))
    related_movies = sorted(related_movies, key=lambda x: x[1], reverse=True)[1:]

    recommendations = []
    for movie_id, similarity in related_movies[:5]:
        recommendations.append(data.loc[movie_id - 1, 'Movie'])

    return recommendations

# Create bag of words representation
tfidf_matrix = create_bag_of_words(movies_df)

# Get recommendations for a movie
movie_title_to_recommend = 'Movie1'
recommendations = get_recommendations(movie_title_to_recommend, movies_df, tfidf_matrix)

print(f"Recommended movies for {movie_title_to_recommend}: {recommendations}")
