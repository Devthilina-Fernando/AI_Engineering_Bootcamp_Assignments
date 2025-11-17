# Weather Chatbot 🌤️

An AI-powered weather forecast chatbot that uses Tavily API for web search, OpenAI for intelligent responses, and DALL-E for weather visualization.

## Features

- 🤖 AI-powered conversational weather assistant
- 🔍 Real-time weather data using Tavily API
- 🎨 Beautiful weather visualizations using OpenAI DALL-E
- 💬 Modern chat interface built with Next.js
- 🚀 Fast API backend with FastAPI

## Project Structure

```
weather-chatbot/
├── backend/          # FastAPI backend
│   ├── main.py      # Main API server
│   └── requirements.txt
└── frontend/        # Next.js frontend
    ├── app/         # Next.js app directory
    └── package.json
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
```bash
cd weather-chatbot/backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory:
```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

5. Run the backend server:
```bash
uvicorn main:app --reload --port 8000
```

The API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd weather-chatbot/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Run the development server:
```bash
npm run dev
```

The app will be available at `http://localhost:3000`

## API Keys Required

1. **OpenAI API Key**: Get it from [OpenAI Platform](https://platform.openai.com/api-keys)
   - Used for LLM responses and DALL-E image generation

2. **Tavily API Key**: Get it from [Tavily](https://tavily.com)
   - Used for real-time weather data search

## Usage

1. Start both the backend and frontend servers
2. Open `http://localhost:3000` in your browser
3. Ask questions like:
   - "What's the weather in New York?"
   - "Will it rain in London tomorrow?"
   - "How's the weather in Tokyo this week?"

The chatbot will:
- Search for current weather information using Tavily
- Generate intelligent responses using OpenAI
- Create beautiful weather visualizations using DALL-E

## Technologies Used

- **Backend**: FastAPI, Python, OpenAI API, Tavily API
- **Frontend**: Next.js, React, TypeScript, CSS Modules
- **AI**: OpenAI GPT-4, DALL-E 3

