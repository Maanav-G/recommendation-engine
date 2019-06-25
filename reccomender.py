import pandas as pd 
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

def get_title_from_index(index):
    return dataFrame[dataFrame.index == index]["title"].values[0]

def get_index_from_title(title):
    return dataFrame[dataFrame.title == title]["index"].values[0]

#1 CSV
dataFrame = pd.read_csv("movie_dataset.csv")
print dataFrame.columns

#2 Features
features = ['keywords', 'cast', 'genres', 'director']

#3 Create a column in dataFrame which combines features
def combine_features(row):
    return row['keywords']+" "+row['cast'}+" "+row['genres']+" "+row['director']

#4 Create count matrix from the new combined column

#5 Compute the Cosine Similarity based on the count_matrix

movie_user_likes = "Avatar"

#6 Get index of the movie from the title 

#7 Get a list of similar movies, in order of similarity score 

#8 Print titles of first 50 movies 
