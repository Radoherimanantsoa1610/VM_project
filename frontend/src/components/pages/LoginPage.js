import React, { useState } from 'react';

const LoginPage = ({ setIsLoggedIn, setError }) => {
  const [loading, setLoading] = useState(false); // Indicateur de chargement
  const [username, setUsername] = useState(''); // État pour le nom d'utilisateur
  const [password, setPassword] = useState(''); // État pour le mot de passe
  const [error, setLocalError] = useState(null); // État pour l'erreur

  // Fonction de gestion de la connexion
  const handleLogin = (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null); // Réinitialiser les erreurs avant chaque tentative de connexion

    // Appel à l'API de connexion
    fetch('http://ton-backend-api.com/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }), // Envoyer les informations de connexion
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.token) {
          localStorage.setItem('token', data.token); // Sauvegarder le token reçu du backend
          setIsLoggedIn(true); // Connexion réussie
        } else {
          setLocalError('Identifiants incorrects'); // Afficher l'erreur en cas de problème
          setError('Identifiants incorrects'); // Passer l'erreur vers App.js
        }
        setLoading(false); // Fin du chargement
      })
      .catch((error) => {
        console.error('Erreur:', error);
        setLocalError('Erreur de connexion');
        setError('Erreur de connexion'); // Passer l'erreur vers App.js
        setLoading(false); // Fin du chargement
      });
  };

  return (
    <div className="login-page">
      <h2>Connexion</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>} {/* Afficher l'erreur si présente */}
      <form onSubmit={handleLogin}>
        <div>
          <label>Nom d'utilisateur</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Mot de passe</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <div>
          <button type="submit" disabled={loading}>
            {loading ? 'Chargement...' : 'Se connecter'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default LoginPage
