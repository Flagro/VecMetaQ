from pydantic import BaseModel
from typing import List, Optional


class SearchResult(BaseModel):
    index: int
    distance: float
    tag: str
    metadata: str


class SearchResponse(BaseModel):
    results: List[SearchResult]


class AddDataRequest(BaseModel):
    text: str
    tag: str
    metadata: str


class DeleteDataRequest(BaseModel):
    tag: str


class SearchSimilarRequest(BaseModel):
    query: str
    k: Optional[int] = None
    distance_threshold: Optional[float] = None
