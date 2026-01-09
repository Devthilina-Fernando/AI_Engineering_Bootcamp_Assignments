'use client';

import { useState, useEffect, useRef } from 'react';
import { touristApi, CityInfo } from '@/services/api';
import ChatMessage, { Message } from '@/components/ChatMessage';
import CitiesShowcase from '@/components/CitiesShowcase';
import { Send, Sparkles, Globe, Loader2 } from 'lucide-react';

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [inputValue, setInputValue] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [cities, setCities] = useState<CityInfo[]>([]);
  const [showCities, setShowCities] = useState(true);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    loadCities();
    addWelcomeMessage();
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

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

  const addWelcomeMessage = () => {
    const welcomeMessage: Message = {
      id: Date.now().toString(),
      type: 'bot',
      content: `Welcome to the Heritage Tourist Guide! 🌍

I'm your personal guide to the world's most magnificent ancient heritage sites and historical destinations. I have detailed knowledge about incredible places like Rome, Athens, Cairo, Istanbul, Kyoto, and many more!

Feel free to ask me about:
• Ancient monuments and heritage sites
• Best times to visit
• Historical significance and stories
• Practical travel tips
• Local recommendations

Click on any city below or ask me anything about these amazing destinations!`,
      timestamp: new Date(),
    };
    setMessages([welcomeMessage]);
  };

  const handleCityClick = (city: CityInfo) => {
    const query = `Tell me about the ancient heritage sites in ${city.city}`;
    setInputValue(query);
    handleSendMessage(query);
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
      const response = await touristApi.askTouristGuide(textToSend);

      // Add bot response
      const botMessage: Message = {
        id: (Date.now() + 1).toString(),
        type: 'bot',
        content: response.response,
        cities_mentioned: response.cities_mentioned,
        heritage_sites_mentioned: response.heritage_sites_mentioned,
        timestamp: new Date(),
      };
      setMessages((prev) => [...prev, botMessage]);
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

  const handleKeyPress = (e: React.KeyboardEvent) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const suggestedQuestions = [
    "What are the must-see sites in Rome?",
    "Best time to visit Machu Picchu?",
    "Tell me about the Pyramids of Giza",
    "Ancient temples in Kyoto"
  ];

  return (
    <div className="min-h-screen bg-heritage-pattern">
      {/* Header */}
      <header className="bg-gradient-to-r from-primary-500 via-primary-600 to-orange-500 shadow-lg sticky top-0 z-10">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="bg-white p-2 rounded-lg shadow-md">
                <Globe className="text-primary-600" size={32} />
              </div>
              <div>
                <h1 className="text-2xl sm:text-3xl font-bold text-white font-serif">
                  Heritage Tourist Guide
                </h1>
                <p className="text-primary-100 text-sm">Your gateway to ancient wonders</p>
              </div>
            </div>
            <Sparkles className="text-white animate-pulse-slow" size={28} />
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Cities Showcase */}
        {showCities && cities.length > 0 && (
          <div className="animate-slideUp">
            <CitiesShowcase cities={cities} onCityClick={handleCityClick} />
          </div>
        )}

        {/* Chat Container */}
        <div className="card p-6 max-w-5xl mx-auto">
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
                onKeyPress={handleKeyPress}
                placeholder="Ask me about ancient heritage sites..."
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
        {!showCities && (
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
      <footer className="bg-gray-800 text-white py-6 mt-12">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
          <p className="text-sm">
            Powered by AI • Explore the world's ancient heritage sites
          </p>
        </div>
      </footer>
    </div>
  );
}
