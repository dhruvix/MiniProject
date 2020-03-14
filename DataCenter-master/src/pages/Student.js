import './Student.css';
import React from "react";
import {
  Link,
  useRouteMatch
} from "react-router-dom";

function Student() {
    let match = useRouteMatch();

    return (
      <div>
        <div>
        <div className="main">
            <h2>Student Analytics</h2>
        </div>
        <nav>
            <Link to={`${match.url}/higherstudies`}>Higher Studies</Link>
            <Link to={`${match.url}/placements`}>Placements</Link>
            <Link to={`${match.url}/achievements`}>Student Achievements</Link>
            <Link to={`${match.url}/activities`}>Student Activities</Link>
        </nav>
        </div>
      </div>
    );
}

export default Student;