import React from 'react';
import { Link } from 'react-router-dom';
import './LandingPage.css';


const LandingPage = () => {
  return (
    <div className="landing-page">
      <header className="header">
        <h1 className="title">Welcome to the Scholarship Application Portal</h1>
        <p className="description">
          Empowering students to achieve their dreams through our scholarship programs. Explore opportunities and start your application today!
        </p>
      </header>
      <div className="content">
        <Link to="/second" className="button">Apply Now</Link>
      </div>
      <footer className="footer">
        <p className="footer-text"><b>Kennice Gonsalves, Roll Number: 39, Batch: A3</b></p>
      </footer>
    </div>
  );
};


export default LandingPage;