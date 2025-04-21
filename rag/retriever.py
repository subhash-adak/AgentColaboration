from sentence_transformers import SentenceTransformer
from config import PINECONE_API_KEY, PINECONE_INDEX
import pinecone

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Setup Pinecone v3 client
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

def retrieve_relevant_chunks(query, top_k=3):
    # Convert query to embedding
    embed = model.encode([query])[0].tolist()

    # Query Pinecone index
    results = index.query(vector=embed, top_k=top_k, include_metadata=True)

    # Extract relevant text chunks
    return "\n".join([match["metadata"]["text"] for match in results["matches"]])
