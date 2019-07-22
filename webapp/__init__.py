from flask import Flask
from flask import render_template

from datetime import datetime

app  = Flask(__name__)

@app.route("/")
def index():
    """ Renders list of movies
    """
    return render_template("index.html", 
                            title="Reccomendation Engine",  
                            movie_user_inputted = movie_user_inputted,
                            )



""" 
    Model of reccomendation engine - start
"""
import pandas as pd 
import numpy as np
import pickle
from math import ceil, floor
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
from fuzzywuzzy import process 



# Read CSV
dataFrame = pd.read_csv("./dataset/movie_dataset.csv")

# Features
features = ['keywords', 'cast', 'genres', 'director']
# extracted titles only 
titles = ['title']


# Create a column in dataFrame which combines features
# replaced all "NaN"'s with " "
for feature in features:
    dataFrame[feature] = dataFrame[feature].fillna(' ')

def combine_features(row):
    try:
        return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
    except:
        print "Error: ", row

dataFrame["combined_features"] = dataFrame.apply(combine_features, axis=1)
# print "Combined Features:", dataFrame["combined_features"].head()

# created a titles only data frame
for title in titles:
    dataFrame[title] = dataFrame[title].fillna(' ')

def only_title(row):
    try:
        return row['title']
    except:
        print "Error: ", row

dataFrame["only_titles"] = dataFrame.apply(only_title, axis=1)



# Create count matrix from the new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(dataFrame["combined_features"])


# Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)

movie_user_inputted = "The Avenegers"
# returns similar matches from title database
def get_matches(query, choices, limit=3):
    results = process.extract(query, choices, limit=limit)
    return results
movie_user_likes = get_matches(movie_user_inputted, dataFrame["only_titles"])[0][0]


# Get index of the movie from the title 
def get_index_from_title(title):
    return dataFrame[dataFrame.title == title]["index"].values[0]

movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))

# Get a list of similar movies, in order of similarity score 
sorted_similar_movies = sorted(similar_movies,key= lambda x:x[1], reverse=True)

# Print titles of first 20 movies 
def get_title_from_index(index):
    return dataFrame[dataFrame.index == index]["title"].values[0]

# round to n number of decimals 
def float_round(num, places = 0, direction = floor):
    return direction(num * (10**places)) / float(10**places)

print movie_user_inputted
i=0 
for movie in sorted_similar_movies:
    print "Movie: ", get_title_from_index(movie[0]), "\n", "Similarity: ", round(float_round(movie[1], 3, ceil)*100), "%", "\n" 
    i=i+1
    if i>20:
        break



""" 
    Model of reccomendation engine - end
"""



if __name__=="__main__":
	# app.run(threaded=True)
	app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)