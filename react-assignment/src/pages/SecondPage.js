import './SecondPage.css';
import React from 'react';

const SecondPage = () => {

  const handleSubmit = (event) => {
    event.preventDefault(); 
    alert('Form Submitted'); 
  };

  return (
    <div className="second-page-container">
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="scholarship-info">Display Label</label>
          <input type="text" id="scholarship-info" name="scholarship-info" placeholder="How did you hear about this scholarship?" />
        </div>

        <div className="form-group checkbox-group">
          <label>
            <input type="checkbox" name="required" /> Required
          </label>
        </div>

        <div className="section-header">Print Options</div>
        <div className="form-group checkbox-group">
          <label>
            <input type="checkbox" name="printOptions" /> Page Break Before Element?
          </label>
        </div>

        <div className="section-header">Alternate/Short Form</div>
        <div className="form-group checkbox-group">
          <label>
            <input type="checkbox" name="alternateForm" /> Display on alternate/shorter form?
          </label>
        </div>

        <div className="options-container">
          <span className="options-header">Options</span>
          <span className="value-header">Value</span>
          <span className="correct-header">Correct</span>
        </div>

        <div className="form-group options-group">
          <div className="option-item">
            <input type="text" placeholder="Internet" className="option-input" />
            <input type="text" className="option-value" />
            <input type="checkbox" className="option-checkbox" />
          </div>
          <div className="option-item">
            <input type="text" placeholder="Other" className="option-input" />
            <input type="text" className="option-value" />
            <input type="checkbox" className="option-checkbox" />
          </div>
          <div className="option-item">
            <input type="text" placeholder="Option text" className="option-input" />
            <input type="text" className="option-value" />
            <input type="checkbox" className="option-checkbox" />
          </div>
        </div>

        <button type="submit" className="submit-button">Submit</button>
      </form>
    </div>
  );
};

export default SecondPage;
