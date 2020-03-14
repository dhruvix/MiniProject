import React, { useEffect, useState } from 'react';
import './Home.css';
import HsTable from './HsTable';

function HsData() {
  const [hstudies, setIt] = useState([]);
  useEffect(()=>{fetch("/HS2data").then(response=>response.json().then(data1=>{setIt(data1)
    console.log(data1[0])
}))},[]);
 
  return (
    <div className="App">
      
      <HsTable hsdata={hstudies}/>
    </div>
  );
}
export default HsData;
