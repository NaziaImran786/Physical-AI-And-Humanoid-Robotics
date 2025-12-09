# D:\...\backend\src\api\main.py

from dotenv import load_dotenv
load_dotenv()   # Load .env BEFORE anything else

from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.core.rag_service import RAGService

app = FastAPI(
    title="Panaversity RAG Chatbot API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

# ---------------------------
# FIX 1: SAFE Lazy Initialization
# ---------------------------
rag_service = None

def get_rag_service():
    global rag_service
    if rag_service is None:
        rag_service = RAGService()   # build only once, safely
    return rag_service


# ---------------------------
# FIX 2: SAFE Request Model
# ---------------------------
class ChatRequest(BaseModel):
    message: str


@router.get("/")
def read_root():
    return {"message": "Chatbot API is running."}


@router.post("/chat")
async def handle_chat(data: ChatRequest):
    message = data.message

    rag = get_rag_service()

    try:
        retrieved_content = rag.retrieve_content(message)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {
        "response": retrieved_content,
        "original": message
    }


app.include_router(router)
