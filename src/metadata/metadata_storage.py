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
    
    def add_metadata(self, index_id, file_path, metadata):
        db_session = self.db()
        new_metadata = self.Metadata(faiss_index=index_id, file_path=file_path, metadata=metadata)
        db_session.add(new_metadata)
        try:
            db_session.commit()
        except:
            db_session.rollback()
            raise
        finally:
            db_session.close()


    def get_metadata(self, indices, exclude_deleted=True):
        db_session = self.db()
        query = db_session.query(self.Metadata).filter(self.Metadata.faiss_index.in_(indices))
        if exclude_deleted:
            query = query.filter(self.Metadata.is_deleted == False)
        results = query.all()
        db_session.close()
        return results


    def mark_deleted(self, file_path):
        db_session = self.db()
        db_session.query(self.Metadata).filter(self.Metadata.file_path == file_path).update({"is_deleted": True})
        try:
            db_session.commit()
        except:
            db_session.rollback()
            raise
        finally:
            db_session.close()
