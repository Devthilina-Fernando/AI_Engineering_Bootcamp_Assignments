'use client';

import { CityInfo } from '@/services/api';
import { MapPin, Landmark } from 'lucide-react';

interface CitiesShowcaseProps {
  cities: CityInfo[];
  onCityClick: (city: CityInfo) => void;
}

export default function CitiesShowcase({ cities, onCityClick }: CitiesShowcaseProps) {
  return (
    <div className="mb-8">
      <h2 className="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
        <MapPin className="text-primary-500" size={28} />
        Explore Heritage Destinations
      </h2>
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4">
        {cities.map((city) => (
          <div
            key={`${city.city}-${city.country}`}
            onClick={() => onCityClick(city)}
            className="city-card group"
          >
            <div className="flex items-start justify-between mb-3">
              <div>
                <h3 className="text-lg font-bold text-gray-800 group-hover:text-primary-600 transition-colors">
                  {city.city}
                </h3>
                <p className="text-sm text-gray-500">{city.country}</p>
              </div>
              <Landmark className="text-primary-400 group-hover:text-primary-600 transition-colors" size={24} />
            </div>
            <div className="flex items-center gap-2 text-sm text-gray-600">
              <span className="badge-primary">
                {city.heritage_sites_count} {city.heritage_sites_count === 1 ? 'Site' : 'Sites'}
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
