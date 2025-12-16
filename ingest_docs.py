import os
import uuid
import httpx
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()

# --- CONFIGURATION ---
# Change this to your Docusaurus docs folder path
DOCS_PATH = "./my-book/docs" 
COLLECTION_NAME = "textbook_collection"

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
QDRANT_URL = os.getenv("QDRANT_URL").rstrip('/')
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")

def get_markdown_files(directory):
    """Finds all .md and .mdx files in the Docusaurus folder."""
    return list(Path(directory).rglob("*.md")) + list(Path(directory).rglob("*.mdx"))

def upload_to_qdrant(text, source_name):
    """Embeds text and sends it to Qdrant."""
    if len(text.strip()) < 10: return # Skip empty files

    # 1. Create Embedding
    print(f"🔄 Processing: {source_name}")
    emb_response = client.embeddings.create(
        input=text,
        model="text-embedding-3-small"
    )
    vector = emb_response.data[0].embedding

    # 2. Upload to Qdrant
    headers = {"api-key": QDRANT_API_KEY, "Content-Type": "application/json"}
    payload = {
        "points": [{
            "id": str(uuid.uuid4()),
            "vector": vector,
            "payload": {
                "text": text,
                "source": source_name
            }
        }]
    }
    
    url = f"{QDRANT_URL}/collections/{COLLECTION_NAME}/points"
    httpx.put(url, json=payload, headers=headers)

def run_ingestion():
    files = get_markdown_files(DOCS_PATH)
    print(f"📚 Found {len(files)} files in Docusaurus docs.")

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Simple chunking: You might want to split large files by paragraph
            # For now, we upload the whole file as one context
            upload_to_qdrant(content, file_path.name)

    print("✅ Ingestion complete! Your AI now knows your Docusaurus book.")

if __name__ == "__main__":
    run_ingestion()