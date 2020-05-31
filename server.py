import pandas as pd 
import numpy as np
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask_cors import cross_origin
import pickle
from math import ceil, floor
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 
from fuzzywuzzy import process 

app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/")
def index():
    return "Server's Up"

@cross_origin(supports_credentials=True)
@app.route("/get_recommendations", methods=['POST'])    
def get_recommendations():
    movie_user_inputted = request.form['movie_name']
    print(movie_user_inputted)
    movie_user_likes = get_matches(movie_user_inputted, dataFrame["only_titles"])[0][0]
    movie_index = get_index_from_title(movie_user_likes)
    similar_movies = list(enumerate(cosine_sim[movie_index]))
    sorted_similar_movies = sorted(similar_movies,key= lambda x:x[1], reverse=True)

    i=0 
    movie_list = []

    for movie in sorted_similar_movies:
        movie_title = get_title_from_index(movie[0])
        similarity = round(float_round(movie[1], 3, ceil)*100)
        data = [{
            'title': movie_title,
            'similarity': similarity
        }]
        movie_list.append(data)
        i=i+1
        if i>10:
            break
    return jsonify(movie_list)


dataFrame = pd.read_csv("./movie_dataset.csv")
features = ['keywords', 'cast', 'genres', 'director']
titles = ['title']

for feature in features:
    dataFrame[feature] = dataFrame[feature].fillna(' ')

def combine_features(row):
    try:
        return row['keywords']+" "+row['cast']+" "+row['genres']+" "+row['director']
    except:
        print ("Error: " + row)

dataFrame["combined_features"] = dataFrame.apply(combine_features, axis=1)

for title in titles:
    dataFrame[title] = dataFrame[title].fillna(' ')

def only_title(row):
    try:
        return row['title']
    except:
        print ("Error: " + row)

dataFrame["only_titles"] = dataFrame.apply(only_title, axis=1)

cv = CountVectorizer()
count_matrix = cv.fit_transform(dataFrame["combined_features"])
cosine_sim = cosine_similarity(count_matrix)

def get_matches(query, choices, limit=3):
    results = process.extract(query, choices, limit=limit)
    return results

def get_index_from_title(title):
    return dataFrame[dataFrame.title == title]["index"].values[0]



def get_title_from_index(index):
    return dataFrame[dataFrame.index == index]["title"].values[0]

def float_round(num, places = 0, direction = floor):
    return direction(num * (10**places)) / float(10**places)




if __name__ == '__main__':
    app.run(debug=True)


