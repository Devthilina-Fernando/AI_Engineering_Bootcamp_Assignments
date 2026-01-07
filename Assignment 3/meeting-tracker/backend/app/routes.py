from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from typing import List, Optional
from app.models import (
    TranscriptUploadResponse,
    EmailRequest,
    EmailResponse,
    ActionItem
)
from app.services.openai_service import TranscriptProcessor
from app.services.email_service import EmailService
from app.utils.file_handler import FileHandler
import json

router = APIRouter()


@router.post("/upload/transcript", response_model=TranscriptUploadResponse)
async def upload_transcript(file: UploadFile = File(...)):
    """
    Upload a meeting transcript file and extract action items
    
    Supported formats: txt, pdf, docx
    """
    # Validate file type
    if not FileHandler.is_transcript_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Supported formats: txt"
        )
    
    file_path = None
    try:
        # Save uploaded file
        file_path = await FileHandler.save_upload(file)
        
        # Read transcript content
        transcript_text = await FileHandler.read_text_file(file_path)
        
        if not transcript_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Transcript file is empty"
            )
        
        # Process transcript with OpenAI
        result = await TranscriptProcessor.process_transcript(transcript_text)
        
        if not result["success"]:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to process transcript: {result.get('error', 'Unknown error')}"
            )
        
        return TranscriptUploadResponse(
            success=True,
            message=f"Successfully extracted {len(result['actions'])} action items",
            actions=result["actions"],
            meeting_info=result["meeting_info"],
            processing_time=result["processing_time"]
        )
        
    finally:
        # Cleanup
        if file_path:
            FileHandler.cleanup_file(file_path)


@router.post("/upload/audio", response_model=TranscriptUploadResponse)
async def upload_audio(file: UploadFile = File(...)):
    """
    Upload an audio file, transcribe it, and extract action items
    
    Supported formats: mp3, wav, m4a, webm
    """
    # Validate file type
    if not FileHandler.is_audio_file(file.filename):
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Supported formats: mp3, wav, m4a, webm"
        )
    
    file_path = None
    try:
        # Save uploaded file
        file_path = await FileHandler.save_upload(file)
        
        # Transcribe audio
        transcript_text = await TranscriptProcessor.transcribe_audio(file_path)
        
        if not transcript_text.strip():
            raise HTTPException(
                status_code=400,
                detail="Transcription resulted in empty text"
            )
        
        # Process transcript with OpenAI
        result = await TranscriptProcessor.process_transcript(transcript_text)
        
        if not result["success"]:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to process transcript: {result.get('error', 'Unknown error')}"
            )
        
        return TranscriptUploadResponse(
            success=True,
            message=f"Successfully transcribed and extracted {len(result['actions'])} action items",
            actions=result["actions"],
            meeting_info=result["meeting_info"],
            processing_time=result["processing_time"]
        )
        
    finally:
        # Cleanup
        if file_path:
            FileHandler.cleanup_file(file_path)


@router.post("/email/send", response_model=EmailResponse)
async def send_action_items_email(request: EmailRequest):
    """
    Send action items to specified email addresses
    """
    try:
        # Create HTML email content
        html_content = EmailService.create_html_email(
            actions=request.actions,
            meeting_title=request.meeting_title,
            meeting_date=request.meeting_date
        )
        
        # Send email
        result = await EmailService.send_email(
            recipients=request.recipients,
            subject=request.subject,
            html_content=html_content
        )
        
        if not result["success"]:
            raise HTTPException(
                status_code=500,
                detail=result["message"]
            )
        
        return EmailResponse(
            success=True,
            message=result["message"],
            sent_to=result["sent_to"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Failed to send email: {str(e)}"
        )


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Meeting Action Tracker API"
    }