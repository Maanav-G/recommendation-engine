import pandas as pd 
import numpy as np
from math import ceil, floor
from fuzzywuzzy import process 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

dataFrame = pd.read_csv("./dataset/movie_dataset.csv")






titles = ['title']

for title in titles:
    dataFrame[title] = dataFrame[title].fillna(' ')

def only_title(row):
    try:
        return row['title']
    except:
        print "Error: ", row

dataFrame["only_titles"] = dataFrame.apply(only_title, axis=1)


def get_matches(query, choices, limit=3):
    results = process.extract(query, choices, limit=limit)
    return results
movie_user_inputted = "avaaatar"
movie_user_likes = get_matches(movie_user_inputted, dataFrame["only_titles"])[0][0]

print movie_user_likes





# print dataFrame["combined_features"]