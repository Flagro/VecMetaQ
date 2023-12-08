from fastapi import FastAPI
from .faiss_database.router import router as faiss_router

app = FastAPI()
app.include_router(faiss_router)
