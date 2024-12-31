import axios from 'axios';

const API_URL = 'http://localhost:8000/api/';

// Exemple : Charger un solde via Mobile Money
export const chargeBalance = (clientId, amount, phoneNumber) => {
  return axios.post(`${API_URL}payments/charge/`, {
    clientId,
    amount,
    phoneNumber,  // Le numéro de téléphone du client pour le paiement Mobile Money
  })
    .then(response => {
      // Cette réponse pourrait être une confirmation de paiement ou une erreur
      console.log('Payment success:', response.data);
      return response.data;
    })
    .catch(error => {
      console.error('Error charging balance via Mobile Money:', error);
      throw error;
    });
};

// Exemple : Enregistrer un paiement
export const recordPayment = (paymentData) => {
  return axios.post(`${API_URL}payments/`, paymentData)
    .then(response => {
      console.log('Payment recorded:', response.data);
      return response.data;
    })
    .catch(error => {
      console.error('Error recording payment:', error);
      throw error;
    });
};

// Exemple : Vérification du statut de la transaction (si le service de Mobile Money propose une vérification)
export const verifyTransaction = (transactionId) => {
  return axios.get(`${API_URL}payments/verify/${transactionId}/`)
    .then(response => {
      console.log('Transaction verified:', response.data);
      return response.data;
    })
    .catch(error => {
      console.error('Error verifying transaction:', error);
      throw error;
    });
};

// Exemple de gestion de l'historique des paiements pour un client
export const getPaymentHistory = (clientId) => {
  return axios.get(`${API_URL}payments/history/${clientId}/`)
    .then(response => response.data)
    .catch(error => {
      console.error(`Error fetching payment history for client ${clientId}:`, error);
      throw error;
    });
};
