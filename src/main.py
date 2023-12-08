from fastapi import FastAPI
from .faiss_index.router import router as faiss_router

app = FastAPI()
app.include_router(faiss_router)
