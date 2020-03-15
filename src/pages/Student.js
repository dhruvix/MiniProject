import './Student.css';
import React from "react";
import {
  Link,
  useRouteMatch
} from "react-router-dom";

function Student() {
    let match = useRouteMatch();

    return (
      <div className="mainbox">
        <div className="main">
            <h2 className="heading">Student Analytics</h2>
            <div>
            <Link to={`${match.url}/higherstudies`}>Higher Studies</Link>
            </div>
            <div>
            <Link to={`${match.url}/competetiveexams`}>Competetive Exams</Link>
            </div>
            <div>
            <Link to={`${match.url}/internships`}>Internships</Link>
            </div>
            <div>
            <Link to={`${match.url}/placements`}>Placements</Link>
            </div>
            <div>
            <Link to={`${match.url}/achievements`}>Student Achievements</Link>
            </div>
            <div>
            <Link to={`${match.url}/activities`}>Student Activities</Link>
            </div>
            <div>
            <Link to={`${match.url}/conference`}>Conference Publications</Link>
            </div>
            <div>
            <Link to={`${match.url}/journal`}>Journal Publications</Link>
            </div>
        </div>
      </div>
    );
}

export default Student;