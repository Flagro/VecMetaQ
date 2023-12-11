import numpy as np
import faiss
from .config import FAISS_DIMENSION, FAISS_DEFAULT_K, FAISS_DEFAULT_DISTANCE_THRESHOLD


class FaissIndex:
    def __init__(self):
        self.index = faiss.IndexFlatIP(FAISS_DIMENSION)

    def add_vector(self, embedding):
        vec = np.array(embedding, dtype='float32').reshape(1, -1)
        faiss.normalize_L2(vec)
        self.index.add(vec)

    def search_vector(self, embedding, k=FAISS_DEFAULT_K, distance_threshold=FAISS_DEFAULT_DISTANCE_THRESHOLD):
        vec = np.array(embedding, dtype='float32').reshape(1, -1)
        faiss.normalize_L2(vec)
        return self.index.search(vec, k)
