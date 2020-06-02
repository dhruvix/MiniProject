import React from "react";
import './Faculty.css';
import Logo from '../components/Logo';
import {
  Link,
  useRouteMatch
} from "react-router-dom";

function Faculty() {
    let match = useRouteMatch();
    const tabs = ["book","book_chapter","conference_paper","consultancy","courses_handled","faculty","faculty_conference_symposia","faculty_guest_lecture","faculty_patent","faculty_qualification","faculty_research","faculty_service","faculty_workshop_fdp","funded_projects"];

    function getname(str){
        return str.replace(/_/g, " ");
    }

    return (
      <div>
        <div style={{marginTop:'10px'}}>
        <Logo />
        </div>
        <div className="main">
            <h2 className="heading">Faculty Data Visualization</h2>
            {
                tabs.map((topic)=>{
                    return(
                        <div>
                            <Link to={`${match.url}/${topic}`}>{getname(topic)}</Link>
                        </div>   
                    )
                })
            } 
        </div>
      </div>
    );
}

export default Faculty;