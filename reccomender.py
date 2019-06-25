import pandas as pd 
import numpy as np
from math import ceil, floor

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 


#1 CSV
dataFrame = pd.read_csv("./dataset/movie_dataset.csv")

#2 Features
features = ['keywords', 'cast', 'genres', 'director']

#3 Create a column in dataFrame which combines features
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


#4 Create count matrix from the new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(dataFrame["combined_features"])


#5 Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)

movie_user_likes = "The Avengers"

#6 Get index of the movie from the title 
def get_index_from_title(title):
    return dataFrame[dataFrame.title == title]["index"].values[0]

movie_index = get_index_from_title(movie_user_likes)
similar_movies = list(enumerate(cosine_sim[movie_index]))

#7 Get a list of similar movies, in order of similarity score 
sorted_similar_movies = sorted(similar_movies,key= lambda x:x[1], reverse=True)

#8 Print titles of first 20 movies 
def get_title_from_index(index):
    return dataFrame[dataFrame.index == index]["title"].values[0]

# round to n number of decimals 
def float_round(num, places = 0, direction = floor):
    return direction(num * (10**places)) / float(10**places)

i=0 
for movie in sorted_similar_movies:
    print "Name: ", get_title_from_index(movie[0]), "   ", "Similarity: ", round(float_round(movie[1], 3, ceil)*100), "%" 
    i=i+1
    if i>10:
        break


