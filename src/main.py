from fastapi import FastAPI
from .vector_storage.router import router as vector_storage_router

app = FastAPI()
app.include_router(vector_storage_router)
