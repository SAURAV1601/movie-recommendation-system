import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def get_similar_movies(movie_df, title, indices, cos_sim):
    curr_index = indices[title]

    sim_scores = list(enumerate(cos_sim[curr_index]))

    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return movie_df['title'].iloc[movie_indices]


def main():
    movies_df = pd.read_csv('../../data/tmdb-5000/tmdb_5000_movies.csv')

    # Remove stop words from the 'overview'
    tf_idf_vectorizer_object = TfidfVectorizer(stop_words='english')

    # Replace NaN string with empty string
    movies_df['overview'] = movies_df['overview'].fillna('')

    # Construct the TF_IDF matrix
    tf_idf_matrix = tf_idf_vectorizer_object.fit_transform(movies_df['overview'])

    # Calculate the cosine similarity
    cos_sim = cosine_similarity(tf_idf_matrix, tf_idf_matrix)

    # Construct a map from title to index
    title_to_index = pd.Series(movies_df.index, index=movies_df['title']).drop_duplicates()

    search_movie_title = 'The Shawshank Redemption'

    print('Movies similar to ' + search_movie_title + ' are:')
    print(get_similar_movies(movies_df, search_movie_title, title_to_index, cos_sim))


if __name__ == "__main__":
    main()
