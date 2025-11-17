from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="VitalVibe API", version="1.0.0")

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


class DayDescription(BaseModel):
    description: str


@app.get("/")
async def root():
    return {"message": "Welcome to VitalVibe API"}


@app.post("/api/health-tips")
async def get_health_tips(day_description: DayDescription):
    """
    Generate personalized health tips based on user's day description
    """
    if not day_description.description or not day_description.description.strip():
        raise HTTPException(status_code=400, detail="Description cannot be empty")
    
    if not os.getenv("OPENAI_API_KEY"):
        raise HTTPException(
            status_code=500,
            detail="OpenAI API key not configured. Please set OPENAI_API_KEY in your environment."
        )
    
    try:
        # Create a prompt for OpenAI
        prompt = f"""The user is describing their day: "{day_description.description}"

Based on this description, provide 3-5 short, friendly, and practical health tips tailored to their specific situation. 
Keep each tip concise (one sentence), actionable, and encouraging. 
Format the response as a simple list without numbering or bullet points, just line breaks between tips.
Be empathetic and supportive in your tone."""

        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a friendly and knowledgeable health and wellness assistant. Provide practical, actionable health tips that are easy to follow."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200,
            temperature=0.7
        )
        
        tips = response.choices[0].message.content.strip()
        
        return {
            "tips": tips,
            "user_input": day_description.description
        }
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error generating health tips: {str(e)}"
        )

