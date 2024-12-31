import React, { useState, useEffect } from 'react';

const ClientDetails = ({ clientId }) => {
  const [client, setClient] = useState(null);

  useEffect(() => {
    fetch(`http://localhost:8000/api/clients/${clientId}`)
      .then(response => response.json())
      .then(data => setClient(data))
      .catch(error => console.error("Error fetching client data:", error));
  }, [clientId]); // Le hook se déclenche chaque fois que clientId change

  return (
    <div>
      {client ? (
        <div>
          <h2>Détails du client</h2>
          <p>Nom: {client.name}</p>
          <p>Email: {client.email}</p>
          {/* Ajoutez d'autres informations du client si nécessaire */}
        </div>
      ) : (
        <p>Chargement...</p>
      )}
    </div>
  );
};

export default ClientDetails;
