# Heritage Tourist Guide - Full Stack Application

An AI-powered tourist guide application that helps travelers explore the world's most magnificent ancient heritage sites. Built with FastAPI backend and Next.js frontend.

## Overview

This full-stack application provides an interactive conversational interface where users can ask questions about ancient heritage sites and historical destinations. The system uses FAISS in-memory vectorstore with RAG (Retrieval Augmented Generation) to provide accurate, context-based responses about 10 major heritage destinations worldwide.

## Features

### Backend
- **FAISS Vectorstore**: In-memory semantic search for fast retrieval
- **RAG Implementation**: LangChain-powered retrieval augmented generation
- **OpenAI Integration**: GPT-4o-mini for natural language responses
- **FastAPI**: Modern, fast web framework
- **Weather Integration**: Existing weather agent functionality
- **Comprehensive Data**: 10 cities with 30+ heritage sites

### Frontend
- **Interactive Chat Interface**: Beautiful conversational UI
- **City Showcase**: Browse heritage destinations visually
- **Real-time Responses**: Instant AI-powered answers
- **Responsive Design**: Works on all devices
- **Modern UI**: Smooth animations and gradients

## Architecture

```
Mini-Project/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── data/
│   │   │   └── tourist_data.py    # Heritage sites database
│   │   ├── routes/
│   │   │   ├── weather.py         # Weather endpoints
│   │   │   ├── agent.py           # Weather agent endpoints
│   │   │   └── tourist.py         # Tourist guide endpoints
│   │   ├── services/
│   │   │   ├── weather_agent.py   # Weather AI agent
│   │   │   └── tourist_guide.py   # Tourist guide service
│   │   ├── models.py              # Pydantic models
│   │   ├── config.py              # Configuration
│   │   └── main.py                # FastAPI application
│   └── requirements.txt
│
└── frontend/                   # Next.js Frontend
    ├── src/
    │   ├── app/
    │   │   ├── page.tsx           # Main page
    │   │   ├── layout.tsx         # Root layout
    │   │   └── globals.css        # Global styles
    │   ├── components/
    │   │   ├── ChatMessage.tsx    # Chat component
    │   │   └── CitiesShowcase.tsx # Cities grid
    │   └── services/
    │       └── api.ts             # API integration
    ├── package.json
    └── tailwind.config.ts
```

## Heritage Destinations Covered

1. **Rome, Italy** - Colosseum, Roman Forum, Pantheon
2. **Athens, Greece** - Acropolis, Ancient Agora, Temple of Zeus
3. **Cairo, Egypt** - Pyramids of Giza, Egyptian Museum, Saqqara
4. **Istanbul, Turkey** - Hagia Sophia, Blue Mosque, Topkapi Palace
5. **Kyoto, Japan** - Fushimi Inari, Golden Pavilion, Kiyomizu-dera
6. **Cusco, Peru** - Machu Picchu, Sacsayhuamán, Qorikancha
7. **Jerusalem, Israel** - Old City, Western Wall, Church of Holy Sepulchre
8. **Siem Reap, Cambodia** - Angkor Wat, Bayon Temple, Ta Prohm
9. **Petra, Jordan** - The Treasury, The Monastery, Royal Tombs
10. **Delhi, India** - Red Fort, Qutub Minar, Humayun's Tomb

## Tech Stack

### Backend
- Python 3.11+
- FastAPI
- LangChain
- OpenAI API (GPT-4o-mini)
- FAISS (CPU)
- Pydantic
- Uvicorn

### Frontend
- Next.js 14
- TypeScript
- React 18
- Tailwind CSS
- Axios
- Lucide React (Icons)

## Prerequisites

- Python 3.11 or higher
- Node.js 18 or higher
- OpenAI API key
- Git

## Installation & Setup

### 1. Clone the Repository

```bash
cd Mini-Project
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
# Add your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install

# Environment is already configured in .env.local
# NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Running the Application

### Start Backend

```bash
cd backend
python -m app.main
```

Backend will run on: `http://localhost:8000`

### Start Frontend

```bash
cd frontend
npm run dev
```

Frontend will run on: `http://localhost:3000`

