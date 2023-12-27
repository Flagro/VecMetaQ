from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from .models import SearchResponse
from .vector_storage import VectorStorage
from ..faiss_index.faiss_index import FaissIndex
from ..embedding.sentence_embedding import SentenceEmbedding
from ..metadata.metadata_storage import MetaDataDataBase
from ..auth.dependencies import get_current_username


router = APIRouter()
faiss_index = FaissIndex()
embedding_model = SentenceEmbedding()
metadata_db = MetaDataDataBase()
vector_storage = VectorStorage(faiss_index, embedding_model, metadata_db)


@router.post("/add_data/")
def add_data(text: str, tag: str, metadata: str, username: str = Depends(get_current_username)):
    try:
        vector_storage.add_data(text, tag, metadata)
        return {"message": "Data added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_data/")
def delete_data(tag: str, username: str = Depends(get_current_username)):
    try:
        vector_storage.delete_data(tag)
        return {"message": "Data marked as deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/search_similar/", response_model=SearchResponse)
def search_similar(query: str, k: Optional[int], distance_threshold: Optional[float], username: str = Depends(get_current_username)):
    try:
        # Assuming vector_storage.search_similar returns a list of SearchResult objects
        results = vector_storage.search_similar(query, k, distance_threshold)
        return SearchResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
