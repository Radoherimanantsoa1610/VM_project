import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

// Récupérer tous les tickets
export const getTickets = () => {
  return axios.get(`${API_URL}tickets/`)
    .then(response => response.data)
    .catch(error => {
      console.error('Error fetching tickets:', error);
      throw error;
    });
};

// Récupérer un ticket par son ID
export const getTicketById = (ticketId) => {
  return axios.get(`${API_URL}tickets/${ticketId}/`)
    .then(response => response.data)
    .catch(error => {
      console.error(`Error fetching ticket ${ticketId}:`, error);
      throw error;
    });
};

// Créer un nouveau ticket
export const createTicket = (ticketData) => {
  return axios.post(`${API_URL}tickets/`, ticketData)
    .then(response => response.data)
    .catch(error => {
      console.error('Error creating ticket:', error);
      throw error;
    });
};

// Mettre à jour un ticket
export const updateTicket = (ticketId, ticketData) => {
  return axios.put(`${API_URL}tickets/${ticketId}/`, ticketData)
    .then(response => response.data)
    .catch(error => {
      console.error(`Error updating ticket ${ticketId}:`, error);
      throw error;
    });
};

// Supprimer un ticket
export const deleteTicket = (ticketId) => {
  return axios.delete(`${API_URL}tickets/${ticketId}/`)
    .then(response => response.data)
    .catch(error => {
      console.error(`Error deleting ticket ${ticketId}:`, error);
      throw error;
    });
};
