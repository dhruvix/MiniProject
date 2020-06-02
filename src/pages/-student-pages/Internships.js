import React,{useState} from 'react'
import Table from '../../components/Table';
import Error from '../Error';
import Options from '../../components/Options';
import Graph from '../../components/Graph';
import '../Home.css';

function Internships(){
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

const options={x:["companyName","departmentId","year"],
             y:["NoOfStu"],
             year:["all","0","1","2","3","4"],
             dep:["all","cse","is","ece","ee","cv","bt","ch","im","it","mba","me","ml","te"],
             op:["ug","pg"]
            };

const names={x:["company name","department","year"],
            y:["No. of students"],
            year:["all years","current year","last year","last 2 years","last 3 years","last 4 years"],
            dep:["all","computer science","information science","electronics and communication","electrical engineering","civil engineering","biotechnology","chemical engineering","industrial management","information technology","MBA","mechanical engineering","medical electronics","telecommunication"],
            op:["UG","PG"]
           };

   return(       
      <div>
      {component?(<Options submithandler= {submithandler} options={options} names={names} table="internship"/>):
          (type1==="data")?
          (<Table tabledata={data} fields={graph}/>)
          :(type1==="graph")?<Graph data={graph}/>:<Error />
      }
              </div>         
  );
}

export default Internships;