import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib

def createEmbedding(text_list):

    r = requests.post("http://localhost:11434/api/embed",json = {"model" : "bge-m3", "input" : text_list})

    embeddings = r.json()['embeddings']

    return embeddings

#output = createEmbedding(["I am Iron Man","I can do this all day"])

#print(output)

my_dict = []
chunk_id = 0

jsons = os.listdir("newjsons")

for file in jsons:

    with open(f"newjsons/{file}") as f:
        content = json.load(f)
 
    print(f"Creating Embeddings for {file}")

    embeddings = createEmbedding([c['text'] for c in content['chunks']])
    for i,chunk in enumerate(content["chunks"]):

        chunk["id"] = chunk_id 
        chunk["embedding"] = embeddings[i]
        my_dict.append(chunk)
        chunk_id += 1
       
    
#print(my_dict)


df = pd.DataFrame.from_records(my_dict)
#print(df)

joblib.dump(df,"embeddings.joblib")

