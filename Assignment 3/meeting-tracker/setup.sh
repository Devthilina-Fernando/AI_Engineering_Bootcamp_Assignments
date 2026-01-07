#!/bin/bash

echo "🚀 Meeting Action Tracker - Setup Script"
echo "========================================"
echo ""

# Check if required tools are installed
command -v python3 >/dev/null 2>&1 || { echo "❌ Python 3 is required but not installed. Aborting." >&2; exit 1; }
command -v node >/dev/null 2>&1 || { echo "❌ Node.js is required but not installed. Aborting." >&2; exit 1; }

echo "✅ Prerequisites check passed"
echo ""

# Backend Setup
echo "📦 Setting up Backend..."
cd backend

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing backend dependencies..."
pip install -r requirements.txt

# Create .env if it doesn't exist
if [ ! -f ".env" ]; then
    echo "Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit backend/.env and add your OpenAI API key"
fi

cd ..

# Frontend Setup
echo ""
echo "📦 Setting up Frontend..."
cd frontend

# Install dependencies
echo "Installing frontend dependencies..."
npm install

# Create .env.local if it doesn't exist
if [ ! -f ".env.local" ]; then
    echo "Creating .env.local file from template..."
    cp .env.local.example .env.local
fi

cd ..

echo ""
echo "✅ Setup complete!"
echo ""
echo "📝 Next steps:"
echo "1. Edit backend/.env and add your OpenAI API key"
echo "2. (Optional) Configure email settings in backend/.env"
echo ""
echo "🚀 To start the application:"
echo ""
echo "Terminal 1 - Backend:"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  uvicorn app.main:app --reload"
echo ""
echo "Terminal 2 - Frontend:"
echo "  cd frontend"
echo "  npm run dev"
echo ""
echo "Then visit http://localhost:3000"
echo ""