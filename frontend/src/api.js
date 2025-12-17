// Placeholder for API interactions
const API_BASE_URL = '/api';

export async function checkHealth() {
  try {
    const response = await fetch(`${API_BASE_URL}/`);
    return await response.json();
  } catch (error) {
    console.error('Error fetching health status:', error);
    return null;
  }
}
