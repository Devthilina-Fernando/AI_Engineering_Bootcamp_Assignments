# Weather Chatbot Backend

FastAPI backend for the weather chatbot application.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

3. Run the server:
```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

## API Endpoints

- `GET /` - Health check
- `POST /api/chat` - Chat endpoint that accepts:
  - `message`: User's message
  - `conversation_history`: Optional list of previous messages

