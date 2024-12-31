import React, { useState } from 'react';

const TicketPurchasePage = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [paymentProcessing, setPaymentProcessing] = useState(false);
  const [paymentError, setPaymentError] = useState(null); // Gérer l'erreur de paiement

  const handlePurchase = (e) => {
    e.preventDefault();
    setPaymentProcessing(true);
    setPaymentError(null);

    fetch('https://api.vanillapay.com/charge', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        name,
        email,
        amount: 1000,  // Exemple de montant
        currency: 'USD',
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          console.log('Paiement réussi');
        } else {
          setPaymentError('Erreur de paiement');
        }
        setPaymentProcessing(false);
      })
      .catch((error) => {
        console.error('Erreur:', error);
        setPaymentError('Erreur de paiement');
        setPaymentProcessing(false);
      });
  };

  return (
    <div>
      <h2>Achète ton ticket</h2>
      {paymentError && <p style={{ color: 'red' }}>{paymentError}</p>}  {/* Afficher l'erreur de paiement */}
      <form onSubmit={handlePurchase}>
        <label>
          Nom:
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit" disabled={paymentProcessing}>
          {paymentProcessing ? 'Traitement en cours...' : 'Payer'}
        </button>
      </form>
    </div>
  );
};

export default TicketPurchasePage;
