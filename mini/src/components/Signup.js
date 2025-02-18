import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './Signup.css';

const Signup = () => {
  const [formData, setFormData] = useState({
    fullName: '',
    email: '',
    phoneNumber: '',
    password: '',
    confirmPassword: '',
    homeAddress: '',
    workAddress: '',
  });

  const [errorMessage, setErrorMessage] = useState('');

  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const { fullName, email, phoneNumber, password, confirmPassword, homeAddress, workAddress } = formData;

    if (!fullName || !email || !phoneNumber || !password || !confirmPassword || !homeAddress || !workAddress) {
      setErrorMessage('Please fill in all fields.');
      return;
    }

    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      setErrorMessage('Please enter a valid email.');
      return;
    }

    if (phoneNumber.length !== 10 || isNaN(phoneNumber)) {
      setErrorMessage('Please enter a valid 10-digit phone number.');
      return;
    }

    if (password.length < 6) {
      setErrorMessage('Password must be at least 6 characters long.');
      return;
    }

    if (password !== confirmPassword) {
      setErrorMessage('Passwords do not match.');
      return;
    }

    setErrorMessage('');
    navigate('/services');
  };

  return (
    <div className="login-container">
      <div className="top-left">
        <h1>SharedMiles</h1>
      </div>
      <div className="login-box">
        <h2 className="login-header">Sign Up</h2>
        <form className="login-form" onSubmit={handleSubmit}>
          <input
            type="text"
            name="fullName"
            placeholder="Full Name"
            className="login-input"
            value={formData.fullName}
            onChange={handleChange}
          />
          <input
            type="email"
            name="email"
            placeholder="Email"
            className="login-input"
            value={formData.email}
            onChange={handleChange}
          />
          <input
            type="tel"
            name="phoneNumber"
            placeholder="Phone Number"
            className="login-input"
            value={formData.phoneNumber}
            onChange={handleChange}
          />
          <input
            type="password"
            name="password"
            placeholder="Password"
            className="login-input"
            value={formData.password}
            onChange={handleChange}
          />
          <input
            type="password"
            name="confirmPassword"
            placeholder="Confirm Password"
            className="login-input"
            value={formData.confirmPassword}
            onChange={handleChange}
          />
          <input
            type="text"
            name="homeAddress"
            placeholder="Home Address"
            className="login-input"
            value={formData.homeAddress}
            onChange={handleChange}
          />
          <input
            type="text"
            name="workAddress"
            placeholder="Work Address"
            className="login-input"
            value={formData.workAddress}
            onChange={handleChange}
          />
          {errorMessage && <p className="error-message">{errorMessage}</p>}
          <button type="submit" className="login-btn">SIGN UP</button>
        </form>
      </div>
    </div>
  );
};

export default Signup;
