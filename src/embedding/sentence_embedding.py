from sentence_transformers import SentenceTransformer
from .config import SENTENCE_TRANSFORMERS_MODEL


class SentenceEmbedding:
    def __init__(self):
        self.model = SentenceTransformer(SENTENCE_TRANSFORMERS_MODEL)

    def encode(self, doc):
        return self.model.encode(doc)
