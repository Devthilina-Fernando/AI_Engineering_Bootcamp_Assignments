# System Architecture

## Overview Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        USER BROWSER                              │
│                     (http://localhost:3000)                      │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ HTTP/REST
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                      NEXT.JS FRONTEND                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  App Router (src/app/)                                   │   │
│  │  - page.tsx: Main chat interface                        │   │
│  │  - layout.tsx: Root layout                              │   │
│  │  - globals.css: Styling                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Components (src/components/)                            │   │
│  │  - ChatMessage: Message display                         │   │
│  │  - CitiesShowcase: City grid                            │   │
│  └─────────────────────────────────────────────────────────┘   │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Services (src/services/)                                │   │
│  │  - api.ts: Backend integration                          │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ Axios HTTP Requests
                             │ POST /tourist/ask
                             │ GET /tourist/cities
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                     FASTAPI BACKEND                              │
│                   (http://localhost:8000)                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Routes (app/routes/)                                    │   │
│  │  - tourist.py: Tourist endpoints                        │   │
│  │  - agent.py: Weather agent                              │   │
│  │  - weather.py: Weather data                             │   │
│  └─────────────────────────────────────────────────────────┘   │
│                             │                                    │
│                             ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Tourist Guide Service (app/services/tourist_guide.py)  │   │
│  │                                                          │   │
│  │  ┌──────────────────────────────────────────────────┐  │   │
│  │  │  Initialization Phase                             │  │   │
│  │  │  1. Load tourist_data.py                         │  │   │
│  │  │  2. Split into chunks (1000 chars)               │  │   │
│  │  │  3. Generate embeddings (OpenAI)                 │  │   │
│  │  │  4. Build FAISS index                            │  │   │
│  │  └──────────────────────────────────────────────────┘  │   │
│  │                                                          │   │
│  │  ┌──────────────────────────────────────────────────┐  │   │
│  │  │  Query Processing Phase                          │  │   │
│  │  │  1. Receive user query                           │  │   │
│  │  │  2. Convert query to embedding                   │  │   │
│  │  │  3. Search FAISS (top 4 similar chunks)         │  │   │
│  │  │  4. Build context from chunks                    │  │   │
│  │  │  5. Generate response via LLM                    │  │   │
│  │  └──────────────────────────────────────────────────┘  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                             │                                    │
│                             ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  FAISS Vectorstore (In-Memory)                          │   │
│  │  - ~100 document chunks                                 │   │
│  │  - OpenAI embeddings (1536 dimensions)                  │   │
│  │  - Similarity search with threshold                     │   │
│  └─────────────────────────────────────────────────────────┘   │
│                             │                                    │
│                             ▼                                    │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Tourist Data (app/data/tourist_data.py)                │   │
│  │  - 10 cities with metadata                              │   │
│  │  - 30+ heritage sites                                   │   │
│  │  - Historical information                               │   │
│  │  - Travel tips and recommendations                      │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────────┬────────────────────────────────────┘
                             │
                             │ API Calls
                             │
┌────────────────────────────▼────────────────────────────────────┐
│                      OPENAI API                                  │
│  - text-embedding-ada-002: Generate embeddings                  │
│  - gpt-4o-mini: Generate responses                              │
└──────────────────────────────────────────────────────────────────┘
```

## Request Flow

### Tourist Query Flow

```
1. User Types Query
   "Tell me about Rome"
   │
   ▼
2. Frontend (page.tsx)
   - Create user message
   - Display in chat
   - Set loading state
   │
   ▼
3. API Service (api.ts)
   - POST /tourist/ask
   - Body: { query: "Tell me about Rome" }
   │
   ▼
4. Backend Route (tourist.py)
   - Validate request
   - Call tourist_guide service
   │
   ▼
5. Tourist Guide Service (tourist_guide.py)
   - Convert query to embedding
   │
   ▼
6. FAISS Vector Search
   - Search for similar chunks
   - Return top 4 matches with metadata
   │
   ▼
7. RAG Chain (LangChain)
   - Combine chunks into context
   - Build prompt with instructions
   - Send to OpenAI
   │
   ▼
8. OpenAI (GPT-4o-mini)
   - Generate response using context
   - Temperature: 0.3 (factual)
   │
   ▼
9. Response Processing
   - Extract cities mentioned
   - Extract heritage sites mentioned
   - Count sources used
   │
   ▼
10. Return to Frontend
    - Response text
    - Metadata (cities, sites)
    │
    ▼
11. Display in Chat
    - Show bot message
    - Display badges for cities/sites
    - Add timestamp
```

## Data Flow Diagram

```
┌──────────────────┐
│  tourist_data.py │  Static heritage data
│  (10 cities)     │
└────────┬─────────┘
         │
         │ Load on startup
         ▼
┌────────────────────────────┐
│  Text Splitter             │  Chunk into smaller pieces
│  (RecursiveCharacterText)  │  1000 chars, 200 overlap
└────────┬───────────────────┘
         │
         │ ~100 chunks
         ▼
┌────────────────────────────┐
│  OpenAI Embeddings         │  Convert text to vectors
│  (text-embedding-ada-002)  │  1536 dimensions
└────────┬───────────────────┘
         │
         │ Vector representations
         ▼
┌────────────────────────────┐
│  FAISS Index               │  Store in memory
│  (IndexFlatL2)             │  Fast similarity search
└────────┬───────────────────┘
         │
         │ Ready for queries
         ▼
┌────────────────────────────┐
│  Query Processing          │  User questions
│  (Semantic Search)         │
└────────────────────────────┘
```

## Component Architecture

### Frontend Components

```
App (page.tsx)
├── Header
│   ├── Logo
│   └── Title
│
├── Cities Showcase (CitiesShowcase.tsx)
│   └── City Cards (grid)
│       ├── City Name
│       ├── Country
│       └── Sites Count
│
├── Chat Container
│   ├── Messages Area
│   │   ├── Chat Message (ChatMessage.tsx)
│   │   │   ├── Avatar
│   │   │   ├── Message Bubble
│   │   │   ├── Badges (cities/sites)
│   │   │   └── Timestamp
│   │   │
│   │   └── Loading Indicator
│   │
│   ├── Suggested Questions
│   │
│   └── Input Area
│       ├── Text Input
│       └── Send Button
│
└── Footer
```

### Backend Services

```
FastAPI App (main.py)
├── Routers
│   ├── Tourist Router (/tourist)
│   │   ├── POST /ask
│   │   ├── GET /cities
│   │   └── GET /health
│   │
│   ├── Agent Router (/agent)
│   └── Weather Router (/weather)
│
├── Services
│   ├── Tourist Guide Service
│   │   ├── FAISS Vectorstore
│   │   ├── OpenAI Embeddings
│   │   ├── LangChain RAG
│   │   └── Prompt Template
│   │
│   ├── Weather Agent Service
│   └── Weather API Service
│
└── Models (Pydantic)
    ├── TouristQueryRequest
    ├── TouristQueryResponse
    └── CityInfo
```

## Technology Stack

### Frontend Stack

```
┌──────────────────────────────┐
│      Next.js 14              │  React Framework
├──────────────────────────────┤
│      React 18                │  UI Library
├──────────────────────────────┤
│      TypeScript              │  Type Safety
├──────────────────────────────┤
│      Tailwind CSS            │  Styling
├──────────────────────────────┤
│      Lucide React            │  Icons
├──────────────────────────────┤
│      Axios                   │  HTTP Client
└──────────────────────────────┘
```

### Backend Stack

```
┌──────────────────────────────┐
│      FastAPI                 │  Web Framework
├──────────────────────────────┤
│      Python 3.11+            │  Language
├──────────────────────────────┤
│      LangChain               │  RAG Framework
├──────────────────────────────┤
│      FAISS                   │  Vector Database
├──────────────────────────────┤
│      OpenAI                  │  LLM & Embeddings
├──────────────────────────────┤
│      Pydantic                │  Data Validation
├──────────────────────────────┤
│      Uvicorn                 │  ASGI Server
└──────────────────────────────┘
```

## Database Schema (FAISS)

### Document Structure

```javascript
{
  "content": "City: Rome, Italy\n\nDescription: ...",
  "metadata": {
    "type": "city_overview" | "heritage_site",
    "city": "Rome",
    "country": "Italy",
    "site_name": "Colosseum" // only for heritage_site type
  },
  "embedding": [0.123, -0.456, ...] // 1536 dimensions
}
```

## API Contract

### POST /tourist/ask

**Request:**
```json
{
  "query": "Tell me about Rome"
}
```

**Response:**
```json
{
  "success": true,
  "response": "Rome, the Eternal City, is a living museum...",
  "cities_mentioned": ["Rome, Italy"],
  "heritage_sites_mentioned": ["Colosseum", "Roman Forum"],
  "sources_count": 4
}
```

### GET /tourist/cities

**Response:**
```json
[
  {
    "city": "Rome",
    "country": "Italy",
    "heritage_sites_count": 3
  },
  ...
]
```

## Security Considerations

```
┌─────────────────────────────────┐
│  Security Measures              │
├─────────────────────────────────┤
│  ✓ CORS configured              │
│  ✓ Environment variables        │
│  ✓ API key protection           │
│  ✓ Input validation (Pydantic)  │
│  ✓ Rate limiting (recommended)  │
│  ✓ HTTPS (production)           │
└─────────────────────────────────┘
```

## Performance Metrics

```
┌────────────────────────────────────┐
│  Component         │  Performance  │
├────────────────────┼───────────────┤
│  Vector Search     │  <100ms       │
│  OpenAI Embedding  │  ~500ms       │
│  OpenAI Response   │  1-2s         │
│  Total Backend     │  2-3s         │
│  Frontend Load     │  <1s          │
│  Memory Usage      │  ~500MB       │
└────────────────────────────────────┘
```

## Scalability Options

```
Current (Single Server)
┌───────────┐
│  Backend  │
│  + FAISS  │
└───────────┘

Option 1: Horizontal Scaling
┌───────────┐  ┌───────────┐
│  Backend  │  │  Backend  │
│  + FAISS  │  │  + FAISS  │
└─────┬─────┘  └─────┬─────┘
      │              │
      └──────┬───────┘
     ┌───────▼───────┐
     │ Load Balancer │
     └───────────────┘

Option 2: Shared Vector DB
┌───────────┐  ┌───────────┐
│  Backend  │  │  Backend  │
└─────┬─────┘  └─────┬─────┘
      │              │
      └──────┬───────┘
     ┌───────▼───────┐
     │   Pinecone    │
     │  or Weaviate  │
     └───────────────┘
```

## Deployment Architecture

```
┌─────────────────────────────────────────┐
│           PRODUCTION                     │
│                                          │
│  ┌────────────────┐  ┌────────────────┐│
│  │  Vercel        │  │  Railway/      ││
│  │  (Frontend)    │  │  Heroku        ││
│  │                │  │  (Backend)     ││
│  │  CDN + Edge    │  │  + FAISS       ││
│  └────────┬───────┘  └───────┬────────┘│
│           │                   │          │
│           └─────────┬─────────┘          │
│                     │                    │
│           ┌─────────▼─────────┐          │
│           │   OpenAI API      │          │
│           └───────────────────┘          │
└─────────────────────────────────────────┘
```

---

This architecture is designed for:
- ✅ Fast response times
- ✅ Scalability
- ✅ Maintainability
- ✅ Easy deployment
- ✅ Cost effectiveness
