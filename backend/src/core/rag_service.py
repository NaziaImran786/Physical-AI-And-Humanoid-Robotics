# src/core/rag_service.py

import os
from qdrant_client import QdrantClient
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate

class RAGService:
    def __init__(self):
        # 1️⃣ Qdrant Client initialization
        self.qdrant_client = QdrantClient(
            url=f"https://{os.getenv('QDRANT_HOST')}",
            api_key=os.getenv("QDRANT_API_KEY"),
            timeout=60
        )

        # 2️⃣ OpenAI embeddings & LLM
        self.embeddings_model = OpenAIEmbeddings(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model="text-embedding-ada-002"
        )

        self.llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            model_name="gpt-3.5-turbo"
        )

        # 3️⃣ Prompt template
        self.prompt = ChatPromptTemplate.from_template(
            """Answer the question based only on the following context:
{context}

Question: {question}"""
        )

    def retrieve_content(self, query: str):
        try:
            # Embed the query
            query_vector = self.embeddings_model.embed_query(query)

            # Query Qdrant
            collection_name = os.getenv("QDRANT_COLLECTION_NAME", "docusaurus_docs")
            search_results = self.qdrant_client.search(
                collection_name=collection_name,
                query_vector=query_vector,
                limit=3
            )

            # Extract context
            context = "No relevant content found."
            if search_results and len(search_results) > 0:
                for point in search_results:
                    if point.payload and "content" in point.payload:
                        context = point.payload["content"]
                        break

            # Generate LLM response
            final_prompt = self.prompt.format(context=context, question=query)
            response = self.llm(final_prompt)
            return response

        except Exception as e:
            print(f"[RAGService Critical Error]: {e}")
            raise e
