import React from 'react';
import './Footer.css'; // Assurez-vous d'importer le fichier CSS pour le style

const Footer = () => {
    return (
        <footer className="App-footer">
            <div>
                &copy; {new Date().getFullYear()} Mon Application. Tous droits réservés.
            </div>
            <div>
                <a href="/contact" className="footer-link">Contact</a>
                <a href="/about" className="footer-link">À propos</a>
            </div>
        </footer>
    );
};

export default Footer;