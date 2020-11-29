import pandas as pd
import numpy as np

minimum_votes = 0
mean_rating = 0


def imdb_weighted_rating(df, m=minimum_votes, c=mean_rating):
    v = df['vote_count']
    r = df['vote_average']

    return ((v / v + m) * r) + ((m / v + m) * c)


def main():
    credits_df = pd.read_csv('../../data/tmdb-5000/tmdb_5000_credits.csv')
    movies_df = pd.read_csv('../../data/tmdb-5000/tmdb_5000_movies.csv')

    # These are the columns present in the credits csv file,
    # rename movie_id to id to match with the second dataframe
    credits_df.columns = ['id', 'title', 'cast', 'crew']

    # Merge these to one combined dataframe
    movies_df = movies_df.merge(credits_df, on='id')

    # Mean rating of all movies
    mean_rating = movies_df['vote_average'].mean()

    # Minimum votes should be at least  75th percentile
    minimum_votes = movies_df['vote_count'].quantile(0.75)

    top_movies = movies_df.copy().loc[movies_df['vote_count'] >= minimum_votes]

    # axis=1, use the index as the dataframe's column
    top_movies['score'] = top_movies.apply(imdb_weighted_rating, axis=1)

    top_movies = top_movies.sort_values('score', ascending=False)

    print("The list of top 10 movies are:"+"\n"+str(top_movies[['original_title', 'score']].head(10)))


if __name__ == "__main__":
    main()
