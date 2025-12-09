import os
from qdrant_client import QdrantClient, models
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class RAGService:
    def __init__(self):
        # Qdrant client
        self.qdrant_client = QdrantClient(
            url=f"https://{os.getenv('QDRANT_HOST')}",
            api_key=os.getenv("QDRANT_API_KEY"),
            timeout=60,
        )

        # Embeddings model
        self.embeddings_model = OpenAIEmbeddings(
            api_key=os.getenv("OPENAI_API_KEY"),
            model="text-embedding-ada-002"
        )

        # LLM
        self.llm = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model="gpt-3.5-turbo"
        )

        # Prompt template
        self.prompt = ChatPromptTemplate.from_template(
            """Answer the question based only on the following context:
{context}

Question: {question}"""
        )

    def retrieve_content(self, query: str):
        try:
            # 1️⃣ Embed the query
            query_vector = self.embeddings_model.embed_query(query)

            # 2️⃣ Query Qdrant using query_points (latest client)
            collection_name = os.getenv("QDRANT_COLLECTION_NAME", "docusaurus_docs")
            results = self.qdrant_client.query_points(
                collection_name=collection_name,
                query_vector=query_vector,
                limit=1
            )

            # 3️⃣ Extract context safely
            context = "No relevant content found."
            if results and results.points and len(results.points) > 0:
                payload = results.points[0].payload
                if payload and "content" in payload:
                    context = payload["content"]

            # 4️⃣ Generate LLM response
            chain = self.prompt | self.llm
            response = chain.invoke({"context": context, "question": query})
            return response.content

        except Exception as e:
            print(f"[RAGService Error]: {e}")
            return "Sorry, an error occurred while retrieving content."
