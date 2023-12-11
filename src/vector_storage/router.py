from fastapi import APIRouter, Depends, HTTPException
from .models import Vector
from ..faiss_index.faiss_index import FaissIndex
from ..embedding.sentence_embedding import SentenceEmbedding
from ..auth.dependencies import get_current_username


router = APIRouter()
faiss_index = FaissIndex()
embedding_model = SentenceEmbedding()


@router.post("/add_vector/")
def add_vector(vector: Vector, username: str = Depends(get_current_username)):
    try:
        faiss_index.add_vector(vector.vector)
        return {"message": "Vector added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/search/")
def search_vector(vector: Vector, username: str = Depends(get_current_username)):
    try:
        distances, indices = faiss_index.search_vector(vector.vector)
        return {"distances": distances.tolist(), "indices": indices.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
