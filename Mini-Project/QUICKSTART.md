# Quick Start Guide

Get the Heritage Tourist Guide running in 5 minutes!

## Prerequisites Check

Before starting, make sure you have:
- ✅ Python 3.11+ installed (`python --version`)
- ✅ Node.js 18+ installed (`node --version`)
- ✅ OpenAI API key ready
- ✅ Terminal/Command Prompt open

## Step 1: Backend Setup (2 minutes)

```bash
# Navigate to backend
cd Mini-Project/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies (this may take a minute)
pip install -r requirements.txt

# Create .env file with your OpenAI API key
# Windows:
echo OPENAI_API_KEY=your_key_here > .env
# Mac/Linux:
echo "OPENAI_API_KEY=your_key_here" > .env

# Replace 'your_key_here' with your actual OpenAI API key
```

## Step 2: Start Backend (30 seconds)

```bash
# Make sure you're in the backend directory
python -m app.main
```

You should see:
```
INFO:     Started server process
INFO:     Application startup complete
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ Backend is running! Keep this terminal open.

## Step 3: Frontend Setup (2 minutes)

Open a **NEW** terminal window:

```bash
# Navigate to frontend
cd Mini-Project/frontend

# Install dependencies
npm install
```

## Step 4: Start Frontend (30 seconds)

```bash
# Make sure you're in the frontend directory
npm run dev
```

You should see:
```
- ready started server on 0.0.0.0:3000
- Local:        http://localhost:3000
```

✅ Frontend is running!

## Step 5: Open the Application

Open your browser and go to:
```
http://localhost:3000
```

## Quick Test

Try these queries to test the application:

1. Click on "Rome" in the cities showcase
2. Or type: "Tell me about ancient sites in Athens"
3. Or ask: "Best time to visit Machu Picchu?"

## You Should See:

1. A beautiful interface with a gradient header
2. City cards showing all available destinations
3. A chat interface at the bottom
4. The bot responding with detailed heritage site information

## Troubleshooting

### Backend won't start?

**Check 1:** Is your OpenAI API key set correctly?
```bash
# Windows
echo %OPENAI_API_KEY%
# Mac/Linux
echo $OPENAI_API_KEY
```

**Check 2:** Are all dependencies installed?
```bash
pip list | grep langchain
pip list | grep faiss
```

**Check 3:** Python version?
```bash
python --version
# Should be 3.11 or higher
```

### Frontend won't start?

**Check 1:** Node version?
```bash
node --version
# Should be 18 or higher
```

**Check 2:** Dependencies installed?
```bash
npm list next
```

**Check 3:** Backend running?
```bash
# Try accessing
curl http://localhost:8000/tourist/health
```

### Connection Error?

Make sure:
1. Backend is running on port 8000
2. Frontend is running on port 3000
3. No firewall blocking localhost connections
4. Check `.env.local` in frontend has: `NEXT_PUBLIC_API_URL=http://localhost:8000`

## API Documentation

Once backend is running, visit:
```
http://localhost:8000/docs
```

This shows interactive API documentation (Swagger UI).

## Stopping the Application

**Stop Backend:**
- Press `Ctrl + C` in the backend terminal

**Stop Frontend:**
- Press `Ctrl + C` in the frontend terminal

## Next Steps

1. ✅ Application is running
2. 📖 Read the main [README.md](README.md) for detailed documentation
3. 🎨 Explore the [frontend README](frontend/README.md) for UI customization
4. 🔧 Check [backend README](backend/README.md) for API details
5. 🌍 Ask questions about heritage sites!

## Available Commands

### Backend
```bash
# Start server
python -m app.main

# Run tests (if you add them)
pytest

# Check code
python -m app.main --help
```

### Frontend
```bash
# Development
npm run dev

# Production build
npm run build
npm start

# Linting
npm run lint
```

## Ports Summary

- **Backend**: http://localhost:8000
- **Frontend**: http://localhost:3000
- **API Docs**: http://localhost:8000/docs

## Getting Help

1. Check error messages carefully
2. Review the troubleshooting sections
3. Make sure both backend and frontend are running
4. Check browser console for frontend errors
5. Check terminal for backend errors

---

**Enjoy exploring the world's ancient heritage sites! 🌍✨**
