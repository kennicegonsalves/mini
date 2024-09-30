import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; 
import './Login.css';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  
  const navigate = useNavigate(); 

  const handleSubmit = (e) => {
    e.preventDefault();

    //add validation or authentication logic 

    navigate('/services');
  };

  return (
    <div className="login-container">
      <div className="top-left">
        <h1>SharedMiles</h1>
      </div>
      <div className="login-box">
        <h2 className="login-header">Login</h2>
        <form className="login-form" onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email"
            className="login-input"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            className="login-input"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button type="submit" className="login-btn">LOGIN</button>
        </form>
      </div>
    </div>
  );
};

export default Login;
