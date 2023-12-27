from ..embedding.chunking import chunk_text, concat_chunks


class VectorStorage:
    def __init__(self, faiss_index, embedding_model, metadata_db):
        self.faiss_index = faiss_index
        self.embedding_model = embedding_model
        self.metadata_db = metadata_db

    def add_data(self, text, tag, metadata):
        for chunk in chunk_text(text, self.embedding_model.max_tokens):
            embedding = self.embedding_model.generate_embedding(chunk)
            index_id = self.faiss_index.add_vector(embedding)
            self.metadata_db.add_metadata(index_id, tag, metadata)

    def delete_data(self, tag):
        # Mark entries as deleted in metadata database for given tag
        self.metadata_db.mark_deleted(tag)

    def search_similar(self, query_text, k=None, distance_threshold=None):
        query_embedding = self.embedding_model.generate_embedding(query_text)
        indices = self.faiss_index.search_vector(query_embedding, k, distance_threshold)
        results = self.metadata_db.get_metadata(indices, exclude_deleted=True)

        # Aggregate results by tag and concatenate text chunks
        aggregated_results = {}
        for result in results:
            tag = result['tag']
            if tag not in aggregated_results:
                aggregated_results[tag] = {'text': [], 'tag': tag, 'metadata': result['metadata']}
            aggregated_results[tag]['text'].append(result['text'])
        
        for tag, result in aggregated_results.items():
            result['text'] = concat_chunks(result['text'])

        return list(aggregated_results.values())
