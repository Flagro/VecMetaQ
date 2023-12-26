from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from .config import VECMETAQ_USER, VECMETAQ_PASSWORD


security = HTTPBasic()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username != VECMETAQ_USER or credentials.password != VECMETAQ_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect credentials",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username
