import os
import httpx
from pathlib import Path
from dotenv import load_dotenv
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from openai import OpenAI

# 1. FIX: Explicitly find the .env file in the project root
# This looks 2 levels up from 'api/routes/chat.py' to find the root directory
base_dir = Path(__file__).resolve().parent.parent.parent
env_path = base_dir / ".env"
load_dotenv(dotenv_path=env_path)

router = APIRouter()

# 2. Get Variables
OPENAI_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
COLLECTION_NAME = "textbook_collection"

# 3. Validation Prints (Check your terminal when server starts)
print(f"--- Environment Check ---")
print(f"Looking for .env at: {env_path}")
print(f"Found .env: {env_path.exists()}")
print(f"QDRANT_URL Loaded: {'✅' if QDRANT_URL else '❌'}")
print(f"-------------------------")

client = OpenAI(api_key=OPENAI_KEY)

class ChatRequest(BaseModel):
    message: str

@router.get("/chat")
def chat_endpoint():
    return {"message": "Chat route working"}

@router.post("/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # Strict validation before making API calls
        if not QDRANT_URL or not QDRANT_API_KEY:
            raise ValueError("QDRANT_URL or QDRANT_API_KEY is missing from .env file")

        print(f"🔍 Searching for: {request.message}")

        # Step A: User Query to Vector
        emb_response = client.embeddings.create(
            input=request.message,
            model="text-embedding-3-small"
        )
        user_vector = emb_response.data[0].embedding

        # Step B: Direct API Call to Qdrant
        # Cleanup URL to prevent double slashes
        clean_url = QDRANT_URL.rstrip('/')
        search_url = f"{clean_url}/collections/{COLLECTION_NAME}/points/search"
        
        headers = {
            "api-key": str(QDRANT_API_KEY),
            "Content-Type": "application/json"
        }
        
        payload = {
            "vector": user_vector,
            "limit": 3,
            "with_payload": True
        }

        async with httpx.AsyncClient() as http_client:
            response = await http_client.post(search_url, json=payload, headers=headers, timeout=10.0)
            
            if response.status_code != 200:
                print(f"❌ Qdrant Error: {response.text}")
                raise Exception(f"Qdrant Search Failed: {response.text}")
                
            search_results = response.json().get("result", [])

        # Step C: Context Aggregation
        context = ""
        for item in search_results:
            # Safely navigate nested JSON
            payload_data = item.get("payload")
            if payload_data and "text" in payload_data:
                context += f"{payload_data['text']}\n---\n"

        if not context.strip():
            context = "No relevant context found in the book."

        print("✅ Context found! Generating answer...")

        # Step D: OpenAI Completion
        system_prompt = f"""You are a Robotics Tutor. Answer based ONLY on this context:
        
        {context}
        
        If answer is not in context, say 'I don't know based on the book'."""

        ai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": request.message}
            ]
        )

        return {"response": ai_response.choices[0].message.content}

    except Exception as e:
        print(f"❌ Error Detail: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))