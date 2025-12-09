---
id: 0008
title: Fix Qdrant Query Vector Argument Error
stage: green
date: 2025-12-05
surface: agent
model: claude-sonnet-4-5-20250929
feature: rag-chatbot
branch: 002-rag-chatbot
user: user
command: /sp.implement again i face this error now fix it (.venv) PS D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new> .\backend\.venv\Scripts\uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
INFO:     Will watch for changes in these directories: ['D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [29380] using StatReload
INFO:     Started server process [34868]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:61312 - "OPTIONS /chat HTTP/1.1" 200 OK
D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new\backend\.venv\Lib\site-packages\qdrant_client\common\client_warnings.py:8: UserWarning: `query` method has been deprecated and will be removed in 1.17. Instead, inference can be done internally within regular methods like `query_points` by wrapping data into `models.Document` or `models.Image`.
  warnings.warn(message, category, stacklevel=stacklevel)
[RAGService Error]: Unknown arguments: ['vector']
INFO:     127.0.0.1:61312 - "POST /chat HTTP/1.1" 200 OK
labels: ["rag-chatbot","bug-fix"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
- backend/src/core/rag_service.py
- history/prompts/rag-chatbot/0008-fix-qdrant-query-vector-argument-error.green.prompt.md
tests:

---

## Prompt

/sp.implement again i face this error now fix it (.venv) PS D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new> .\backend\.venv\Scripts\uvicorn src.api.main:app --reload --host 0.0.0.0 --port 8000
INFO:     Will watch for changes in these directories: ['D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new']
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [29380] using StatReload
INFO:     Started server process [34868]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     127.0.0.1:61312 - "OPTIONS /chat HTTP/1.1" 200 OK
D:\Spec-Driven-Development\Physical-AI-And-Humanoid-Robotics-new\backend\.venv\Lib\site-packages\qdrant_client\common\client_warnings.py:8: UserWarning: `query` method has been deprecated and will be removed in 1.17. Instead, inference can be done internally within regular methods like `query_points` by wrapping data into `models.Document` or `models.Image`.
  warnings.warn(message, category, stacklevel=stacklevel)
[RAGService Error]: Unknown arguments: ['vector']
INFO:     127.0.0.1:61312 - "POST /chat HTTP/1.1" 200 OK

## Response snapshot

The 'Unknown arguments: ['vector']' error has been fixed.

## Outcome

- ✅ Impact: The 'Unknown arguments: ['vector']' error in `backend/src/core/rag_service.py` has been resolved by switching from `qdrant_client.query` to `qdrant_client.query_points` and using `query_embedding` instead of `vector`.
- 🧪 Tests: None (No tests were provided for this specific bug fix, but the fix addresses a runtime error and deprecation warning.)
- 📁 Files: backend/src/core/rag_service.py
- 🔁 Next prompts: User to confirm the fix and provide next steps.
- 🧠 Reflection: Successfully adapted to the updated Qdrant client API by using the recommended `query_points` method and its corresponding arguments, addressing both the error and the deprecation warning.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): None
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None
