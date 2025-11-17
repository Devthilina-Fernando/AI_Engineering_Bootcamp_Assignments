# ✨ VitalVibe - Your Daily Health Companion

VitalVibe is a beautiful, AI-powered health tips application that provides personalized wellness advice based on your daily routine. Simply describe your day, and get tailored health tips powered by OpenAI.

## 🌟 Features

- **Personalized Health Tips**: Get customized health advice based on your daily activities
- **Beautiful Modern UI**: Clean, responsive design with smooth animations
- **Fast & Efficient**: Single API call to OpenAI for quick responses
- **User-Friendly**: Simple one-line or paragraph input about your day

## 🏗️ Architecture

- **Backend**: FastAPI (Python) - RESTful API with OpenAI integration
- **Frontend**: Next.js 14 (TypeScript) - Modern React framework with App Router
- **AI**: OpenAI GPT-3.5 Turbo for generating health tips

## 📋 Prerequisites

- Python 3.8+ 
- Node.js 18+ and npm
- OpenAI API Key ([Get one here](https://platform.openai.com/api-keys))

## 🚀 Quick Start

### Backend Setup

1. Navigate to the backend directory:
```bash
cd vitalvibe/backend
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
```

3. Activate the virtual environment:
   - **Windows**: `venv\Scripts\activate`
   - **macOS/Linux**: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create a `.env` file from the example:
```bash
copy env.example .env  # Windows
# or
cp env.example .env    # macOS/Linux
```

6. Add your OpenAI API key to `.env`:
```
OPENAI_API_KEY=your_actual_api_key_here
```

7. Run the FastAPI server:
```bash
uvicorn main:app --reload --port 8000
```

The backend will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory (in a new terminal):
```bash
cd vitalvibe/frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create a `.env.local` file from the example:
```bash
copy env.local.example .env.local  # Windows
# or
cp env.local.example .env.local    # macOS/Linux
```

4. Update `.env.local` if your backend runs on a different port:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

5. Run the development server:
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## 📖 Usage

1. Open your browser and navigate to `http://localhost:3000`
2. Type a description of your day in the text area (e.g., "busy meetings today, skipped breakfast, feeling tired")
3. Click "Get Health Tips"
4. Receive personalized health tips tailored to your day!

## 🎨 Example Inputs

- "Busy meetings all day, skipped breakfast, feeling tired"
- "Had a stressful day at work, didn't exercise, ate fast food"
- "Feeling great today, went for a run, had a healthy lunch"
- "Long day, lots of screen time, feeling drained"

## 🔧 Configuration

### Backend Configuration

- **Port**: Default is 8000. Change in the uvicorn command
- **OpenAI Model**: Currently using `gpt-3.5-turbo`. Can be changed in `main.py`
- **CORS**: Configured for `localhost:3000`. Update in `main.py` if needed

### Frontend Configuration

- **API URL**: Set in `.env.local` as `NEXT_PUBLIC_API_URL`
- **Port**: Default is 3000. Change in `package.json` scripts

## 📁 Project Structure

```
vitalvibe/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── requirements.txt     # Python dependencies
│   ├── env.example          # Environment variables template
│   └── .env                 # Your environment variables (create this)
│
├── frontend/
│   ├── app/
│   │   ├── layout.tsx       # Root layout
│   │   ├── page.tsx         # Main page component
│   │   ├── page.module.css  # Page styles
│   │   └── globals.css      # Global styles
│   ├── package.json         # Node dependencies
│   ├── tsconfig.json        # TypeScript configuration
│   ├── next.config.js       # Next.js configuration
│   ├── env.local.example    # Frontend environment variables template
│   └── .env.local           # Frontend environment variables (create this)
│
└── README.md                # This file
```

## 🛠️ Development

### Backend Development

- The FastAPI server runs with auto-reload enabled
- API documentation available at `http://localhost:8000/docs`
- Interactive API testing at `http://localhost:8000/redoc`

### Frontend Development

- Next.js hot-reload is enabled by default
- TypeScript for type safety
- CSS Modules for component styling

## 🚢 Production Deployment

### Backend

1. Use a production ASGI server like Gunicorn with Uvicorn workers:
```bash
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker
```

2. Set up proper environment variables on your hosting platform
3. Configure CORS for your production domain

### Frontend

1. Build the production bundle:
```bash
npm run build
```

2. Start the production server:
```bash
npm start
```

Or deploy to platforms like Vercel, Netlify, or any Node.js hosting service.

## 🔒 Security Notes

- Never commit `.env` or `.env.local` files to version control
- Keep your OpenAI API key secure
- In production, use environment variables provided by your hosting platform
- Consider rate limiting for production use

## 📝 License

This project is open source and available for personal and educational use.

## 🤝 Contributing

Feel free to fork, modify, and use this project for your own purposes!

## 💡 Tips

- Be descriptive in your day description for better tips
- The app works best with honest, detailed descriptions
- Tips are generated fresh each time, so you can ask multiple times per day

---

Made with ❤️ for your wellness journey

