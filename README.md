# movie-recommendation-system
CS6550 - Introduction to Information Retrieval project

Term: Fall, 2020

A movie recommention system using information retrieval techniques.

Authors
* [Abishek Krishnan](https://github.com/github4ak)
* [Sai Vamshi Dobbali](https://github.com/saivamshidobbali)

Overview
--------


Setup steps
-----------
- Download Numpy & Pandas
```
$ sudo apt-get install python-pip
$ sudo pip install numpy
$ sudo pip install pandas
```

- Download Scikit-Learn <br/>
`$ pip3 install -U scikit-learn`

Run steps
---------
- To run statistical filtering,
  - From /code/Statistical filtering/ <br/>
  `python3 topMovies.py`

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
