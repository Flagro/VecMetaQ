from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Metadata
from .config import SQLALCHEMY_DATABASE_URL


class MetaDataDataBase():
    def __init__(self):
        engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
        self.db = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.Metadata = Metadata
        self.Metadata.metadata.create_all(bind=engine)
    
    def add(self, obj):
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def get(self, obj):
        return self.db.query(obj).all()

    def delete(self, obj):
        self.db.delete(obj)
        self.db.commit()

    def update(self):
        self.db.commit()

    def close(self):
        self.db.close()
