# Tasks: RAG Chatbot Integration

**Input**: Design documents from `/specs/002-rag-chatbot-integration/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification does not explicitly request tests, but TDD is a core principle (III). Therefore, test tasks will be included for critical components.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`
- Paths shown below assume web application structure.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure for backend and frontend.

- [ ] T001 Create backend project structure in `backend/` per implementation plan
- [ ] T002 Initialize Python project with FastAPI and dependencies in `backend/src/`
- [ ] T003 Create frontend project structure in `frontend/` for Docusaurus components
- [ ] T004 Initialize React/TypeScript project with Docusaurus dependencies in `frontend/src/`
- [ ] T005 [P] Configure linting and formatting for backend (e.g., Black, flake8) in `backend/`
- [ ] T006 [P] Configure linting and formatting for frontend (e.g., Prettier, ESLint) in `frontend/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented.

**⚠️ CRITICAL**: No user story work can begin until this phase is complete.

- [ ] T007 Setup FastAPI application instance and basic routing in `backend/src/api/main.py`
- [ ] T008 Configure Qdrant Cloud connection in `backend/src/core/qdrant_client.py`
- [ ] T009 Configure Neon Serverless Postgres connection in `backend/src/core/neon_db.py`
- [ ] T010 [P] Implement environment variable loading for API keys and connection strings in `backend/src/core/config.py`
- [ ] T011 [P] Implement basic error handling middleware for FastAPI in `backend/src/api/middleware/error_handler.py`
- [ ] T012 [P] Configure structured logging for backend in `backend/src/core/logger.py`

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Ask Textbook Questions (Priority: P1) 🎯 MVP

**Goal**: Enable users to ask general questions about the textbook content and receive answers.

**Independent Test**: A user can navigate to any Docusaurus page, activate the chatbot, ask a question relevant to the textbook, and receive a correct answer sourced from the book.

### Tests for User Story 1 ⚠️

- [ ] T013 [P] [US1] Unit test for text chunking utility in `backend/tests/unit/test_text_processor.py`
- [ ] T014 [P] [US1] Unit test for Qdrant search service in `backend/tests/unit/test_qdrant_service.py`
- [ ] T015 [P] [US1] Integration test for RAG pipeline (without OpenAI) in `backend/tests/integration/test_rag_pipeline.py`
- [ ] T016 [P] [US1] Unit test for basic chatbot UI component rendering in `frontend/tests/unit/test_chatbot_component.test.tsx`

### Implementation for User Story 1

- [ ] T017 [US1] Implement text chunking and embedding generation utility in `backend/src/services/text_processor.py`
- [ ] T018 [US1] Implement service for Qdrant vector database interactions (indexing, search) in `backend/src/services/qdrant_service.py`
- [ ] T019 [US1] Implement RAG pipeline logic to retrieve context from Qdrant in `backend/src/services/rag_pipeline.py`
- [ ] T020 [US1] Integrate OpenAI Agents/ChatKit SDK for response generation in `backend/src/services/openai_agent.py`
- [ ] T021 [US1] Create FastAPI endpoint for general question answering in `backend/src/api/routers/chatbot.py`
- [ ] T022 [US1] Develop basic React chatbot UI component (`ChatWindow`, `TextInput`, `MessageDisplay`) in `frontend/src/components/Chatbot/`
- [ ] T023 [US1] Implement frontend service for API calls to the FastAPI chatbot endpoint in `frontend/src/services/chatbot_api.ts`

**Checkpoint**: User Story 1 should be fully functional and testable independently.

---

## Phase 4: User Story 2 - Answer Based on Selected Text (Priority: P2)

**Goal**: Allow users to ask questions based only on selected text within the textbook.

**Independent Test**: A user can select a paragraph of text, activate the chatbot, ask a question about the selected text, and receive an answer derived exclusively from the selected content.

### Tests for User Story 2 ⚠️

- [ ] T024 [P] [US2] Unit test for text selection utility in `frontend/tests/unit/test_text_selection.test.ts`
- [ ] T025 [P] [US2] Integration test for RAG pipeline with selected text context in `backend/tests/integration/test_rag_selected_text.py`

### Implementation for User Story 2

- [ ] T026 [US2] Implement frontend utility to capture and pass selected text to the chatbot component in `frontend/src/hooks/useTextSelection.ts`
- [ ] T027 [US2] Modify chatbot UI component to accept and display selected text context in `frontend/src/components/Chatbot/ChatWindow.tsx`
- [ ] T028 [US2] Update FastAPI chatbot endpoint to receive selected text and pass to RAG pipeline in `backend/src/api/routers/chatbot.py`
- [ ] T029 [US2] Modify RAG pipeline to use selected text as primary context or filter in `backend/src/services/rag_pipeline.py`

**Checkpoint**: User Stories 1 AND 2 should both work independently.

---

## Phase 5: User Story 3 - Seamless Docusaurus Integration (Priority: P1)

**Goal**: Ensure the RAG chatbot integrates seamlessly into the Docusaurus environment.

**Independent Test**: The chatbot interface can be easily activated and used from any Docusaurus page, maintaining the Docusaurus styling and responsiveness.

### Tests for User Story 3 ⚠️

- [ ] T030 [P] [US3] E2E test for chatbot activation/deactivation on Docusaurus page in `frontend/tests/e2e/test_docusaurus_integration.spec.ts`
- [ ] T031 [P] [US3] E2E test for responsive behavior of chatbot UI across breakpoints in `frontend/tests/e2e/test_responsive_chatbot.spec.ts`

### Implementation for User Story 3

- [ ] T032 [US3] Create Docusaurus plugin or theme component to embed the chatbot in `frontend/src/theme/ChatbotWrapper.tsx`
- [ ] T033 [US3] Apply Docusaurus-compatible styling to chatbot components in `frontend/src/components/Chatbot/styles.css`
- [ ] T034 [US3] Ensure chatbot responsiveness and accessibility within Docusaurus layout in `frontend/src/components/Chatbot/ChatWindow.tsx`

**Checkpoint**: All user stories should now be independently functional.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories and overall system quality.

- [ ] T035 Documentation updates for backend API endpoints (e.g., OpenAPI spec generation) in `backend/docs/`
- [ ] T036 Code cleanup and refactoring across backend and frontend
- [ ] T037 Performance optimization for RAG pipeline and frontend rendering
- [ ] T038 Implement robust security measures (e.g., API rate limiting, input sanitization) in `backend/src/api/`
- [ ] T039 Implement comprehensive metrics and tracing for backend services in `backend/src/core/observability.py`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately.
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories.
- **User Stories (Phase 3+)**: All depend on Foundational phase completion.
  - User stories can then proceed in parallel (if staffed) or sequentially in priority order (P1 → P2 → P3).
- **Polish (Final Phase)**: Depends on all desired user stories being complete.

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories.
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Depends on US1 for core chatbot functionality, but can be developed relatively independently.
- **User Story 3 (P1)**: Can start after Foundational (Phase 2) - Depends on US1 for the chatbot component to embed.

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation.
- Models before services.
- Services before endpoints/UI components.
- Core implementation before integration.
- Story complete before moving to next priority.

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel.
- All Foundational tasks marked [P] can run in parallel (within Phase 2).
- Once Foundational phase completes, User Story 1, User Story 2 (with US1 as a dependency), and User Story 3 (with US1 as a dependency) can be worked on in parallel by different team members.
- All tests for a user story marked [P] can run in parallel.
- Different user stories can be worked on in parallel by different team members, considering explicit dependencies.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 3 (P1) → Test independently → Deploy/Demo
4. Add User Story 2 (P2) → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together.
2. Once Foundational is done:
   - Developer A: User Story 1 (core RAG chatbot).
   - Developer B: User Story 3 (Docusaurus integration, depends on A for basic chatbot).
   - Developer C: User Story 2 (selected text functionality, depends on A for core RAG).
3. Stories complete and integrate independently.

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
