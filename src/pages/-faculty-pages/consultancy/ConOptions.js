import React,{useState} from 'react'
import axios from 'axios';
import '../../Home.css';
import Logo from '../../../components/Logo';

const depid = ["all","cse","is","ece","ee","cv","bt","ch","im","it","mba","me","ml","te","ar","chy","data","mat","mca","phy"];
const depname = ["all","computer science","information science","electronics and communication","electrical engineering","civil engineering","biotechnology","chemical engineering","industrial management","information technology","MBA","mechanical engineering","medical electronics","telecommunication","architecture","chemistry","data science","mathematics","MCA","physics"];

function ConOptions({submithandler})
{
  const [yvalue, sety] = useState(true);
  let obj
  if(!yvalue)
  obj={tab:"consultancy",x:"departmentId",y:"No of Con",dep:"all",year:"all"} 
  else
  obj={tab:"consultancy",x:"role",y:"No of Fac",dep:"all",year:"all"}
  const [hstudies, setIt] = useState(obj);
  
  function handle(event){
    event.persist()
        if(event.target.value==="No of Con"){
          sety(false);
          obj={tab:"consultancy",x:"departmentId",y:"No of Con",dep:"all",year:"all"}
          setIt(obj)
        }
        else if(event.target.value==="No of Fac"){
          sety(true);
        }
  }
    function handleChange(event) {
        event.persist()
      
      setIt({...hstudies,[event.target.name]:event.target.value});
   }

    async function submitHandler(e) {
        e.preventDefault()
        e.persist()
        if (e.target.value === "data") {
         await axios.post('/data',hstudies).then(res => {
              submithandler(res.data,e.target.value,hstudies)
          }).catch(err => console.log(err))
        }
        if (e.target.value === "graph"){
          submithandler(null,e.target.value,hstudies);
        }
    }

    return (
        <div>
        <div style={{marginTop:'10px'}}>
        <Logo />
        </div>
        <div className="cardHolder">
        <div className="card2">

          <form >
            <div>
            
              <h3>Choose parameters</h3>
              
              {!yvalue?
              <div className="together">
                <h5>x:</h5>
                <select className="select-css" id="x" name="x" onChange={handleChange} >
                <option value="departmentId">department</option>
                <option value="year">year</option>
                </select>
              </div>
              :
              <div className="together">
                <h5>x:</h5>
                <select className="select-css" id="x" name="x" onChange={handleChange}>
                <option value="role">role</option>
                <option value="typeOfConsultancy">type of Consultancy</option>
                </select>
              </div>}

              <div className="together">
                <h5>y:</h5>
                <select className="select-css" id="y" name="y" onChange={handleChange} onClick={handle}>
                <option value="No of Fac">no. of faculty members</option>
                <option value="No of Con">no. of Consultancies</option>
                </select>
              </div>

              <div className="together">
                <h5>department:</h5>
                <select className="select-css" id="dep" name="dep" onChange={handleChange}> 
                  {
                    depid.map((did,i)=>{
                      return(
                        <option value={did}>{depname[i]}</option>
                      )
                    })
                  }
                </select>
              </div>

              <div className="together">
                <h5>year:</h5>
                <select className="select-css" id="year" name="year" onChange={handleChange}>
                  <option value="all">all</option>
                  <option value="2019">2019</option>
                  <option value="2018">2018</option>
                  <option value="2017">2017</option>
                  <option value="2016">2016</option>
                  <option value="2015">2015</option>
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
      </div>
    )
}

export default ConOptions