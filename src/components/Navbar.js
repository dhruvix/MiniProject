import React from 'react';
import {Link} from "react-router-dom";
import './Navbar.css';

function Navbar({links}){

    return(
        <nav>
        {
            links.map((att,i)=>{
                return(
                    <Link to={att.url}>{att.Name}</Link>  
                ); 
            })
        }
        </nav>
    );
}

export default Navbar;