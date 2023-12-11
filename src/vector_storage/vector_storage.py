class VectorStorage:
    def __init__(self, faiss_index, embedding_model, metadata_db):
        self.faiss_index = faiss_index
        self.embedding_model = embedding_model
        self.metadata_db = metadata_db

    def add_data(self, text, file_path, metadata):
        # Generate embedding
        embedding = self.embedding_model.generate_embedding(text)

        # Add embedding to FAISS index
        index_id = self.faiss_index.add_vector(embedding)

        # Store metadata in database with index_id
        self.metadata_db.add_metadata(index_id, file_path, metadata)

    def delete_data(self, file_path):
        # Mark entries as deleted in metadata database for given file_path
        self.metadata_db.mark_deleted(file_path)

    def search_similar(self, query_text):
        # Generate embedding for query
        query_embedding = self.embedding_model.generate_embedding(query_text)

        # Search in FAISS
        distances, indices = self.faiss_index.search_vector(query_embedding)

        # Fetch metadata for indices and aggregate by file_path
        results = self.metadata_db.get_metadata(indices, exclude_deleted=True)
        return distances, results
