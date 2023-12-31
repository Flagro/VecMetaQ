# 🚀 **VecMetaQ**

Part of a [`ProjectText Suite`](https://github.com/Flagro/ProjectTextSuite). VecMetaQ (Vector Metadata Query) is a FastAPI web app encapsulating a FAISS vector index for easy management of embeddings and metadata.

## 🌟 **Features**
- **Add Data**: Add text, tag, and metadata using `POST /add_data/`.
- **Delete Data**: Mark data as deleted via tag using `DELETE /delete_data/`.
- **Search Similar**: Search for similar text using `POST /search_similar/`.

## 🚀 **Getting Started**
Make sure to have docker installed on your system and then simply copy and initialize the .env file and do a docker compose up:
```bash
mv .env-example .env
docker compose up
```

Or to use the GHCR you can (make sure to have the .env file ready):
```bash
docker pull ghcr.io/flagro/vecmetaq
docker run -it --env-file .env ghcr.io/flagro/vecmetaq
```

## 📘 **Usage**
Accessible by default at `127.0.0.1:8000`. 

🛠️ **API Endpoints**
- **Add Data (POST /add_data/)**: Requires `text`, `tag`, `metadata`, and credentials.
- **Delete Data (DELETE /delete_data/)**: Needs `tag` and credentials.
- **Search Similar (POST /search_similar/)**: Expects `query`, optional `k` (int), `distance_threshold` (float), and credentials.

## 🤝 **Collaboration & Issues**
Open for collaboration; check the [issues page](https://github.com/Flagro/VecMetaQ/issues) for discussions.
