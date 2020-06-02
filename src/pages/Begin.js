import React from 'react';
import {Link} from "react-router-dom";
import dhruva from "../images/dhruva.jpg";
import harsha from "../images/harsha.jpg";
import abhishek from "../images/abhishek.jpg";
import sandeep from "../images/sandeep.jpg";
import './Begin.css';

function Begin() {
    return (
        <div className="everything">
            <div className="heading">
                <h1 className="tit">Mini project - June 2020</h1>
                <h3>Data centre visualization</h3>
                <div className="buttline">
                    <Link className="butt" to="/home">Data Visualization and Analytics</Link>
                    <Link className="butt" to="/generate_link">Generte Paper links</Link>
                </div>
                <h4 style={{marginTop:'10px'}}>created by:</h4>
            </div>
            <div className="infoHolder">
            <div className="info">
                <img src={abhishek} alt="Avatar" width='200px' height='200px'/>
                <div className="container">
                    <h4><b>Abhishek Srivastava</b></h4>
                    <p>1MS17CS003</p>
                </div>
            </div>
            <div className="info">
                <img src={dhruva} alt="Avatar" width='200px' height='200px'/>
                <div className="container">
                    <h4><b>Dhruva H Narayan</b></h4>
                    <p>1MS17CS029</p>
                </div>
            </div>
            <div className="info">
                <img src={harsha} alt="Avatar" width='200px' height='200px'/>
                <div className="container">
                    <h4><b>Harsha H Narayan</b></h4>
                    <p>1MS17CS035</p>
                </div>
            </div>
            <div className="info">
                <img src={sandeep} alt="Avatar" width='200px' height='200px'/>
                <div className="container">
                    <h4><b>P Sandeep Reddy</b></h4>
                    <p>1MS17CS077</p>
                </div>
            </div>
            </div>
        </div>
    )
}

export default Begin;
