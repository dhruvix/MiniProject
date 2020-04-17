import React,{useState} from 'react'
import axios from 'axios';
import '../pages/Home.css';
import Logo from '../components/Logo';


function Options({submithandler, options, names, table}) {
    let obj={tab:table}
    let k=Object.keys(options)
    k.map((e,i)=>{
        obj[e]=options[e][0]
        return null
    })
    const [datastate, setIt] = useState(obj)
    
    function handleChange(event) {
        event.persist()
      setIt({...datastate,[event.target.name]:event.target.value}); 
   }

    async function submitHandler(e) {
        e.preventDefault()
        e.persist()
        if (e.target.value === "data") {
         await axios.post('/data',datastate).then(res => {
              submithandler(res.data,e.target.value,datastate)
          }).catch(err => console.log(err))
        }
        if (e.target.value === "graph"){
          submithandler(null,e.target.value,datastate);
        }
    }
   
    return(
      <div>
        <div style={{marginTop:'10px'}}>
        <Logo />
        </div>
        <div className="cardHolder">
        <div className="card2">

          <form >
            <div>
            
              <h3>Choose parameters:</h3>
                        {
                            k.map((e, i) => {
                                return (
                                    <div className="together">
                                        <h5>{e}:</h5>
                                        <select className="select-css" id={e} name={e} onChange={handleChange}>
                                            {options[e].map((o,j) => {
                                                return (
                                                    <option key={o} value={o}>{names[e][j]}</option>
                                                )
                                            })}
                                        </select>
                                    </div>
                                )
                            })

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

export default Options

