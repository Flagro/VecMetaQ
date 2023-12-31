from decouple import config


SENTENCE_TRANSFORMERS_MODEL = config("SENTENCE_TRANSFORMERS_MODEL")
SENTENCE_TRANSFORMERS_MAX_TOKENS = config("SENTENCE_TRANSFORMERS_MAX_TOKENS", cast=int)
