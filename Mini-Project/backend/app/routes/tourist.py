"""API routes for the tourist guide"""
import logging
from fastapi import APIRouter, HTTPException
from app.models import TouristQueryRequest, TouristQueryResponse, CityInfo
from app.services.tourist_guide import get_tourist_guide

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/tourist", tags=["tourist"])


@router.post("/ask", response_model=TouristQueryResponse)
async def ask_tourist_guide(request: TouristQueryRequest):
    """
    Ask the tourist guide about cities and ancient heritage sites.

    The guide will:
    - Provide detailed information about cities and their heritage sites
    - Share historical context and significance
    - Offer practical travel tips and recommendations
    - Inspire you to visit these incredible destinations

    Example queries:
    - "Tell me about ancient heritage sites in Rome"
    - "What can I visit in Athens?"
    - "Best time to visit Machu Picchu?"
    - "What are the must-see temples in Kyoto?"
    - "Ancient monuments in Egypt"
    """
    try:
        guide = get_tourist_guide()
        result = await guide.get_travel_advice(request.query)

        return TouristQueryResponse(**result)

    except Exception as e:
        logger.error(f"Error in tourist guide endpoint: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to process tourist query: {str(e)}"
        )


@router.get("/cities", response_model=list[CityInfo])
async def get_available_cities():
    """
    Get a list of all cities available in the tourist guide knowledge base.

    Returns information about each city including:
    - City name
    - Country
    - Number of heritage sites covered
    """
    try:
        guide = get_tourist_guide()
        cities = guide.get_available_cities()
        return cities

    except Exception as e:
        logger.error(f"Error getting available cities: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Failed to retrieve cities: {str(e)}"
        )


@router.get("/health")
async def tourist_guide_health():
    """Check if the tourist guide service is healthy"""
    try:
        guide = get_tourist_guide()
        cities = guide.get_available_cities()
        return {
            "status": "healthy",
            "vectorstore": "initialized" if guide.vectorstore else "not_initialized",
            "cities_available": len(cities),
            "model": "gpt-4o-mini"
        }
    except Exception as e:
        logger.error(f"Tourist guide health check failed: {str(e)}")
        raise HTTPException(
            status_code=503,
            detail=f"Tourist guide service unhealthy: {str(e)}"
        )
