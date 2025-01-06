// src/components/pages/LoginPage.js
import React, { useState } from 'react';

const LoginPage = ({ setIsLoggedIn, setError }) => {
  const [loading, setLoading] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [localError, setLocalError] = useState(null);

  const handleLogin = (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);  // Réinitialiser l'erreur locale

    // Envoi de la requête POST à l'endpoint '/api/token/'
    fetch('http://127.0.0.1:8000/api/token/', {  // URL mise à jour
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ username, password }),  // Les identifiants envoyés
    })
      .then((response) => {
        // Vérification du statut de la réponse (si c'est OK)
        if (!response.ok) {
          throw new Error('Identifiants incorrects ou problème serveur');
        }
        return response.json();
      })
      .then((data) => {
        if (data.access) {
          // Sauvegarder le token d'accès dans le stockage local
          localStorage.setItem('token', data.access);
          setIsLoggedIn(true);  // Connexion réussie
        } else {
          setLocalError(data.detail || 'Identifiants incorrects');  // Gestion des erreurs
          setError(data.detail || 'Identifiants incorrects');
        }
        setLoading(false);  // Fin du chargement
      })
      .catch((error) => {
        // Gestion des erreurs globales (problème serveur, etc.)
        setLocalError(error.message || 'Erreur de connexion');
        setError(error.message || 'Erreur de connexion');
        setLoading(false);  // Fin du chargement
      });
  };

  return (
    <div className="login-page">
      <h2>Connexion</h2>
      {localError && <p style={{ color: 'red' }}>{localError}</p>}  {/* Affichage des erreurs */}
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

export default LoginPage;
