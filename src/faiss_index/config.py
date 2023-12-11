from decouple import config


FAISS_DIMENSION = config("FAISS_DIMENSION", cast=int)
FAISS_DEFAULT_K = config("FAISS_DEFAULT_K", cast=int)
FAISS_DEFAULT_DISTANCE_THRESHOLD = config("FAISS_DEFAULT_DISTANCE_THRESHOLD", cast=float)
