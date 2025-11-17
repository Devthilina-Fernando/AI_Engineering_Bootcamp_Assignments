from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
import httpx
from dotenv import load_dotenv
from typing import Optional

load_dotenv()

app = FastAPI(title="Weather Chatbot API", version="1.0.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize OpenAI client
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


class ChatMessage(BaseModel):
    message: str
    conversation_history: Optional[list] = []


async def search_weather_with_tavily(query: str) -> str:
    """Search for weather information using Tavily API"""
    if not TAVILY_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Tavily API key not configured. Please set TAVILY_API_KEY in your environment."
        )
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.tavily.com/search",
                json={
                    "api_key": TAVILY_API_KEY,
                    "query": query,
                    "search_depth": "basic",
                    "include_answer": True,
                    "include_raw_content": False,
                    "max_results": 5
                },
                timeout=30.0
            )
            response.raise_for_status()
            data = response.json()
            
            # Extract answer if available, otherwise use results
            if data.get("answer"):
                return data["answer"]
            elif data.get("results"):
                # Combine results into a summary
                results_text = "\n".join([
                    f"- {result.get('title', '')}: {result.get('content', '')[:200]}"
                    for result in data["results"][:3]
                ])
                return results_text
            else:
                return "No weather information found."
    except httpx.HTTPError as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error fetching weather data from Tavily: {str(e)}"
        )


async def generate_weather_image(weather_details: str, location: str, weather_info: str) -> str:
    """Generate a weather image with detailed information using OpenAI DALL-E"""
    try:
        # Create a detailed prompt that includes weather information as text overlays
        prompt = f"""A professional weather forecast infographic card showing the weather for {location}. 
The image should display:
- A beautiful realistic weather scene in the background showing the current weather conditions
- Weather forecast card style with text overlays showing detailed weather information
- Include visible text displaying: location name "{location}", temperature, weather conditions, and other key details
- Modern, clean design with readable text overlays
- Professional weather app style with information clearly visible
- The background scene should match the weather conditions described

Weather details to display: {weather_details}

Make sure all text is clearly visible and readable in the image."""
        
        response = openai_client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1024x1024",
            quality="standard",
            n=1,
        )
        
        return response.data[0].url
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating weather image: {str(e)}"
        )


def extract_location_from_message(message: str) -> str:
    """Extract location from user message using OpenAI"""
    try:
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Extract the location name from the user's message. Return only the location name, nothing else. If no location is mentioned, return 'current location'."},
                {"role": "user", "content": message}
            ],
            max_tokens=50,
            temperature=0.3
        )
        location = response.choices[0].message.content.strip()
        return location if location else "current location"
    except:
        return "current location"


@app.get("/")
async def root():
    return {"message": "Welcome to Weather Chatbot API"}


@app.post("/api/chat")
async def chat(chat_message: ChatMessage):
    """
    Chat endpoint that uses Tavily to search for weather info and OpenAI to generate responses
    """
    if not chat_message.message or not chat_message.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty")
    
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=500,
            detail="OpenAI API key not configured. Please set OPENAI_API_KEY in your environment."
        )
    
    try:
        # Extract location from message
        location = extract_location_from_message(chat_message.message)
        
        # Search for weather information using Tavily
        weather_info = await search_weather_with_tavily(
            f"weather forecast {location} {chat_message.message}"
        )
        
        # Build conversation history for context
        messages = [
            {
                "role": "system",
                "content": "You are a friendly and knowledgeable weather assistant. Use the provided weather information to answer user questions accurately and conversationally. Be concise but informative. If the weather information doesn't fully answer the question, use your knowledge to provide helpful context."
            }
        ]
        
        # Add conversation history
        for msg in chat_message.conversation_history[-5:]:  # Keep last 5 messages for context
            messages.append({
                "role": msg.get("role", "user"),
                "content": msg.get("content", "")
            })
        
        # Add current user message with weather context
        user_prompt = f"""Weather information for {location}:
{weather_info}

User question: {chat_message.message}

Please answer the user's question about the weather using the information provided above."""
        
        messages.append({"role": "user", "content": user_prompt})
        
        # Get response from OpenAI
        response = openai_client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=500,
            temperature=0.7
        )
        
        assistant_message = response.choices[0].message.content.strip()
        
        # Generate weather image with detailed information
        try:
            # Extract detailed weather information for the image
            weather_details_prompt = f"""Based on the following weather information, create a concise summary that includes:
- Current temperature (if available)
- Weather conditions (sunny, rainy, cloudy, etc.)
- Key details like humidity, wind speed, or precipitation (if mentioned)
- Time of day or forecast period

Weather information:
{weather_info}

Assistant response:
{assistant_message}

Format the summary as a brief, clear description suitable for a weather forecast card. Include specific numbers and details when available."""
            
            weather_details_response = openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a weather information formatter. Extract and format weather details clearly and concisely for display on a weather forecast card."},
                    {"role": "user", "content": weather_details_prompt}
                ],
                max_tokens=150,
                temperature=0.3
            )
            weather_details = weather_details_response.choices[0].message.content.strip()
            image_url = await generate_weather_image(weather_details, location, weather_info)
        except Exception as e:
            # If image generation fails, continue without image
            print(f"Image generation error: {str(e)}")
            image_url = None
        
        return {
            "response": assistant_message,
            "location": location,
            "weather_info": weather_info,
            "image_url": image_url
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing chat message: {str(e)}"
        )

