from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .config import FAISS_USER, FAISS_PASSWORD


security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != FAISS_USER or credentials.password != FAISS_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
