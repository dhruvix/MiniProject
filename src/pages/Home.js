import React from 'react';
import {Link} from "react-router-dom";
import './Home.css';
import MSRITlogo from '../images/MSRITlogo.png';

function Home() {
  return (
    <div>
        <div className = "mainbox">
        <div className="card1">
          <img alt="MSRIT_logo" src={MSRITlogo} />
          <h1>RIT college data visualization and analytics</h1>
          <div className="buttline">
          <Link className = "butt" to="/faculty-anal">Faculty Data Analytics</Link>
          <Link className = "butt" to="/student-anal">Student Data Analytics</Link>
          </div>
          <div className="buttline">
          <Link className = "butt" to="/faculty">Faculty Data Visualization</Link>
          <Link className = "butt" to="/student">Student Data Visualization</Link>
          </div>
          <div className="buttline">
          <Link className = "butt" to="/nonteaching">Non teaching staff Data Visualization</Link>
          </div>
        </div>
        </div>
    </div>
  );
}

export default Home;
