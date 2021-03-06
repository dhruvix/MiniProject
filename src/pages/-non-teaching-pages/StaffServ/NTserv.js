import React,{useState} from 'react'
import NTserveOp from './NTserveOp';
import Table from '../../../components/Table';
import Error from '../../Error';
import Graph from '../../../components/Graph';
import '../../Home.css';

function NTserv(){
  const [type1,settype]=useState("none")
  const [component,setcomponent]=useState(true)
  const [data,setData]=useState([])
  const [graph,setGraph]=useState([])

const submithandler=(data1,typpe1,graph1)=>{
  setcomponent(false)
  setData(data1)
  setGraph(graph1)
  settype(typpe1)
  console.log(data1)
  console.log(graph1)
}

  return(       
      <div>
      {component?
      (<NTserveOp submithandler= {submithandler} />):
          (type1==="data")?
          (<div><Table tabledata={data} fields={graph}/></div>)
          :(type1==="graph")?<Graph data={graph}/>:<Error />
      }
              </div>         
  );
}

export default NTserv;