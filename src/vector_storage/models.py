from pydantic import BaseModel
from typing import List


class SearchResult(BaseModel):
    index: int
    distance: float
    tag: str
    metadata: str


class SearchResponse(BaseModel):
    results: List[SearchResult]