### Access the Application

Open your browser and navigate to: `http://localhost:3000`

## API Endpoints

### Tourist Guide Endpoints

- `POST /tourist/ask` - Ask questions about heritage sites
  ```json
  {
    "query": "Tell me about ancient sites in Rome"
  }
  ```

- `GET /tourist/cities` - Get list of available cities

- `GET /tourist/health` - Health check for tourist guide service

### Weather Endpoints (Existing)

- `POST /agent/query` - Ask weather-related questions
- `GET /weather/latest/{city}` - Get latest weather data
- `GET /agent/health` - Health check for weather agent

## Example Queries

Try asking the tourist guide:

- "Tell me about the Colosseum in Rome"
- "What are the best heritage sites to visit in Athens?"
- "When is the best time to visit Machu Picchu?"
- "What should I know before visiting the Pyramids?"
- "Tell me about ancient temples in Kyoto"
- "Which sites can I visit in Petra?"

## How It Works

1. **User Query**: User asks a question about a heritage site or city
2. **Vector Search**: FAISS searches the knowledge base for relevant information
3. **Context Retrieval**: Top 4 most relevant document chunks are retrieved
4. **RAG Response**: OpenAI generates a response using only the retrieved context
5. **Display**: Frontend shows the response with mentioned cities and sites

## Key Features

### Knowledge Base Constraints
- Responses are based ONLY on the vectorstore data
- No hallucination - if data isn't in the knowledge base, bot says so
- Lower temperature (0.3) for factual responses
- Similarity threshold ensures relevant retrieval

### Rich Information
Each destination includes:
- Historical context and significance
- Best time to visit
- Practical travel tips
- Local recommendations
- Detailed descriptions of heritage sites

## Configuration

### Backend Configuration

Edit `backend/app/config.py` or `.env`:
```env
OPENAI_API_KEY=your_key_here
GOOGLE_APPLICATION_CREDENTIALS=path/to/credentials.json
OPENWEATHERMAP_API_KEY=your_weather_key
```

### Frontend Configuration

Edit `frontend/.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Development

### Adding New Cities

1. Edit `backend/app/data/tourist_data.py`
2. Add new city data following the existing structure
3. Restart backend - FAISS will reinitialize automatically

### Customizing UI

1. Edit colors in `frontend/tailwind.config.ts`
2. Modify components in `frontend/src/components/`
3. Update styles in `frontend/src/app/globals.css`

## Production Deployment

### Backend

```bash
cd backend
pip install gunicorn
gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend

```bash
cd frontend
npm run build
npm start
```

Or deploy to Vercel:
```bash
vercel deploy
```

## Troubleshooting

### Backend Issues

**Import errors:**
```bash
pip install --upgrade -r requirements.txt
```

**FAISS initialization fails:**
- Check OpenAI API key is set
- Verify internet connection for embeddings

### Frontend Issues

**Cannot connect to backend:**
- Verify backend is running on port 8000
- Check CORS settings in backend
- Verify API URL in `.env.local`

**Build errors:**
```bash
rm -rf node_modules .next
npm install
npm run build
```

## Performance

- FAISS provides fast semantic search (<100ms)
- Response generation typically takes 2-3 seconds
- Frontend optimized with Next.js code splitting
- Supports concurrent users

## Future Enhancements

- [ ] Add more cities and heritage sites
- [ ] Include images of heritage sites
- [ ] Add multi-language support
- [ ] Implement user authentication
- [ ] Add favorite destinations feature
- [ ] Include weather integration for travel planning
- [ ] Add maps and location services
- [ ] Create mobile apps (React Native)

## Contributing

This project is part of the AI Engineering Bootcamp. Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Add more heritage sites

## License

Educational project for AI Engineering Bootcamp

## Acknowledgments

- OpenAI for GPT models
- LangChain for RAG framework
- FAISS for vector search
- FastAPI and Next.js communities

## Support

For issues or questions:
1. Check the README files in backend and frontend folders
2. Review the troubleshooting section
3. Check API documentation at `http://localhost:8000/docs`

---

**Built with ❤️ for heritage enthusiasts and travelers worldwide**
