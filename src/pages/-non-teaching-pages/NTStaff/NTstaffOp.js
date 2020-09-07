import React,{useState} from 'react'
import axios from 'axios';
import '../../Home.css';
import Logo from '../../../components/Logo';

const depid = ["all","cse","is","ece","ee","cv","bt","ch","im","it","mba","me","ml","te","ar","chy","data","mat","mca","phy"];
const depname = ["all","computer science","information science","electronics and communication","electrical engineering","civil engineering","biotechnology","chemical engineering","industrial management","information technology","MBA","mechanical engineering","medical electronics","telecommunication","architecture","chemistry","data science","mathematics","MCA","physics"];

function NTstaffOp({submithandler})
{
  const [yvalue, sety] = useState(true);
  let obj
  if(!yvalue)
  obj={tab:'non_teaching_staff',x:"departmentId",y:'No of Staff'} 
  else
  obj={tab:'non_teaching_staff',x:"gender",y:"No of Staff",dep:"all"}
  const [hstudies, setIt] = useState(obj);
  
  function handle(event){
    event.persist()
        if(event.target.value==='departmentId'){
          sety(false);
          obj={tab:"non_teaching_staff",x:"departmentId",y:'No of Staff'}
          setIt(obj)
        }
        else{
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

              <div className="together">
                <h5>x:</h5>
                <select className="select-css" id="x" name="x" onChange={handleChange} onClick={handle}>
                <option value="gender">gender</option>
                <option value="departmentId">department</option>
                <option value="category">category</option>
                </select>
              </div>

              <div className="together">
                <h5>y:</h5>
                <select className="select-css" id="y" name="y" onChange={handleChange} >
                <option value="No of Staff">no. of staff members</option>
                </select>
              </div>

            {
                yvalue ?
                    (
                        <div className="together">
                            <h5>department:</h5>
                            <select className="select-css" id="dep" name="dep" onChange={handleChange}>
                                {
                                    depid.map((did, i) => {
                                        return (
                                            <option value={did}>{depname[i]}</option>
                                        )
                                    })
                                }
                            </select>
                        </div>
                    )
                    :
                    (null)
            }

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

export default NTstaffOp