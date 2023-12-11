def chunk_text(text, max_tokens):
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
