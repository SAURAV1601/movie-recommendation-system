# movie-recommendation-system
CS6550 - Introduction to Information Retrieval project

Term: Fall, 2020

A movie recommention system using information retrieval techniques.

Authors
* [Abishek Krishnan](https://github.com/github4ak)
* [Sai Vamshi Dobbali](https://github.com/saivamshidobbali)

Overview
--------
This project contains i) Statistical Filtering and ii) Content based filtering to recommend top movies.

Setup steps
-----------
- Download Numpy & Pandas
```
$ sudo apt-get install python-pip
$ sudo pip install numpy
$ sudo pip install pandas
```

- Download Scikit-Learn <br/>
```
$ pip3 install -U scikit-learn`
```

Run steps
---------
- To run statistical filtering,
  - From /code/Statistical filtering/ <br/>
  `python3 topMovies.py`

- To run content based filtering,
  - From /code/Content based filtering/ <br/>
  `python3 topSimilarContentMovies.py`

Results
-------

For our statistical filtering, we got the top 10 movies in TMDB dataset as,

```
The list of top 10 movies are:
                original_title  score
1881  The Shawshank Redemption    8.5
3337             The Godfather    8.4
2294                  千と千尋の神隠し    8.3
3865                  Whiplash    8.3
2731    The Godfather: Part II    8.3
3232              Pulp Fiction    8.3
1818          Schindler's List    8.3
662                 Fight Club    8.3
2170                    Psycho    8.2
1847                GoodFellas    8.2
```

For our content based filtering, finding similarity between movie's overview, we got the top 10 movies similar to 'The Shawshank Redemption' as,
```
Movies similar to The Shawshank Redemption are:
4531               Civil Brand
3785                    Prison
609                Escape Plan
2868                  Fortress
4727              Penitentiary
1779    The 40 Year Old Virgin
2667          Fatal Attraction
3871         A Christmas Story
434           The Longest Yard
42                 Toy Story 3
Name: title, dtype: object
```

References
----------
Our methods are based on [Hands-On Recommendation Systems with Python](https://www.oreilly.com/library/view/hands-on-recommendation-systems/9781788993753/) by [Rounak Banik](https://github.com/rounakbanik)
