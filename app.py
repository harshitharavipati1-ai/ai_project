# app.py

from dotenv import load_dotenv
import os
from groq import Groq
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify

# -----------------------------
# Create Flask app
# -----------------------------
app = Flask(__name__)
=======
>>>>>>> 1e05be0ff380682155cace53c505a473494222f1

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file. Check your .env!")

<<<<<<< HEAD
print("Loaded Key:", api_key)
=======
print("Loaded Key:", api_key)  # Debug to confirm key loaded
>>>>>>> 1e05be0ff380682155cace53c505a473494222f1

# -----------------------------
# Initialize Groq client
# -----------------------------
client = Groq(api_key=api_key)

# -----------------------------
# Load embedding model
# -----------------------------
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# -----------------------------
# Load documents from file
# -----------------------------
<<<<<<< HEAD
=======
# Make sure you have data.txt in project root with text data
>>>>>>> 1e05be0ff380682155cace53c505a473494222f1
with open("data.txt", "r", encoding="utf-8") as f:
    documents = f.readlines()

# -----------------------------
# Create embeddings
# -----------------------------
doc_embeddings = embedding_model.encode(documents)
doc_embeddings = np.array(doc_embeddings).astype("float32")

# -----------------------------
# Create FAISS index
# -----------------------------
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

# -----------------------------
# Retrieval function
# -----------------------------
def retrieve(query, top_k=3):
<<<<<<< HEAD

    query_embedding = embedding_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")

    distances, indices = index.search(query_embedding, top_k)

=======
    query_embedding = embedding_model.encode([query])
    query_embedding = np.array(query_embedding).astype("float32")
    distances, indices = index.search(query_embedding, top_k)
>>>>>>> 1e05be0ff380682155cace53c505a473494222f1
    return [documents[i] for i in indices[0]]

# -----------------------------
# Generate answer function
# -----------------------------
def generate_answer(query):
<<<<<<< HEAD

=======
>>>>>>> 1e05be0ff380682155cace53c505a473494222f1
    retrieved_docs = retrieve(query)
    context = "\n".join(retrieved_docs)

    prompt = f"""
Answer the question based only on the context below.

Context:
{context}

Question:
{query}

Answer:
"""

<<<<<<< HEAD
    response = client.chat.completions.create(
        model="groq/compound-mini",
=======
    # -----------------------------
    # Groq chat completion
    # -----------------------------
    response = client.chat.completions.create(
        model="groq/compound-mini",  # <-- use a model your key can access
>>>>>>> 1e05be0ff380682155cace53c505a473494222f1
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )

<<<<<<< HEAD
    return response.choices[0].message.content

# -----------------------------
# Webpage route
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")

# -----------------------------
# Chat API route
# -----------------------------
@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    answer = generate_answer(user_message)

    return jsonify({"reply": answer})

# -----------------------------
# Run Flask App
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
=======
    return response.choices[0].message.content, retrieved_docs

# -----------------------------
# Main execution
# -----------------------------
if __name__ == "__main__":
    query = input("Enter your question: ")
    answer, sources = generate_answer(query)

    print("\nAnswer:\n", answer)
    print("\nSources:")
    for src in sources:
        print("-", src.strip())
>>>>>>> 1e05be0ff380682155cace53c505a473494222f1
