from sentence_transformers import SentenceTransformer
import numpy as np
EMBED_MODEL = None

def load_embed_model():
    global EMBED_MODEL
    if EMBED_MODEL is None:
        EMBED_MODEL = SentenceTransformer('all-MiniLM-L6-v2')
    return EMBED_MODEL

def embed_text(text):
    model = load_embed_model()
    return model.encode([text], convert_to_numpy=True)[0]

def cosine_sim(a, b):
    a = a / (np.linalg.norm(a) + 1e-10)
    b = b / (np.linalg.norm(b) + 1e-10)
    return float(np.dot(a, b))
