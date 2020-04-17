import React from 'react';
import {Link} from "react-router-dom";
import './Home.css';
import MSRITlogo from './MSRITlogo.png';

function Home() {
  return (
    <div>
        <div className = "mainbox">
        <div className="card1">
          <img alt="MSRIT_logo" src={MSRITlogo} />
          <h1>College Analytics</h1>
          <div className="buttline">
          <Link className = "butt" to="/faculty">Faculty</Link>
          <Link className = "butt" to="/student">Student</Link>
          <Link className = "butt" to="/nonteaching">Non Teaching Staff</Link>
          </div>
        </div>
        </div>
    </div>
  );
}

export default Home;
