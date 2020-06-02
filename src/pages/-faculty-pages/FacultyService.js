import React,{useState} from 'react'
import Table from '../../components/Table1';
import Error from '../Error';
import Options from '../../components/Options';
import Graph from '../../components/Graph';
import '../Home.css';

function FacultyService(){
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

const options={x:["designation"],
            y:["nof"],
            current_or_all:["current","all"]
            };

const names={x:["designation"],
            y:["No. of faculty members"],
            current_or_all:["current","all"]
            };

   return(       
      <div>
      {component?(<Options submithandler= {submithandler} options={options} names={names} table="faculty_service"/>):
          (type1==="data")?
          (<div><Table tabledata={data} fields={graph}/></div>)
          :(type1==="graph")?<Graph data={graph}/>:<Error />
      }
              </div>         
  );
}

export default FacultyService;