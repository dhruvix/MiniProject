import React from "react";
import './Faculty.css';
import Logo from '../components/Logo';
import {
  Link,
  useRouteMatch
} from "react-router-dom";

function NonTeach() {
    let match = useRouteMatch();
    const tabs = ['non_teaching_staff','staff_achievement','staff_service'];

    function getname(str){
        return str.replace(/_/g, " ");
    }

    return (
      <div>
        <div style={{marginTop:'10px'}}>
        <Logo />
        </div>
        <div className="main">
            <h2 className="heading">Non Teaching Staff Data Visualization</h2>
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

export default NonTeach;