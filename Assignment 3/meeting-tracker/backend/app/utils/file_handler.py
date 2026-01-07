import aiofiles
import os
from pathlib import Path
from typing import Optional
from fastapi import UploadFile, HTTPException
from app.config import settings


class FileHandler:
    """Utility class for handling file uploads and processing"""
    
    UPLOAD_DIR = Path("/tmp/meeting-tracker-uploads")
    
    @classmethod
    def setup(cls):
        """Create upload directory if it doesn't exist"""
        cls.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def validate_file_size(file: UploadFile) -> bool:
        """
        Validate file size
        
        Args:
            file: Uploaded file
            
        Returns:
            True if valid, raises HTTPException otherwise
        """
        # Note: file.size might be None for some files
        # We'll check during actual reading
        return True
    
    @staticmethod
    def get_file_extension(filename: str) -> str:
        """Get file extension without dot"""
        return Path(filename).suffix.lstrip('.').lower()
    
    @staticmethod
    def is_audio_file(filename: str) -> bool:
        """Check if file is an audio file"""
        ext = FileHandler.get_file_extension(filename)
        return ext in settings.audio_formats_list
    
    @staticmethod
    def is_transcript_file(filename: str) -> bool:
        """Check if file is a transcript file"""
        ext = FileHandler.get_file_extension(filename)
        return ext in settings.transcript_formats_list
    
    @classmethod
    async def save_upload(cls, file: UploadFile) -> str:
        """
        Save uploaded file to temporary directory
        
        Args:
            file: Uploaded file
            
        Returns:
            Path to saved file
        """
        cls.setup()
        
        # Generate unique filename
        filename = f"{os.urandom(16).hex()}_{file.filename}"
        file_path = cls.UPLOAD_DIR / filename
        
        # Save file
        try:
            async with aiofiles.open(file_path, 'wb') as f:
                content = await file.read()
                
                # Check file size
                size_mb = len(content) / (1024 * 1024)
                if size_mb > settings.max_file_size:
                    raise HTTPException(
                        status_code=413,
                        detail=f"File too large. Maximum size is {settings.max_file_size}MB"
                    )
                
                await f.write(content)
            
            return str(file_path)
            
        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to save file: {str(e)}"
            )
    
    @classmethod
    async def read_text_file(cls, file_path: str) -> str:
        """
        Read text content from file
        
        Args:
            file_path: Path to file
            
        Returns:
            Text content
        """
        try:
            async with aiofiles.open(file_path, 'r', encoding='utf-8') as f:
                content = await f.read()
            return content
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to read file: {str(e)}"
            )
    
    @classmethod
    def cleanup_file(cls, file_path: str):
        """
        Remove file from filesystem
        
        Args:
            file_path: Path to file to remove
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except Exception:
            pass  # Silent fail for cleanup


# Initialize upload directory on module import
FileHandler.setup()