import requests
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib


def create_embeddings(text_list):
    # Post request:- You are sending text to: "http://localhost:11434/api/embed" and getting embeddings back.
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": text_list

    })

    embedding = r.json()["embeddings"]
    return embedding

def response_from_LLM(prompt):
    print("Getting response from LLM.....")
    # Post request:- You are sending prompt to: "http://localhost:11434/api/generate" and getting response back.
    r = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False # “Give complete response at once.”
        }
    )

    return r.json()["response"]

df = joblib.load("Vector_Embeddings.joblib")

incoming_query = input("Ask a Question: ")
incoming_query_embedding = create_embeddings([incoming_query])[0] # We are taking the first element of the list because create_embeddings() function returns a list of embeddings, but we are sending only one query, so we will get only one embedding in the list. Hence we take the first element of the list using [0]. If we were sending multiple queries, then we would not use [0] and we would get a list of embeddings for all the queries we sent.

# Find the cosine similarity (Semantic Search) between the incoming_query_embedding and the other embeddings present in the DataFrame.
# np.vstack(...) :- Stacks all embeddings vertically into matrix form. Why? Because cosine similarity expects matrix input.
# .flatten() :- Converts output into simple 1D array.
similarities = cosine_similarity(np.vstack(df['embedding']), [incoming_query_embedding]).flatten()


top_results = 5 # I want top 5 results.
# .argsort() :- It returns: The indexes of sorted values in ascending order. [::-1] :- It reverses the order of indexes, so we will get the indexes of sorted values in descending order. [0:top_results] :- It gives us the top 5 indexes.
# Why we are taking the indexes of sorted values in decending order? Because w.k.t higher the value, the more similar it is...
max_indx = similarities.argsort()[::-1][0:top_results]
new_df = df.loc[max_indx] # Now you retrieve those rows from DataFrame.

prompt = f'''You are a helpful AI Teaching Assistant.

Answer the user's question ONLY using the provided context.

If the answer is not present in the context, say:
"I could not find the answer for the provided context."

Context:
{new_df[["file_name", "tutorial_number", "start", "end", "text"]].to_json(orient = "records")}

User Question:
{incoming_query}

'''

response = response_from_LLM(prompt)
print(response)

