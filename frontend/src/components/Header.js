import React from 'react';
import './Header.css'; // Assurez-vous d'importer le fichier CSS

const Header = () => {
    return (
        <header className="App-header">
            <h1>Bienvenue sur mon application</h1>
            <nav>
                <a href="/">Accueil</a>
                <a href="/about">À propos</a>
                <a href="/contact">Contact</a>
            </nav>
        </header>
    );
};

export default Header;