# Movie-Finder
Searches for a random movie with adjustable search settings and outputs information about the movie and a link to its YouTube trailer.

To use the program, you must get your own free IMDb api key that is then inserted into line 6 of APIConnector.py.

Search settings can be adjusted by changing line 6 of main.py

For variables that end with the suffix "MinMax", they must be written in the form '(lower bound),(upper bound)', where lowerbound and upper bound are each optional.
For example "5,7.1" or ",8.7" or "8.8,"
