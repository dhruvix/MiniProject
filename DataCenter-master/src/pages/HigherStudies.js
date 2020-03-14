import React from 'react';
import './Home.css';
import {
    Link,
    useRouteMatch
  } from "react-router-dom";
  
function HigherStudies(){
    let match = useRouteMatch();
    return(
        <div>
            <div className="mainbox">
                <div className="card1">
                    <h2>Graph or data?</h2>
                    <div className="buttline">
                        <Link to={`${match.url}/data`}>Data</Link>
                        <Link to={`${match.url}/graph`}>Graph</Link>
                    </div>
                </div>
            </div>
        </div>
    );
}

export default HigherStudies;