// src/App.js
import React, { useState } from "react";
import LoginPage from "./components/pages/LoginPage";  // Import du composant LoginPage

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [error, setError] = useState(null); // Ajout d'un état pour gérer les erreurs globales

  return (
    <div>
      <h1>Welcome to the Event Management System</h1>
      
      {/* Utilisation de isLoggedIn dans le rendu */}
      {isLoggedIn ? (
        <p>You are logged in!</p>  // Si l'utilisateur est connecté
      ) : (
        <p>Please log in.</p>  // Si l'utilisateur n'est pas connecté
      )}

      {/* Affichage de l'erreur si présente */}
      {error && <p style={{ color: 'red' }}>{error}</p>}

      {/* Passer la fonction setIsLoggedIn et setError à LoginPage pour changer l'état */}
      <LoginPage setIsLoggedIn={setIsLoggedIn} setError={setError} />
    </div>
  );
}

export default App;
