import React, { useEffect, useState } from 'react';
import '../Home.css';
import HsTable from './HsTable';
import Error from '../Error';
//import { DropdownMenu, MenuItem } from 'react-bootstrap';

function HsData() {
  const [hstudies, setIt] = useState([]);
  const [x, setx] = useState('country');
  const [y, sety] = useState('nos');
  const [dep, setdep] = useState('all');
  const [year, setyear] = useState('all');
  const [istable, settable] = useState(false);
  const [rendered,render]=useState(false)
  useEffect(()=>{fetch("/data").then(response=>response.json().then(data1=>{setIt(data1);
    render(true)
    console.log(data1[0]);}))},[]);
 
  function handleChangex(event) {
    setx(event.target.value);
  }
  function handleChangey(event) {
    sety(event.target.value); 
  }
  function handleChangedep(event) {
    setdep(event.target.value);
  }
  function handleChangeyear(event) {
    setyear(event.target.value); 
  }

  return (
    <div> 
      {
        istable?(rendered?
        <HsTable hsdata={hstudies}/>
        :<Error />)
        :
          <div className="mainbox">
            <div className="card1">
              <form method="post">
                <div>
                  <h3>Choose parameters</h3>
                  <div className="together">
                    <h5>x:</h5>
                    <select id="x" name="x" onChange={handleChangex}>
                      <option value="country">country</option>
                      <option value="yearOfPassing">year of passing</option>
                      <option value="departmentId">department</option>
                      <option value="course">course</option>
                      <option value="program">program</option>
                    </select>
                  </div>
                  <div className="together">
                  {/* <DropdownMenu userName="Chris Smith">
                    <MenuItem text="Home" location="/home" />
                    <MenuItem text="Edit Profile" location="/profile" />
                    <MenuItem text="Change Password" location="/change-password" />
                    <MenuItem text="Privacy Settings" location="/privacy-settings" />
                    <MenuItem text="Delete Account" onClick={this.deleteAccount} />
                    <MenuItem text="Logout" onClick={this.logout} />
                  </DropdownMenu> */}
                  </div>
                  <div className="together">
                    <h5>year:</h5>
                    <select id="year" name="year" onChange={handleChangeyear}>
                      <option value="all">all</option>
                      <option value="2019">2019</option>
                      <option value="2018">2018</option>
                      <option value="2017">2017</option>
                      <option value="2016">2016</option>
                      <option value="2015">2015</option>
                    </select>
                  </div>
                  <div className="together">
                    <h5>department:</h5>
                    <select id="dep" name="dep" onChange={handleChangedep}>
                      <option value="all">all</option>
                      <option value="cs">computer science</option>
                      <option value="is">information science</option>
                      <option value="ec">electronics and communication</option>
                      <option value="ee">electrical engineering</option>
                      <option value="cv">civil engineering</option>
                      <option value="bt">biotechnology</option>
                      <option value="ch">chemical engineering</option>
                      <option value="im">industrial management</option>
                      <option value="it">information technology</option>
                      <option value="mba">MBA</option>
                      <option value="me">mechanical engineering</option>
                      <option value="ml">medical electronics</option>
                      <option value="te">telecommunication</option>
                    </select>
                  </div>
                </div>
                <button className="butt" type="submit" onClick={async () => {
                  const data = {
                    "tab":"higher_studies",
                    "x": x,
                    "y": y,
                    "dep": dep,
                    "year": year
                  };
                  console.log(data);
                  const response = await fetch("/fields", {
                    method: "POST",
                    headers: {
                      "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                  })
                  if (response.ok) {
                  settable(true)
                  }
                }}> GO </button>
              </form>
            </div>
          </div>
      }
    </div>
  );
}
export default HsData;
