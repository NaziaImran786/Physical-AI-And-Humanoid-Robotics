import os
import logging
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import chat

# 1. Load Environment Variables
load_dotenv()

# 2. Logging Setup (Terminal mein errors dekhne ke liye)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Physical AI & Humanoid Robotics API")

# 3. CORS Fix: Ye frontend ko backend se jodne ke liye zaroori hai
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development ke liye sahi hai
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Router Connection
# Note: Is prefix ki wajah se aapka URL http://127.0.0.1:8000/api/chat ban gaya hai
app.include_router(chat.router, prefix="/api", tags=["Chat"])

@app.get("/")
async def root():
    return {"status": "online", "message": "FastAPI RAG Backend is Running!"}

# Debugging helper: Terminal mein print karega ke server start ho gaya
@app.on_event("startup")
async def startup_event():
    print("\n🚀 Server is starting...")
    print("📍 API Endpoint: http://127.0.0.1:8000/api/chat")
    print("📑 Swagger Docs: http://127.0.0.1:8000/docs\n")