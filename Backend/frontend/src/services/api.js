import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

// Fonction pour récupérer tous les clients
export const getClients = () => {
  return axios.get(`${API_URL}clients/`)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching clients:', error);
      throw error;
    });
};

// Fonction pour obtenir le token de l'utilisateur
export const login = (username, password) => {
  return axios.post(`${API_URL}token/`, { username, password })
    .then(response => response.data)
    .catch(error => {
      console.error('Login failed:', error);
      throw error;
    });
};
