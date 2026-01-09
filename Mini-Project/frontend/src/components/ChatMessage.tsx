'use client';

import { User, Bot, MapPin, Landmark } from 'lucide-react';

export interface Message {
  id: string;
  type: 'user' | 'bot';
  content: string;
  cities_mentioned?: string[];
  heritage_sites_mentioned?: string[];
  timestamp: Date;
}

interface ChatMessageProps {
  message: Message;
}

export default function ChatMessage({ message }: ChatMessageProps) {
  const isUser = message.type === 'user';

  return (
    <div className={`flex gap-3 mb-6 animate-fadeIn ${isUser ? 'justify-end' : 'justify-start'}`}>
      {!isUser && (
        <div className="flex-shrink-0 w-10 h-10 rounded-full bg-gradient-to-br from-primary-400 to-primary-600 flex items-center justify-center shadow-md">
          <Bot className="text-white" size={20} />
        </div>
      )}

      <div className={`flex flex-col ${isUser ? 'items-end' : 'items-start'} max-w-3xl`}>
        <div className={isUser ? 'chat-bubble-user' : 'chat-bubble-bot'}>
          <p className="text-sm leading-relaxed whitespace-pre-wrap">{message.content}</p>
        </div>

        {!isUser && (message.cities_mentioned?.length || message.heritage_sites_mentioned?.length) ? (
          <div className="mt-3 flex flex-wrap gap-2">
            {message.cities_mentioned?.map((city, idx) => (
              <span key={idx} className="badge bg-secondary-100 text-secondary-800 flex items-center gap-1">
                <MapPin size={14} />
                {city}
              </span>
            ))}
            {message.heritage_sites_mentioned?.map((site, idx) => (
              <span key={idx} className="badge bg-primary-100 text-primary-800 flex items-center gap-1">
                <Landmark size={14} />
                {site}
              </span>
            ))}
          </div>
        ) : null}

        <span className="text-xs text-gray-400 mt-1">
          {message.timestamp.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
        </span>
      </div>

      {isUser && (
        <div className="flex-shrink-0 w-10 h-10 rounded-full bg-gradient-to-br from-gray-600 to-gray-800 flex items-center justify-center shadow-md">
          <User className="text-white" size={20} />
        </div>
      )}
    </div>
  );
}
