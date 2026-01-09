'use client';

import { useState, useEffect, useRef } from 'react';
import { touristApi, weatherApi, CityInfo, WeatherData } from '@/services/api';
import ChatMessage, { Message } from '@/components/ChatMessage';
import CitiesShowcase from '@/components/CitiesShowcase';
import WeatherCard from '@/components/WeatherCard';
import { Send, Globe, Loader2, Compass, CloudRain, Plane } from 'lucide-react';

type AgentMode = 'tourist' | 'weather';

export default function Home() {
  const [agentMode, setAgentMode] = useState<AgentMode>('tourist');
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [cities, setCities] = useState<CityInfo[]>([]);
  const [showCities, setShowCities] = useState(true);
  const [weatherData, setWeatherData] = useState<WeatherData | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    loadCities();
    addWelcomeMessage(agentMode);
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  useEffect(() => {
    // Clear messages and add welcome message when switching agents
    setMessages([]);
    setShowCities(agentMode === 'tourist');
    setWeatherData(null);
    addWelcomeMessage(agentMode);
  }, [agentMode]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  const loadCities = async () => {
    try {
      const citiesData = await touristApi.getAvailableCities();
      setCities(citiesData);
    } catch (error) {
      console.error('Failed to load cities:', error);
    }
  };

  const addWelcomeMessage = (mode: AgentMode) => {
    const touristWelcome = `Welcome to the Heritage Tourist Guide! 🏛️

I'm your personal AI guide to the world's most magnificent ancient heritage sites and historical destinations. I have detailed knowledge about incredible places like Rome, Athens, Cairo, Istanbul, Kyoto, and many more!

Feel free to ask me about:
• Ancient monuments and heritage sites
• Best times to visit
• Historical significance and stories
• Practical travel tips
• Local recommendations

Click on any city below or ask me anything about these amazing destinations!`;

    const weatherWelcome = `Welcome to the Weather Information Agent! ☁️

I'm your AI weather assistant, here to help you plan your travels with accurate weather information. I can provide current weather conditions, historical data, and help you make informed decisions about when to visit your chosen destinations.

Feel free to ask me about:
• Current weather in any city
• Weather history and averages
• Temperature, humidity, and wind conditions
• Weather-related travel planning

Try asking: "What's the weather in London?" or "Show me weather history for Paris"`;

    const welcomeMessage: Message = {
      id: Date.now().toString(),
      type: 'bot',
      content: mode === 'tourist' ? touristWelcome : weatherWelcome,
      timestamp: new Date(),
    };
    setMessages([welcomeMessage]);
  };

  const handleCityClick = async (city: CityInfo) => {
    if (agentMode === 'tourist') {
      const query = `Tell me about the ancient heritage sites in ${city.city}`;
      setInputValue(query);
      handleSendMessage(query);
    } else {
      // For weather mode, fetch weather data
      try {
        setIsLoading(true);
        const weather = await weatherApi.getLatestWeather(city.city);
        setWeatherData(weather);

        const query = `What's the current weather in ${city.city}?`;
        setInputValue(query);
        handleSendMessage(query);
      } catch (error) {
        console.error('Failed to fetch weather:', error);
        const errorMessage: Message = {
          id: (Date.now() + 1).toString(),
          type: 'bot',
          content: `I couldn't fetch the weather data for ${city.city}. Let me try using the weather agent instead.`,
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, errorMessage]);
        handleSendMessage(`What's the weather in ${city.city}?`);
      } finally {
        setIsLoading(false);
      }
    }
  };

  const handleSendMessage = async (messageText?: string) => {
    const textToSend = messageText || inputValue.trim();
    if (!textToSend || isLoading) return;

    setShowCities(false);

    // Add user message
    const userMessage: Message = {
      id: Date.now().toString(),
      type: 'user',
      content: textToSend,
      timestamp: new Date(),
    };
    setMessages((prev) => [...prev, userMessage]);
    setInputValue('');
    setIsLoading(true);

    try {
      if (agentMode === 'tourist') {
        const response = await touristApi.askTouristGuide(textToSend);
        const botMessage: Message = {
          id: (Date.now() + 1).toString(),
          type: 'bot',
          content: response.response,
          cities_mentioned: response.cities_mentioned,
          heritage_sites_mentioned: response.heritage_sites_mentioned,
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, botMessage]);
      } else {
        const response = await weatherApi.askWeatherAgent(textToSend);
        const botMessage: Message = {
          id: (Date.now() + 1).toString(),
          type: 'bot',
          content: response.response,
          timestamp: new Date(),
        };
        setMessages((prev) => [...prev, botMessage]);
      }
    } catch (error) {
      console.error('Failed to get response:', error);
      const errorMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'bot',
        content: 'I apologize, but I encountered an error while processing your request. Please make sure the backend server is running and try again.',
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const touristQuestions = [
    "What are the must-see sites in Rome?",
    "Best time to visit Machu Picchu?",
    "Tell me about the Pyramids of Giza",
    "Ancient temples in Kyoto"
  ];

  const weatherQuestions = [
    "What's the weather in London?",
    "Show me weather in Cairo",
    "Current temperature in Tokyo?",
    "Weather conditions in Paris"
  ];

  const suggestedQuestions = agentMode === 'tourist' ? touristQuestions : weatherQuestions;

  return (
    <div className="min-h-screen bg-mesh-gradient">
      {/* Header */}
      <header className="bg-gradient-to-r from-primary-600 via-primary-500 to-secondary-500 shadow-xl sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div className="bg-white p-2 rounded-lg shadow-lg">
                <Globe className="text-primary-600" size={32} />
              </div>
              <div>
                <h1 className="text-2xl sm:text-3xl font-bold text-white font-serif">
                  Travel AI Assistant
                </h1>
                <p className="text-primary-100 text-sm">Heritage Guide & Weather Info</p>
              </div>
            </div>

            {/* Agent Mode Toggle */}
            <div className="flex bg-white/20 backdrop-blur-sm rounded-lg p-1 gap-1">
              <button
                onClick={() => setAgentMode('tourist')}
                className={`flex items-center gap-2 px-4 py-2 rounded-md font-semibold transition-all ${
                  agentMode === 'tourist'
                    ? 'bg-white text-primary-700 shadow-lg'
                    : 'text-white hover:bg-white/10'
                }`}
              >
                <Compass size={20} />
                <span className="hidden sm:inline">Tourist Guide</span>
              </button>
              <button
                onClick={() => setAgentMode('weather')}
                className={`flex items-center gap-2 px-4 py-2 rounded-md font-semibold transition-all ${
                  agentMode === 'weather'
                    ? 'bg-white text-primary-700 shadow-lg'
                    : 'text-white hover:bg-white/10'
                }`}
              >
                <CloudRain size={20} />
                <span className="hidden sm:inline">Weather Agent</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Cities Showcase */}
        {showCities && cities.length > 0 && (
          <div className="animate-slideUp mb-8">
            <CitiesShowcase cities={cities} onCityClick={handleCityClick} />
          </div>
        )}

        {/* Weather Card */}
        {weatherData && agentMode === 'weather' && (
          <div className="mb-8 animate-fadeIn">
            <WeatherCard weather={weatherData} />
          </div>
        )}

        {/* Chat Container */}
        <div className="card p-6 max-w-5xl mx-auto">
          {/* Agent Mode Indicator */}
          <div className="mb-4 flex items-center gap-2 text-sm text-gray-600">
            {agentMode === 'tourist' ? (
              <>
                <Plane size={16} className="text-primary-600" />
                <span>Tourist Guide Mode - Ask about heritage sites and travel tips</span>
              </>
            ) : (
              <>
                <CloudRain size={16} className="text-primary-600" />
                <span>Weather Agent Mode - Get weather information for any city</span>
              </>
            )}
          </div>

          <div className="flex flex-col h-[600px]">
            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto mb-4 pr-2">
              {messages.map((message) => (
                <ChatMessage key={message.id} message={message} />
              ))}

              {isLoading && (
                <div className="flex gap-3 mb-6">
                  <div className="flex-shrink-0 w-10 h-10 rounded-full bg-gradient-to-br from-primary-400 to-primary-600 flex items-center justify-center shadow-md">
                    <Loader2 className="text-white animate-spin" size={20} />
                  </div>
                  <div className="chat-bubble-bot">
                    <div className="flex gap-2">
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce"></div>
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.1s' }}></div>
                      <div className="w-2 h-2 bg-gray-400 rounded-full animate-bounce" style={{ animationDelay: '0.2s' }}></div>
                    </div>
                  </div>
                </div>
              )}

              <div ref={messagesEndRef} />
            </div>

            {/* Suggested Questions */}
            {messages.length <= 1 && !isLoading && (
              <div className="mb-4">
                <p className="text-sm text-gray-600 mb-2 font-medium">Suggested questions:</p>
                <div className="flex flex-wrap gap-2">
                  {suggestedQuestions.map((question, idx) => (
                    <button
                      key={idx}
                      onClick={() => {
                        setInputValue(question);
                        handleSendMessage(question);
                      }}
                      className="text-sm px-4 py-2 bg-primary-50 text-primary-700 rounded-full
                               hover:bg-primary-100 transition-colors border border-primary-200"
                    >
                      {question}
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Input Area */}
            <div className="flex gap-3">
              <input
                type="text"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
                onKeyDown={handleKeyDown}
                placeholder={agentMode === 'tourist' ? "Ask about heritage sites..." : "Ask about weather..."}
                disabled={isLoading}
                className="input-field flex-1"
              />
              <button
                onClick={() => handleSendMessage()}
                disabled={isLoading || !inputValue.trim()}
                className="btn-primary px-8 flex items-center gap-2"
              >
                <Send size={20} />
                <span className="hidden sm:inline">Send</span>
              </button>
            </div>
          </div>
        </div>

        {/* Toggle Cities Button */}
        {!showCities && agentMode === 'tourist' && (
          <div className="flex justify-center mt-6">
            <button
              onClick={() => setShowCities(true)}
              className="btn-secondary"
            >
              Show All Destinations
            </button>
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-gradient-to-r from-gray-800 to-gray-900 text-white py-8 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
            <div>
              <h3 className="font-bold text-lg mb-2">Tourist Guide</h3>
              <p className="text-sm text-gray-400">
                Explore 10 major heritage destinations with 30+ ancient sites
              </p>
            </div>
            <div>
              <h3 className="font-bold text-lg mb-2">Weather Agent</h3>
              <p className="text-sm text-gray-400">
                Get real-time weather data and historical information for trip planning
              </p>
            </div>
            <div>
              <h3 className="font-bold text-lg mb-2">Powered by AI</h3>
              <p className="text-sm text-gray-400">
                Using OpenAI GPT, FAISS vectorstore, and LangChain RAG
              </p>
            </div>
          </div>
          <div className="text-center text-sm text-gray-500 border-t border-gray-700 pt-6">
            Powered by AI • Explore heritage & plan with weather insights
          </div>
        </div>
      </footer>
    </div>
  );
}
