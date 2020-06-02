import React,{useState} from 'react'
import Table from '../../components/Table1';
import Error from '../Error';
import Options from '../../components/Options';
import Graph from '../../components/Graph';
import '../Home.css';

function FacWorkFDP(){
  const [type1,settype]=useState("none")
  const [component,setcomponent]=useState(true)
  const [data,setData]=useState([])
  const [graph,setGraph]=useState([])

const submithandler=(data1,typpe1,graph1)=>{
  setcomponent(false)
  console.log(data1)
  setData(data1)
  setGraph(graph1)
  settype(typpe1)
  console.log(data1)
}

const options={x:["sponsoredOrFunded","nationalOrInternational","type","role"],
            y:["nof"],
            year:["all","2019","2018","2017","2016","2015"]
            };

const names={x:["sponsored or funded","national or international","type of workshop FDP","role"],
            y:["No. of faculty members"],
            year:["all","2019","2018","2017","2016","2015"]
            };

   return(       
      <div>
      {component?(<Options submithandler= {submithandler} options={options} names={names} table="faculty_workshop_fdp"/>):
          (type1==="data")?
          (<div><Table tabledata={data} fields={graph}/></div>)
          :(type1==="graph")?<Graph data={graph}/>:<Error />
      }
              </div>         
  );
}

export default FacWorkFDP;