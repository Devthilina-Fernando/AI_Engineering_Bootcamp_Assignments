from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import router
from app.config import settings

# Create FastAPI application
app = FastAPI(
    title="Meeting Action Tracker API",
    description="Extract and manage action items from meeting transcripts and audio",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(router, prefix="/api", tags=["Meeting Actions"])


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Meeting Action Tracker API",
        "version": "1.0.0",
        "docs": "/docs"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)