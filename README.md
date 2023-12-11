# 🚀 **ProjectTextFAISS**

Part of a suite including [`ProjectTextAgent`](https://github.com/Flagro/ProjectTextAgent) and [`ProjectDataBaseQnA`](https://github.com/Flagro/ProjectDataBaseQnA), ProjectTextFAISS is a FastAPI web app encapsulating a FAISS vector index for easy management of embeddings and metadata.

## 🌟 **Features**
- **Add Data**: Add text, file path, and metadata using `POST /add_data/`.
- **Delete Data**: Mark data as deleted via file path using `DELETE /delete_data/`.
- **Search Similar**: Search for similar text using `POST /search_similar/`.

## 🚀 **Getting Started**
Make sure to have docker installed on your system and then simply copy and initialize the .env file and do a docker compose up:
```bash
mv .env-example .env
docker compose up
```

## 📘 **Usage**
Accessible by default at `127.0.0.1:8000`. 

🛠️ **API Endpoints**
- **Add Data (POST /add_data/)**: Requires `text`, `file_path`, `metadata`, and credentials.
- **Delete Data (DELETE /delete_data/)**: Needs `file_path` and credentials.
- **Search Similar (POST /search_similar/)**: Expects `query`, optional `k` (int), `distance_threshold` (float), and credentials.

## 🤝 **Collaboration & Issues**
Open for collaboration; check the [issues page](https://github.com/Flagro/ProjectTextFAISS/issues) for discussions.
