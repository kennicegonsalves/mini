import React from 'react';
import './App.css';
import Home from './Home';
import Sessions from './Sessions';
import Contacts from './Contacts';
import {BrowserRouter as Router, Routes, Route, Link} from 'react-router-dom';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFacebook, faInstagram, faYoutube } from "@fortawesome/free-brands-svg-icons";


function App() {
  return (
    <Router>
    <div>
      <header>
        <h1><center>Single Page Application</center></h1>
        <nav className="navbar">
          <Link to='/home'>Home</Link>
          <Link to='/sessions'>Sessions</Link>
          <Link to='/contacts'>Contacts</Link>
          <div>
            <a href="https://www.facebook.com" className="facebook social"><FontAwesomeIcon icon={faFacebook} size="2x" /></a>
            <a href="https://www.instagram.com" className="instagram social"><FontAwesomeIcon icon={faInstagram} size="2x" /></a>
            <a href="https://www.youtube.com" className="youtube social"><FontAwesomeIcon icon={faYoutube} size="2x" /></a>
          </div>
      </nav>
      <main>
        <Routes>
          <Route path="/home" element={<Home/>}/>
          <Route path="/sessions" element={<Sessions/>}/>
          <Route path="/contacts" element={<Contacts/>}/>
        </Routes>
      </main>
 
      </header>
    </div>
    </Router>
  );
}
export default App;

