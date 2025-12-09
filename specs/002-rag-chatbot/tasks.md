# Tasks: RAG Chatbot Integration

**Feature Branch**: `002-rag-chatbot` | **Date**: 2025-12-03 | **Spec**: specs/002-rag-chatbot/spec.md
**Input**: Feature specification from `/specs/002-rag-chatbot/spec.md` and implementation plan from `/specs/002-rag-chatbot/plan.md`

**Note**: This template is filled in by the `/sp.tasks` command. See
`.specify/templates/commands/tasks.md` for the execution workflow.

---

## Implementation Strategy

This feature will be implemented incrementally, starting with core infrastructure and then addressing each user story in priority order. The Minimum Viable Product (MVP) for this feature is the complete implementation of "User Story 1 - Ask Question on Book Content."

---

## Phases & Tasks

### Phase 1: Setup

Goal: Initialize the project structure and configure basic dependencies for both frontend and backend components.

- [ ] T001 Create backend directory structure for FastAPI application in `backend/`
- [ ] T002 Initialize Python environment and install FastAPI, Uvicorn in `backend/`
- [ ] T003 Create frontend directory structure for Docusaurus integration in `frontend/`
- [ ] T004 Initialize Node.js environment and install Docusaurus, React in `frontend/`
- [ ] T005 Configure Docusaurus project to allow custom React components in `frontend/docusaurus.config.js`

### Phase 2: Foundational Components

Goal: Establish connections to external services (Qdrant, Neon) and implement initial data handling for RAG.

- [ ] T006 Implement Qdrant Cloud client initialization in `backend/src/services/qdrant_service.py`
- [ ] T007 Implement Neon Serverless Postgres client initialization in `backend/src/services/postgres_service.py`
- [ ] T008 Develop a script for initial Docusaurus content extraction and embedding generation in `backend/src/scripts/ingest_content.py`
- [ ] T009 Implement logic to store document embeddings in Qdrant Cloud in `backend/src/services/qdrant_service.py`
- [ ] T010 Implement logic to store conversation history in Neon Serverless Postgres in `backend/src/services/postgres_service.py`
- [ ] T011 Create `backend/src/core/rag_service.py` with Qdrant client and OpenAI embedding model initialization

### Phase 3: User Story 1 - Ask Question on Book Content (Priority: P1)

Goal: Enable the chatbot to answer general questions based on the entire book content.

- [ ] T012 [US1] Create `backend/src/api/main.py` with FastAPI app initialization and CORS middleware
- [ ] T013 [US1] Define the `/chat` endpoint in `backend/src/api/main.py` which uses the service from `backend/src/core/rag_service.py`
- [ ] T014 [US1] Develop FastAPI endpoint for general chatbot queries in `backend/src/api/chatbot.py`
- [ ] T015 [US1] Implement RAG logic to retrieve relevant content from Qdrant for general queries in `backend/src/services/rag_service.py`
- [ ] T016 [US1] Integrate OpenAI Agents / ChatKit SDK for generating responses based on retrieved context in `backend/src/services/openai_agent.py`
- [ ] T017 [US1] Create a basic React chatbot UI component in `frontend/src/components/Chatbot/index.tsx`
- [ ] T018 [US1] Integrate the chatbot UI component into a Docusaurus page or layout in `frontend/src/theme/Layout/index.js`
- [ ] T019 [US1] Implement frontend logic to send user queries to the backend API and display responses in `frontend/src/components/Chatbot/index.tsx`
- [ ] T020 [US1] Add basic styling to the chatbot UI in `frontend/src/css/custom.css`
- [ ] T021 [P] [US1] Implement unit tests for general query RAG logic in `backend/tests/unit/test_rag_service.py`
- [ ] T022 [P] [US1] Implement integration tests for the general chatbot API endpoint in `backend/tests/integration/test_chatbot_api.py`

### Phase 4: User Story 2 - Ask Question on Selected Text (Priority: P1)

Goal: Extend the chatbot to answer questions strictly confined to user-selected text.

