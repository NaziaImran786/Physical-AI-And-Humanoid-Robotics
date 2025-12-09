---
id: 0009
title: Fix Qdrant Query Embedding Argument Error
stage: green
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: rag-chatbot
branch: 002-rag-chatbot
user: user
command: /sp.implement fix my error (.venv) PS D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new> .\backend\.venv\Scripts\uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
INFO:     Will watch for changes in these directories: ['D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1560] using StatReload
INFO:     Started server process [34184]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
[RAGService Error]: Unknown arguments: ['query_embedding']
INFO:     127.0.0.1:51821 - "POST /chat HTTP/1.1" 200 OK
labels: ["rag-chatbot","bug-fix"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- backend/src/core/rag_service.py
- history/prompts/rag-chatbot/0009-fix-qdrant-query-embedding-argument-error.green.prompt.md
tests:

---

## Prompt

/sp.implement fix my error (.venv) PS D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new> .\backend\.venv\Scripts\uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
INFO:     Will watch for changes in these directories: ['D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [1560] using StatReload
INFO:     Started server process [34184]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
[RAGService Error]: Unknown arguments: ['query_embedding']
INFO:     127.0.0.1:51821 - "POST /chat HTTP/1.1" 200 OK

## Response snapshot

The 'Unknown arguments: ['query_embedding']' error has been fixed.

## Outcome

- ✅ Impact: The 'Unknown arguments: ['query_embedding']' error in `backend/src/core/rag_service.py` has been resolved by switching from `qdrant_client.query_points` to `qdrant_client.search` and using `query_vector` instead of `query_embedding`.
- 🧪 Tests: None (No tests were provided for this specific bug fix, but the fix addresses a runtime error.)
- 📁 Files: backend/src/core/rag_service.py
- 🔁 Next prompts: User to confirm the fix and provide next steps.
- 🧠 Reflection: Successfully adapted to the correct Qdrant client API for vector similarity search by using the `search` method and its `query_vector` argument, resolving the previous error.

## Evaluation notes (flywheel)

- Failure modes observed: Confusion between `query_points` and `search` methods, and their respective argument names (`vector`, `query_embedding`, `query_vector`) in the Qdrant client library.
- Graders run and results (PASS/FAIL): None
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): Improve internal knowledge base or proactive documentation lookup for specific library API changes, especially for rapidly evolving libraries like Qdrant client.
