"""Tourist guide service using FAISS vectorstore and OpenAI"""
import logging
from typing import Optional, Dict, Any
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from app.config import settings
from app.data.tourist_data import TOURIST_DATA

logger = logging.getLogger(__name__)


class TouristGuideService:
    """
    Tourist guide service that uses FAISS in-memory vectorstore to provide
    information about cities and their ancient heritage sites.
    """

    def __init__(self):
        """Initialize the tourist guide service with FAISS vectorstore"""
        self.embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0.7,
            openai_api_key=settings.OPENAI_API_KEY
        )
        self.vectorstore: Optional[FAISS] = None
        self._initialize_vectorstore()

    def _initialize_vectorstore(self):
        """Initialize FAISS vectorstore with tourist data"""
        try:
            logger.info("Initializing FAISS vectorstore with tourist data...")

            # Prepare documents from tourist data
            documents = []
            metadatas = []

            for city_data in TOURIST_DATA:
                city = city_data["city"]
                country = city_data["country"]

                # Add main city description
                main_doc = f"""City: {city}, {country}

Description: {city_data["description"]}

Best Season to Visit: {city_data["best_season"]}

Local Tips: {city_data["local_tips"]}
"""
                documents.append(main_doc)
                metadatas.append({
                    "type": "city_overview",
                    "city": city,
                    "country": country
                })

                # Add each heritage site as a separate document
                for site in city_data["heritage_sites"]:
                    site_doc = f"""Heritage Site: {site["name"]} in {city}, {country}

Description: {site["description"]}

Best Time to Visit: {site["best_time"]}

Travel Tips: {site["tips"]}

City Overview: {city_data["description"]}
"""
                    documents.append(site_doc)
                    metadatas.append({
                        "type": "heritage_site",
                        "site_name": site["name"],
                        "city": city,
                        "country": country
                    })

            # Split documents into smaller chunks for better retrieval
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )

            split_docs = []
            split_metadatas = []

            for doc, metadata in zip(documents, metadatas):
                chunks = text_splitter.split_text(doc)
                split_docs.extend(chunks)
                split_metadatas.extend([metadata] * len(chunks))

            # Create FAISS vectorstore
            self.vectorstore = FAISS.from_texts(
                texts=split_docs,
                embedding=self.embeddings,
                metadatas=split_metadatas
            )

            logger.info(f"FAISS vectorstore initialized with {len(split_docs)} document chunks")

        except Exception as e:
            logger.error(f"Error initializing vectorstore: {str(e)}")
            raise

    def _create_prompt_template(self) -> PromptTemplate:
        """Create a prompt template for the tourist guide"""
        template = """You are an enthusiastic and knowledgeable tourist guide specializing in ancient heritage sites and historical destinations. Your goal is to inspire travelers and make them excited about visiting these incredible places.

Use the following context about cities and heritage sites to answer the traveler's question:

Context:
{context}

Question: {question}

Instructions:
1. Provide detailed, engaging information about the city or heritage sites mentioned
2. Highlight the historical significance and unique features that make these places special
3. Include practical travel tips like best times to visit, what to expect, and local recommendations
4. Use vivid, descriptive language that helps the traveler imagine being there
5. If mentioning multiple sites, organize your response clearly
6. Encourage the traveler and express enthusiasm about these destinations
7. If the question is not about tourist destinations or travel, politely redirect them to ask about cities and heritage sites

Your Response:"""

        return PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )

    async def get_travel_advice(self, query: str) -> Dict[str, Any]:
        """
        Get travel advice based on user query using RAG with FAISS.

        Args:
            query: The user's question about a city or heritage site

        Returns:
            Dictionary containing the response and metadata
        """
        try:
            if not self.vectorstore:
                raise ValueError("Vectorstore not initialized")

            logger.info(f"Processing tourist query: {query}")

            # Create retrieval QA chain
            prompt_template = self._create_prompt_template()

            qa_chain = RetrievalQA.from_chain_type(
                llm=self.llm,
                chain_type="stuff",
                retriever=self.vectorstore.as_retriever(
                    search_type="similarity",
                    search_kwargs={"k": 4}  # Retrieve top 4 most relevant chunks
                ),
                return_source_documents=True,
                chain_type_kwargs={"prompt": prompt_template}
            )

            # Get response
            result = qa_chain.invoke({"query": query})

            # Extract source information
            sources = []
            cities_mentioned = set()

            for doc in result.get("source_documents", []):
                metadata = doc.metadata
                if metadata.get("city"):
                    cities_mentioned.add(f"{metadata['city']}, {metadata['country']}")
                if metadata.get("site_name"):
                    sources.append(metadata["site_name"])

            return {
                "success": True,
                "response": result["result"],
                "cities_mentioned": list(cities_mentioned),
                "heritage_sites_mentioned": list(set(sources)),
                "sources_count": len(result.get("source_documents", []))
            }

        except Exception as e:
            logger.error(f"Error processing tourist query: {str(e)}")
            return {
                "success": False,
                "error": f"Failed to process query: {str(e)}",
                "response": "I apologize, but I encountered an error while processing your request. Please try again."
            }

    def get_available_cities(self) -> list:
        """Get list of available cities in the knowledge base"""
        return [
            {
                "city": data["city"],
                "country": data["country"],
                "heritage_sites_count": len(data["heritage_sites"])
            }
            for data in TOURIST_DATA
        ]


# Singleton instance
_tourist_guide_instance: Optional[TouristGuideService] = None


def get_tourist_guide() -> TouristGuideService:
    """Get or create the tourist guide singleton instance"""
    global _tourist_guide_instance
    if _tourist_guide_instance is None:
        _tourist_guide_instance = TouristGuideService()
    return _tourist_guide_instance
