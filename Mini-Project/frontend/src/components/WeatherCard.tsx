'use client';

import { Cloud, Droplets, Wind, Thermometer, Calendar } from 'lucide-react';
import { WeatherData } from '@/services/api';

interface WeatherCardProps {
  weather: WeatherData;
}

export default function WeatherCard({ weather }: WeatherCardProps) {
  const getWeatherIcon = (condition: string) => {
    const lowerCondition = condition.toLowerCase();
    if (lowerCondition.includes('rain')) return '🌧️';
    if (lowerCondition.includes('cloud')) return '☁️';
    if (lowerCondition.includes('clear') || lowerCondition.includes('sun')) return '☀️';
    if (lowerCondition.includes('snow')) return '❄️';
    if (lowerCondition.includes('thunder')) return '⛈️';
    return '🌤️';
  };

  const formatTimestamp = (timestamp: string) => {
    const date = new Date(timestamp);
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    });
  };

  return (
    <div className="card p-6 bg-gradient-to-br from-primary-50 to-primary-100 border-2 border-primary-200">
      <div className="flex items-start justify-between mb-4">
        <div>
          <h3 className="text-2xl font-bold text-gray-800">{weather.city}</h3>
          <p className="text-sm text-gray-600 flex items-center gap-1 mt-1">
            <Calendar size={14} />
            {formatTimestamp(weather.timestamp)}
          </p>
        </div>
        <div className="text-5xl">{getWeatherIcon(weather.condition)}</div>
      </div>

      <div className="grid grid-cols-2 gap-4 mb-4">
        <div className="flex items-center gap-3 bg-white/80 p-3 rounded-lg">
          <Thermometer className="text-primary-600" size={24} />
          <div>
            <p className="text-3xl font-bold text-gray-800">{weather.temperature}°C</p>
            <p className="text-xs text-gray-600">Temperature</p>
          </div>
        </div>

        <div className="flex items-center gap-3 bg-white/80 p-3 rounded-lg">
          <Droplets className="text-primary-600" size={24} />
          <div>
            <p className="text-3xl font-bold text-gray-800">{weather.humidity}%</p>
            <p className="text-xs text-gray-600">Humidity</p>
          </div>
        </div>
      </div>

      <div className="flex items-center gap-3 bg-white/80 p-3 rounded-lg mb-4">
        <Wind className="text-primary-600" size={24} />
        <div>
          <p className="text-2xl font-bold text-gray-800">{weather.wind_speed} m/s</p>
          <p className="text-xs text-gray-600">Wind Speed</p>
        </div>
      </div>

      <div className="flex items-center gap-2 bg-white/80 p-3 rounded-lg">
        <Cloud className="text-primary-600" size={20} />
        <p className="text-sm font-medium text-gray-700">{weather.condition}</p>
      </div>
    </div>
  );
}