- [ ] T023 [US2] Develop FastAPI endpoint for selected text chatbot queries in `backend/src/api/chatbot.py`
- [ ] T024 [US2] Implement RAG logic to retrieve relevant content from Qdrant, strictly limited to selected text context in `backend/src/services/rag_service.py`
- [ ] T025 [US2] Modify frontend to allow user text selection and pass it to the chatbot component in `frontend/src/components/Chatbot/index.tsx` and Docusaurus content files
- [ ] T026 [US2] Update frontend logic to send selected text along with queries to the backend API in `frontend/src/components/Chatbot/index.tsx`
- [ ] T027 [P] [US2] Implement unit tests for selected text RAG logic in `backend/tests/unit/test_rag_service.py`
- [ ] T028 [P] [US2] Implement integration tests for the selected text chatbot API endpoint in `backend/tests/integration/test_chatbot_api.py`

### Phase 5: User Story 3 - Seamless Docusaurus Integration (Priority: P1)

Goal: Ensure the chatbot seamlessly integrates with the Docusaurus UI/UX.

- [ ] T029 [US3] Implement dynamic styling for the chatbot UI to adapt to Docusaurus themes (e.g., dark mode) in `frontend/src/components/Chatbot/index.tsx` and `frontend/src/css/custom.css`
- [ ] T030 [US3] Ensure chatbot state persists across Docusaurus page navigations (if required by design) in `frontend/src/components/Chatbot/index.tsx` or `frontend/src/context/ChatbotContext.js`
- [ ] T031 [US3] Optimize chatbot loading and initialization to meet performance goals in `frontend/src/components/Chatbot/index.tsx`
- [ ] T032 [P] [US3] Implement end-to-end tests for chatbot UI responsiveness and theme integration in `frontend/tests/e2e/test_chatbot_ui.spec.js`

### Final Phase: Polish & Cross-Cutting Concerns

Goal: Address edge cases, error handling, and overall system robustness.

- [ ] T033 Implement comprehensive error handling for Qdrant, Neon, and OpenAI API calls in `backend/src/services/`
- [ ] T034 Implement graceful degradation for network failures or API timeouts in `backend/src/api/` and `frontend/src/components/Chatbot/index.tsx`
- [ ] T035 Handle cases where no relevant information is found in book content or selected text in `backend/src/services/rag_service.py`
- [ ] T036 Implement logging and monitoring for chatbot interactions and system performance in `backend/src/utils/logger.py`
- [ ] T037 Review and optimize backend queries for Qdrant and Neon for performance and cost efficiency in `backend/src/services/`
- [ ] T038 Implement a mechanism for storing and retrieving conversation history in `backend/src/services/postgres_service.py`

---

## Dependency Graph (User Story Completion Order)

- User Story 1 (P1): Ask Question on Book Content
- User Story 2 (P1): Ask Question on Selected Text (depends on User Story 1)
- User Story 3 (P1): Seamless Docusaurus Integration (can be developed in parallel with or after US1 and US2)

---

## Parallel Execution Examples (Per User Story)

### User Story 1 - Ask Question on Book Content

- `T021 [P] [US1] Implement unit tests for general query RAG logic in backend/tests/unit/test_rag_service.py`
- `T022 [P] [US1] Implement integration tests for the general chatbot API endpoint in backend/tests/integration/test_chatbot_api.py`

### User Story 2 - Ask Question on Selected Text

- `T027 [P] [US2] Implement unit tests for selected text RAG logic in backend/tests/unit/test_rag_service.py`
- `T028 [P] [US2] Implement integration tests for the selected text chatbot API endpoint in backend/tests/integration/test_chatbot_api.py`

### User Story 3 - Seamless Docusaurus Integration

- `T032 [P] [US3] Implement end-to-end tests for chatbot UI responsiveness and theme integration in frontend/tests/e2e/test_chatbot_ui.spec.js`

---

## Output Validation (Self-Check)

- [X] All tasks adhere to the checklist format: `- [ ] [TaskID] [P?] [Story?] Description with file path`
- [X] Tasks are organized by user story, with dedicated phases.
- [X] Each user story has independent test criteria and, where applicable, test tasks.
- [X] Dependency graph clearly outlines user story completion order.
- [X] Parallel execution opportunities are identified.
- [X] Suggested MVP scope is clear.
