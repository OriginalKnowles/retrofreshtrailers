# I decided to learn how to parse in the information from a csv file as
# creating a new class by hand for each one was becoming tedious!

import csv
import fresh_tomatoes
from movie.py import media


# This reads in the Retro Fresh movie trailers main list, creates and object
# for each movie then provides a list ready to be served as content in the
# HTML file
def read_in_csv(csv_file):
    with open(csv_file, 'rb') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',', quotechar='"')

        # Create empty lists to store the column values
        movie_titles = []
        movie_synopsis = []
        movie_posters = []
        movie_trailers = []
        movie_release_date = []
        movie_raking = []

        # Create empty movie objects list to store all the movie objects
        movie_objects = []

        # Iterate through the csv rows and add the column values to
        # specified list
        for row in csv_reader:
            movie_titles.append(row[0])
            movie_synopsis.append(row[1])
            movie_posters.append(row[2])
            movie_trailers.append(row[3])
            movie_release_date.append(row[4])
            movie_raking.append(row[5])

        # counter = len(movie_titles)
        # counter = int(counter)
        # print(counter)
        # Create movie objects for each movie parsing in the values
        # stored in the above lists.
        for i in range(0, 13):
            if i > 0:
                temp = media.Movie(movie_titles[i], movie_synopsis[i],
                                   movie_posters[i], movie_trailers[i],
                                   movie_release_date[i], movie_raking[i])
                movie_objects.append(temp)
        # Test 'print' function
        print(len(movie_objects))

    # Returns all the created movie objects in one list
    return movie_objects


# Assigns the returned 'movie_objects' list from the 'read_in_csv' function
# to a variable
movies = read_in_csv("../data/RetroFreshMovieList.csv")

# Calls the function 'open_movies_page' from 'fresh_tomoatoes.py' which
# renders the content to the HTML file.
fresh_tomatoes.open_movies_page(movies)