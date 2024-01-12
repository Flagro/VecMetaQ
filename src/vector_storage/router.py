from fastapi import APIRouter, Depends, HTTPException
from typing import Optional
from .models import SearchResponse, AddDataRequest, DeleteDataRequest, SearchSimilarRequest
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
def add_data(request: AddDataRequest, username: str = Depends(get_current_username)):
    try:
        vector_storage.add_data(request.text, request.tag, request.metadata)
        return {"message": "Data added successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/delete_data/")
def delete_data(request: DeleteDataRequest, username: str = Depends(get_current_username)):
    try:
        vector_storage.delete_data(request.tag)
        return {"message": "Data marked as deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/search_similar/", response_model=SearchResponse)
def search_similar(request: SearchSimilarRequest, username: str = Depends(get_current_username)):
    try:
        results = vector_storage.search_similar(request.query, request.k, request.distance_threshold)
        return SearchResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
