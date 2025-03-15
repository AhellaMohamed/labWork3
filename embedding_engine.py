from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

embedding_model = OpenAIEmbeddings()

def create_embedding(text):
    """Generate an embedding for the given text."""
    return embedding_model.embed_query(text)

def store_embeddings(articles):
    """Store embeddings in FAISS for efficient retrieval."""
    texts = [article["content"] for article in articles if article["content"]]
    embeddings = [create_embedding(text) for text in texts]
    
    db = FAISS.from_embeddings(embeddings, texts)
    return db
