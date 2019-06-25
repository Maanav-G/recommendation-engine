import pandas as pd 
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

def get_title_from_index(index):
    return dataFrame[dataFrame.index == index]["title"].values[0]

def get_index_from_title(title):
    return dataFrame[dataFrame.title == title]["index"].values[0]

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
print "Combined Features:", dataFrame["combined_features"].head()


#4 Create count matrix from the new combined column
cv = CountVectorizer()
count_matrix = cv.fit_transform(dataFrame["combined_features"])


#5 Compute the Cosine Similarity based on the count_matrix
cosine_sim = cosine_similarity(count_matrix)
movie_user_likes = "Avatar"


#6 Get index of the movie from the title 

#7 Get a list of similar movies, in order of similarity score 

#8 Print titles of first 50 movies 
