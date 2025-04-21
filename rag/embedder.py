from config import PINECONE_API_KEY, PINECONE_INDEX
from sentence_transformers import SentenceTransformer
import pinecone

model = SentenceTransformer("all-MiniLM-L6-v2")
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)

# Auto-create index if missing
if PINECONE_INDEX not in [i.name for i in pc.list_indexes()]:
    pc.create_index(
        name=PINECONE_INDEX,
        dimension=384,
        metric="cosine",
        spec={"serverless": {"cloud": "aws", "region": "us-east-1"}}
    )

index = pc.Index(PINECONE_INDEX)




from sentence_transformers import SentenceTransformer
from config import PINECONE_API_KEY, PINECONE_INDEX
import pinecone
import uuid

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize Pinecone v3 client
pc = pinecone.Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(PINECONE_INDEX)

def embed_and_store(text, metadata={}):
    # Break text into small chunks (~300 characters)
    chunks = [text[i:i+300] for i in range(0, len(text), 300)]

    # Generate embeddings
    vectors = []
    for chunk in chunks:
        embedding = model.encode([chunk])[0].tolist()
        vector_id = str(uuid.uuid4())
        vectors.append((vector_id, embedding, {**metadata, "text": chunk}))

    # Upload to Pinecone
    index.upsert(vectors=vectors)
    return len(vectors)
