import pandas as pd 
import numpy as np

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]