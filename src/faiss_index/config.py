from decouple import config


FAISS_DIMENSION = config("FAISS_DIMENSION", cast=int)
