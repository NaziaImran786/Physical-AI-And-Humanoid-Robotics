---
id: 0001
title: Amend Constitution for RAG Chatbot Integration
stage: constitution
date: 2025-12-03
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: 001-docusaurus-setup
user: User
command: |
  /sp.constitution read project and implement next task """ RAG Chatbot Integration
  Develop and embed a RAG-based AI assistant inside the textbook using:
  - *OpenAI Agents / ChatKit SDK*
  - *FastAPI backend*
  - *Qdrant Cloud* (vector database)
  - *Neon Serverless Postgres* (structured data)

  The chatbot must:
  - Answer questions based on book content.
  - Support “answer based on selected text only”.
  - Work seamlessly inside Docusaurus.
  """
labels: ["constitution", "rag-chatbot"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - ./.specify/memory/constitution.md
tests:
---

## Prompt

```text
 read project and implement next task """ RAG Chatbot Integration
Develop and embed a RAG-based AI assistant inside the textbook using:
- *OpenAI Agents / ChatKit SDK*
- *FastAPI backend*
- *Qdrant Cloud* (vector database)
- *Neon Serverless Postgres* (structured data)

The chatbot must:
- Answer questions based on book content.
- Support “answer based on selected text only”.
- Work seamlessly inside Docusaurus.
"""
```

## Response snapshot

Updated project constitution to version 1.0.1, adding a new principle for 'External Service Integration & AI Responsibility' to reflect the RAG Chatbot Integration feature. The existing constitution file `./.specify/memory/constitution.md` was modified.

## Outcome

- ✅ Impact: Constitution updated.
- 🧪 Tests: N/A
- 📁 Files: .specify/memory/constitution.md modified.
- 🔁 Next prompts: The next steps would be to plan the implementation of the RAG Chatbot Integration.
- 🧠 Reflection: Constitution updated to reflect new project direction.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
