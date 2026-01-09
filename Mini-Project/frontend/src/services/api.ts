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
