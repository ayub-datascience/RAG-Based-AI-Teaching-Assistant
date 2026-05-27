import requests # Used to send API requests to Ollama running locally.
import os
import json
import pandas as pd
import joblib

def create_embeddings(text_list):
    # Post request:- You are sending text to: "http://localhost:11434/api/embed" and getting embeddings back.
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list

    })

    embedding = r.json()["embeddings"]
    return embedding

jsons = os.listdir("jsons")
my_dicts = []
chunk_id = 0

for json_file in jsons:
    with open(f"jsons/{json_file}") as f:
        content = json.load(f)

    print(f"Creating Embeddings for {json_file}")
    embeddings = create_embeddings([c['text'] for c in content['chunks']])

    # enumerate provides both: The "item" and "index number" of that item at the same time. Here item=chunk and index number=i. Hence we not used i += 1 here.
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id += 1
        my_dicts.append(chunk)


# from_records() is a Pandas method used to create a DataFrame from: A list of dictionaries (my_dicts), A list of tuples etc.
df = pd.DataFrame.from_records(my_dicts)

# Save the DataFrame using joblib.
joblib.dump(df, "Vector_Embeddings.joblib")

