from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

text = ["Test Two", "Test One"]
cv = CountVectorizer()

count_matrix = cv.fit_transform(text)
# print count_matrix.toarray()

similarity_scores = cosine_similarity(count_matrix) 
print similarity_scores
