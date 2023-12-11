from sentence_transformers import SentenceTransformer
from .config import SENTENCE_TRANSFORMERS_MODEL, SENTENCE_TRANSFORMERS_MAX_TOKENS


class SentenceEmbedding:
    def __init__(self):
        self.model = SentenceTransformer(SENTENCE_TRANSFORMERS_MODEL)
        self.max_tokens = SENTENCE_TRANSFORMERS_MAX_TOKENS

    def encode(self, doc):
        return self.model.encode(doc)
