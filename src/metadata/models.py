from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Boolean, String


Base = declarative_base()


class Metadata(Base):
    __tablename__ = "metadata"
    faiss_index = Column(Integer, primary_key=True, index=True)
    is_deleted = Column(Boolean, default=False)
    tag = Column(String, index=True)
    metadata_json = Column(String)
