import numpy as np
import faiss
from .config import FAISS_DIMENSION


class FaissIndex:
    def __init__(self):
        self.index = faiss.IndexFlatIP(FAISS_DIMENSION)

    def add_vector(self, vector):
        vec = np.array(vector, dtype='float32').reshape(1, -1)
        faiss.normalize_L2(vec)
        self.index.add(vec)

    def search_vector(self, vector, k=1):
        vec = np.array(vector, dtype='float32').reshape(1, -1)
        faiss.normalize_L2(vec)
        return self.index.search(vec, k)
