import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export interface TouristQueryRequest {
  query: string;
}

export interface TouristQueryResponse {
  success: boolean;
  response: string;
  cities_mentioned: string[];
  heritage_sites_mentioned: string[];
  sources_count: number;
  error?: string;
}

export interface CityInfo {
  city: string;
  country: string;
  heritage_sites_count: number;
}

export interface WeatherAgentRequest {
  query: string;
  conversation_history?: Array<{role: string; content: string}>;
}

export interface WeatherAgentResponse {
  success: boolean;
  response: string;
  is_weather_related: boolean;
  tool_calls: any[];
  model?: string;
  error?: string;
}

export interface WeatherData {
  city: string;
  timestamp: string;
  temperature: number;
  humidity: number;
  wind_speed: number;
  condition: string;
}

export interface WeatherHistoryResponse {
  city: string;
  records: WeatherData[];
  count: number;
}

export const touristApi = {
  async askTouristGuide(query: string): Promise<TouristQueryResponse> {
    const response = await axios.post<TouristQueryResponse>(
      `${API_URL}/tourist/ask`,
      { query }
    );
    return response.data;
  },

  async getAvailableCities(): Promise<CityInfo[]> {
    const response = await axios.get<CityInfo[]>(`${API_URL}/tourist/cities`);
    return response.data;
  },

  async checkHealth(): Promise<any> {
    const response = await axios.get(`${API_URL}/tourist/health`);
    return response.data;
  }
};

export const weatherApi = {
  async askWeatherAgent(query: string, conversation_history?: any[]): Promise<WeatherAgentResponse> {
    const response = await axios.post<WeatherAgentResponse>(
      `${API_URL}/agent/query`,
      { query, conversation_history }
    );
    return response.data;
  },

  async getLatestWeather(city: string): Promise<WeatherData> {
    const response = await axios.get<WeatherData>(`${API_URL}/weather/latest/${city}`);
    return response.data;
  },

  async getWeatherHistory(city: string, days?: number): Promise<WeatherHistoryResponse> {
    const params = days ? `?days=${days}` : '';
    const response = await axios.get<WeatherHistoryResponse>(
      `${API_URL}/weather/history/${city}${params}`
    );
    return response.data;
  },

  async checkHealth(): Promise<any> {
    const response = await axios.get(`${API_URL}/agent/health`);
    return response.data;
  }
};
