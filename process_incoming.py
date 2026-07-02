import pandas as pd
import numpy as np
import requests
from sklearn.metrics.pairwise import cosine_similarity
import joblib


df = joblib.load("embeddings.joblib")

def createEmbedding(text_list):

    r = requests.post("http://localhost:11434/api/embed",json = {"model" : "bge-m3", "input" : text_list})

    embeddings = r.json()['embeddings']

    return embeddings



input_query = input("Ask a question: ")
question_embedding = createEmbedding([input_query])[0]

#print(question_embedding)

similarities = cosine_similarity(np.vstack(df['embedding']),[question_embedding]).flatten()
print(similarities)

top_results = 5
max_idx = similarities.argsort()[::-1][0:top_results] # np.argsort() gives us the index of similarities and the index of max similarity is at the end.Here we reversed the array of index of similarities as we want the index of max similarity at the front.
print(max_idx)
# print(np.vstack(df['embedding'].values)) # np.vstack converts the embeddings into a 2-dimensional(2D) vector form.
# print(np.vstack(df['embedding']).shape)

new_df = df.loc[max_idx]
#print(new_df[["title","number","text"]])

prompt = f'''
I am teaching sigma web development in my web sigma web development course.Here are video subtitle chunks containing video title, video number, 
start time in seconds, end time in seconds, the text at that time

{new_df[["title","number","start","end","text"]].to_json(orient = "records")} 

---------------------------------------------

{input_query}
User asked this question related to the video chunks, you have to answer in a human way(don't mention the above format, its just for you) where and how much content is taught where 
and in which video (in which video and at what timestamp) and guide the user to go to that particular video.
If user aks unrelated question, tell him that you can only answer questions related to the course




'''
# f

# orient = "records" in to_json() gives us a list of dictionaries
with open("prompt.txt","w") as f:
    f.write(prompt)



def inference(prompt):

    r = requests.post("http://localhost:11434/api/generate", 
                      json =  
                        {"model" : "llama3.2",
                        "prompt" : prompt, 
                         "stream" : False
                        })
    
    response = r.json()["response"]
    return response


model_response = inference(prompt)

print(model_response)

with open("response.txt","w") as f:
    f.write(model_response)