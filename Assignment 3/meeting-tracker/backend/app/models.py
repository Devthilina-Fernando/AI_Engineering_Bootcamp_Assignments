from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime


class ActionItem(BaseModel):
    """Single action item from meeting"""
    owner: str = Field(..., description="Person responsible for the task")
    task: str = Field(..., description="Description of the task to be completed")
    priority: Optional[str] = Field(None, description="Priority level: high, medium, low")
    deadline: Optional[str] = Field(None, description="Deadline for task completion")


class MeetingActions(BaseModel):
    """Collection of action items from a meeting"""
    actions: List[ActionItem]
    meeting_title: Optional[str] = None
    meeting_date: Optional[str] = None
    summary: Optional[str] = None


class TranscriptUploadResponse(BaseModel):
    """Response after processing transcript"""
    success: bool
    message: str
    actions: List[ActionItem]
    meeting_info: dict
    processing_time: float


class EmailRequest(BaseModel):
    """Request to email action items"""
    recipients: List[EmailStr] = Field(..., min_items=1, description="List of email addresses")
    actions: List[ActionItem]
    meeting_title: Optional[str] = None
    meeting_date: Optional[str] = None
    subject: Optional[str] = "Meeting Action Items"


class EmailResponse(BaseModel):
    """Response after sending emails"""
    success: bool
    message: str
    sent_to: List[str]