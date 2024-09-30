import React from 'react';
import './Home.css';

function Home() {
  return (
    <div>
      <h4>Topics to be covered</h4>
      <table border="1" className="topics-table">
        <thead>
          <tr>
            <th>Sr. No.</th>
            <th>Topics</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>Internet Programming</td>
          </tr>
          <tr>
            <td>2</td>
            <td>Advanced Data Structures and Algorithms</td>
          </tr>
          <tr>
            <td>3</td>
            <td>Software Engineering</td>
          </tr>
          <tr>
            <td>4</td>
            <td>Computer Networks and Security</td>
          </tr>
          <tr>
            <td>5</td>
            <td>Entrepreneurship and E-business</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
export default Home;
