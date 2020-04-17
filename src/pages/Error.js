import React from 'react';
import './Home.css';
import sad from './sad.png';
  
function Error(){
    return(
        <div>
            <div className="mainbox">
            <div className="card1">
                <img alt="sadFace" src={sad} />
                <h2>No Data!</h2>
            </div>
            </div>
        </div>
    );
}

export default Error;