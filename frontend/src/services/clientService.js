import axios from 'axios';

// URL de base pour l'API
const API_URL = 'http://localhost:8000/api/';

// Récupérer tous les clients
export const getClients = () => {
  return axios.get(`${API_URL}clients/`)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching clients:', error);
      throw error;
    });
};

// Récupérer un client par son ID
export const getClientById = (clientId) => {
  return axios.get(`${API_URL}clients/${clientId}/`)
    .then(response => response.data)
    .catch(error => {
      console.error(`Error fetching client ${clientId}:`, error);
      throw error;
    });
};

// Ajouter un nouveau client
export const addClient = (clientData) => {
  return axios.post(`${API_URL}clients/`, clientData)
    .then(response => response.data)
    .catch(error => {
      console.error('Error adding client:', error);
      throw error;
    });
};

// Mettre à jour un client
export const updateClient = (clientId, clientData) => {
  return axios.put(`${API_URL}clients/${clientId}/`, clientData)
    .then(response => response.data)
    .catch(error => {
      console.error(`Error updating client ${clientId}:`, error);
      throw error;
    });
};

// Supprimer un client
export const deleteClient = (clientId) => {
  return axios.delete(`${API_URL}clients/${clientId}/`)
    .then(response => response.data)
    .catch(error => {
      console.error(`Error deleting client ${clientId}:`, error);
      throw error;
    });
};
