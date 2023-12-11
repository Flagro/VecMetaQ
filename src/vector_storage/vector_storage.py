def chunk_text(text, max_tokens=512):
    # Split text into chunks of max_tokens
    chunks = []
    current_chunk = ""
    for token in text.split(" "):
        if len(current_chunk) + len(token) < max_tokens:
            current_chunk += token + " "
        else:
            chunks.append(current_chunk)
            current_chunk = ""
    chunks.append(current_chunk)
    return chunks


def concat_chunks(chunks):
    # Concatenate chunks into single string
    return "".join(chunks)


class VectorStorage:
    def __init__(self, faiss_index, embedding_model, metadata_db):
        self.faiss_index = faiss_index
        self.embedding_model = embedding_model
        self.metadata_db = metadata_db

    def add_data(self, text, file_path, metadata):
        for chunk in chunk_text(text, self.embedding_model.max_tokens):
            embedding = self.embedding_model.generate_embedding(chunk)
            index_id = self.faiss_index.add_vector(embedding)
            self.metadata_db.add_metadata(index_id, file_path, metadata)

    def delete_data(self, file_path):
        # Mark entries as deleted in metadata database for given file_path
        self.metadata_db.mark_deleted(file_path)

    def search_similar(self, query_text, k=None, distance_threshold=None):
        query_embedding = self.embedding_model.generate_embedding(query_text)
        indices = self.faiss_index.search_vector(query_embedding, k, distance_threshold)
        results = self.metadata_db.get_metadata(indices, exclude_deleted=True)

        # Aggregate results by file_path and concatenate text chunks
        aggregated_results = {}
        for result in results:
            file_path = result['file_path']
            if file_path not in aggregated_results:
                aggregated_results[file_path] = {'text': [], 'file_path': file_path, 'metadata': result['metadata']}
            aggregated_results[file_path]['text'].append(result['text'])
        
        for file_path, result in aggregated_results.items():
            result['text'] = concat_chunks(result['text'])

        return list(aggregated_results.values())
