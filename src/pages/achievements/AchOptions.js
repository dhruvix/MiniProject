import React,{useState} from 'react'
import axios from 'axios';
import '../Home.css';


function IOptions({submithandler}) {
    const [intern, setIt] = useState({tab:"internship",x:"companyName",y:"NoOfStu",dep:"all",year:"all",op:"ug"})

    function handleChange(event) {
        event.persist()
      setIt({...intern,[event.target.name]:event.target.value}); 
   }

    async function submitHandler(e) {
        e.preventDefault()
        e.persist()
        if (e.target.value === "data") {
         await axios.post('/data',intern).then(res => {
              submithandler(res.data,e.target.value,intern)
          }).catch(err => console.log(err))
        }
        if (e.target.value === "graph"){
          submithandler(null,e.target.value,intern);
        }
    }


    return(
      <div className="mainbox">
        <div className="card1">

          <form >
            <div>
            
              <h3>Choose parameters</h3>
              <div className="together">
                <h5>x:</h5>
                <select className="select-css" id="x" name="x" onChange={handleChange}>
                  <option value="companyName">company name</option>
                  <option value="year">year</option>
                  <option value="departmentId">department</option>
                </select>
              </div>

              <div className="together">
                <h5>y:</h5>
                <select className="select-css" id="y" name="y" onChange={handleChange}>
                  <option value="NoOfStu">no. of students</option>
                </select>
              </div>

              <div className="together">
                <h5>year:</h5>
                <select className="select-css" id="year" name="year" onChange={handleChange}>
                  <option value="all">all years</option>
                  <option value="0">current year</option>
                  <option value="1">last year</option>
                  <option value="2">last 2 years</option>
                  <option value="3">last 3 years</option>
                  <option value="4">last 4 years</option>
                </select>
              </div>

              <div className="together">
                <h5>department:</h5>
                <select className="select-css" id="dep" name="dep" onChange={handleChange}>
                  <option value="all">all</option>
                  <option value="cse">computer science</option>
                  <option value="is">information science</option>
                  <option value="ece">electronics and communication</option>
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

              <div className="together">
                <h5>UG/PG:</h5>
                <select className="select-css" id="op" name="op" onChange={handleChange}>
                  <option value="ug">UG</option>
                  <option value="pg">PG</option>
                </select>
              </div>

              <h4>Data or Graph:</h4>
              <div className="buttline">
                <button type="submit" className="butt" value="data" onClick={submitHandler}>data</button>
                <button type="submit" value="graph" className="butt" onClick={submitHandler}>graph</button>
              </div>

            </div>
          </form>
        
        </div>
      </div>
    )
}

export default IOptions;

