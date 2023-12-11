from pydantic import BaseModel
from typing import List


class SearchResult(BaseModel):
    index: int
    distance: float
    file_path: str
    metadata: str


class SearchResponse(BaseModel):
    results: List[SearchResult]
