import React from 'react';
import './Home.css';
import sad from '../images/sad.png';
  
function Error({message}){
    return(
        <div>
            <div className="mainbox">
            <div className="card1">
                <img alt="sadFace" src={sad} />
                <h2>{message}</h2>
            </div>
            </div>
        </div>
    );
}

export default Error;