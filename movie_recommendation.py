import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
data = {
"Movie": ["Avengers","Iron Man","Thor","Titanic","Notebook"],
"Action": [1,1,1,0,0],
"Romance": [0,0,0,1,1]
}

df = pd.DataFrame(data)
similarity = cosine_similarity(df[["Action","Romance"]])
def recommend(movie):
    index = df[df["Movie"] == movie].index[0]
    
    scores = list(enumerate(similarity[index]))
    
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    
    for i in scores[1:3]:
        print(df.iloc[i[0]].Movie)
recommend("Avengers")