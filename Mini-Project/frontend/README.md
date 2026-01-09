# Heritage Tourist Guide - Frontend

A beautiful, responsive Next.js frontend for the Heritage Tourist Guide application. This application provides an AI-powered conversational interface to explore the world's most magnificent ancient heritage sites.

## Features

- **Interactive Chat Interface**: Conversational UI to ask questions about heritage sites
- **City Showcase**: Browse through available heritage destinations
- **Real-time Responses**: Get instant, detailed information about ancient monuments
- **Heritage Site Badges**: Visual indicators showing mentioned cities and sites
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Beautiful UI**: Modern design with smooth animations and gradients
- **Suggested Questions**: Quick-start prompts to explore the guide

## Tech Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **Icons**: Lucide React
- **HTTP Client**: Axios
- **Fonts**: Google Fonts (Inter & Playfair Display)

## Prerequisites

- Node.js 18+ installed
- Backend API running on `http://localhost:8000`

## Installation

1. Navigate to the frontend directory:
   ```bash
   cd Mini-Project/frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Create environment file (already exists):
   ```bash
   # .env.local
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

## Running the Application

### Development Mode

```bash
npm run dev
```

The application will start on [http://localhost:3000](http://localhost:3000)

### Production Build

```bash
npm run build
npm start
```

## Project Structure

```
frontend/
├── src/
│   ├── app/
│   │   ├── globals.css          # Global styles and Tailwind config
│   │   ├── layout.tsx           # Root layout with fonts
│   │   └── page.tsx             # Main page with chat interface
│   ├── components/
│   │   ├── ChatMessage.tsx      # Chat message component
│   │   └── CitiesShowcase.tsx   # Cities grid component
│   └── services/
│       └── api.ts               # API service for backend communication
├── public/                      # Static assets
├── .env.local                   # Environment variables
├── package.json                 # Dependencies and scripts
├── tailwind.config.ts          # Tailwind configuration
└── tsconfig.json               # TypeScript configuration
```

## API Integration

The frontend connects to the backend API with these endpoints:

- `POST /tourist/ask` - Ask questions about heritage sites
- `GET /tourist/cities` - Get list of available cities
- `GET /tourist/health` - Health check

## Features in Detail

### Chat Interface
- User messages appear on the right with a user avatar
- Bot responses appear on the left with a bot avatar
- Messages show timestamps
- Loading indicator while waiting for responses

### Cities Showcase
- Grid layout of all available heritage cities
- Each card shows city name, country, and number of heritage sites
- Click on any city to automatically ask about its heritage sites
- Hover effects for better interactivity

### Responsive Design
- Mobile-first approach
- Adapts to different screen sizes
- Touch-friendly interface
- Optimized for all devices

### Visual Features
- Gradient backgrounds and buttons
- Smooth animations and transitions
- Custom scrollbar styling
- Badge system for cities and heritage sites
- Loading animations

## Example Queries

Try asking questions like:
- "Tell me about ancient heritage sites in Rome"
- "What can I visit in Athens?"
- "Best time to visit Machu Picchu?"
- "What are the must-see temples in Kyoto?"
- "Ancient monuments in Egypt"

## Customization

### Changing Colors

Edit `tailwind.config.ts` to customize the color scheme:

```typescript
colors: {
  primary: {
    // Your primary color shades
  },
  secondary: {
    // Your secondary color shades
  }
}
```

### Changing API URL

Update `.env.local`:

```bash
NEXT_PUBLIC_API_URL=https://your-api-url.com
```

## Troubleshooting

### Backend Connection Issues

If you see connection errors:
1. Make sure the backend is running on `http://localhost:8000`
2. Check CORS settings in the backend
3. Verify the API URL in `.env.local`

### Build Errors

If you encounter build errors:
1. Delete `node_modules` and `.next` folders
2. Run `npm install` again
3. Try `npm run build` again

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Performance

- Optimized bundle size with Next.js
- Image optimization
- Code splitting
- Fast page loads

## Contributing

Feel free to submit issues or pull requests to improve the application.

## License

This project is part of the AI Engineering Bootcamp assignments.
