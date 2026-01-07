import openai
import json
import time
from typing import Dict, Any
from app.config import settings
from app.models import MeetingActions, ActionItem

# Configure OpenAI
openai.api_key = settings.openai_api_key


class TranscriptProcessor:
    """Service to process meeting transcripts using OpenAI"""
    
    SYSTEM_PROMPT = """You are an expert meeting analyzer. Your task is to extract action items from meeting transcripts.

For each action item, identify:
1. Owner: The person responsible (name or role)
2. Task: Clear description of what needs to be done
3. Priority: high, medium, or low (if mentioned or implied)
4. Deadline: Any mentioned deadline or timeframe

Also extract:
- Meeting title (if mentioned)
- Meeting date (if mentioned)
- Brief summary of the meeting (2-3 sentences)

Return a JSON object with this exact structure:
{
    "meeting_title": "string or null",
    "meeting_date": "string or null",
    "summary": "string or null",
    "actions": [
        {
            "owner": "string",
            "task": "string",
            "priority": "string or null",
            "deadline": "string or null"
        }
    ]
}

If no action items are found, return an empty actions array.
Be thorough and extract all actionable items, including implicit ones."""

    @staticmethod
    async def process_transcript(transcript_text: str) -> Dict[str, Any]:
        """
        Process transcript and extract action items using OpenAI
        
        Args:
            transcript_text: The meeting transcript text
            
        Returns:
            Dictionary containing extracted actions and meeting info
        """
        start_time = time.time()
        
        try:
            # Call OpenAI API
            response = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": TranscriptProcessor.SYSTEM_PROMPT},
                    {"role": "user", "content": f"Analyze this meeting transcript and extract action items:\n\n{transcript_text}"}
                ],
                response_format={"type": "json_object"},
                temperature=0.3,
                max_tokens=2000
            )
            
            # Parse response
            result = json.loads(response.choices[0].message.content)
            
            # Validate and structure the response
            meeting_actions = MeetingActions(
                meeting_title=result.get("meeting_title"),
                meeting_date=result.get("meeting_date"),
                summary=result.get("summary"),
                actions=[ActionItem(**action) for action in result.get("actions", [])]
            )
            
            processing_time = time.time() - start_time
            
            return {
                "success": True,
                "meeting_info": {
                    "title": meeting_actions.meeting_title,
                    "date": meeting_actions.meeting_date,
                    "summary": meeting_actions.summary
                },
                "actions": [action.model_dump() for action in meeting_actions.actions],
                "processing_time": round(processing_time, 2)
            }
            
        except Exception as e:
            return {
                "success": False,
                "error": str(e),
                "meeting_info": {},
                "actions": [],
                "processing_time": time.time() - start_time
            }

    @staticmethod
    async def transcribe_audio(audio_file_path: str) -> str:
        """
        Transcribe audio file using OpenAI Whisper
        
        Args:
            audio_file_path: Path to the audio file
            
        Returns:
            Transcribed text
        """
        try:
            with open(audio_file_path, "rb") as audio_file:
                transcript = openai.audio.transcriptions.create(
                    model="whisper-1",
                    file=audio_file,
                    response_format="text"
                )
            return transcript
        except Exception as e:
            raise Exception(f"Error transcribing audio: {str(e)}")