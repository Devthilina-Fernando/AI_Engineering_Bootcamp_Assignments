from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # OpenAI
    openai_api_key: str
    
    # Email
    smtp_host: str = "smtp.gmail.com"
    smtp_port: int = 587
    smtp_username: str = ""
    smtp_password: str = ""
    
    # File handling
    max_file_size: int = 25  # MB
    allowed_audio_formats: str = "mp3,wav,m4a,webm"
    allowed_transcript_formats: str = "txt,pdf,docx"
    
    # CORS
    frontend_url: str = "http://localhost:3000"
    
    class Config:
        env_file = ".env"
        case_sensitive = False
    
    @property
    def audio_formats_list(self) -> List[str]:
        return [f.strip() for f in self.allowed_audio_formats.split(",")]
    
    @property
    def transcript_formats_list(self) -> List[str]:
        return [f.strip() for f in self.allowed_transcript_formats.split(",")]


settings = Settings()