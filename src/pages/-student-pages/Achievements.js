import React,{useState} from 'react'
import Table from '../../components/Table';
import Error from '../Error';
import Options from '../../components/Options';
import Graph from '../../components/Graph';
import '../Home.css';

function Achievements(){
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

const options={x:["type","departmentId","year"],
             y:["NoOfStu"],
             year:["all","2019","2018","2017","2016","2015"],
             dep:["all","cse","is","ece","ee","cv","bt","ch","im","it","mba","me","ml","te"],
             op:["ug","pg"]
            };

const names={x:["type of event","department","year"],
            y:["No. of students"],
            year:["all","2019","2018","2017","2016","2015"],
            dep:["all","computer science","information science","electronics and communication","electrical engineering","civil engineering","biotechnology","chemical engineering","industrial management","information technology","MBA","mechanical engineering","medical electronics","telecommunication"],
            op:["UG","PG"]
           };

   return(       
      <div>
      {component?(<Options submithandler= {submithandler} options={options} names={names} table="student_achievement"/>):
          (type1==="data")?
          (<Table tabledata={data} fields={graph}/>)
          :(type1==="graph")?<Graph data={graph}/>:<Error />
      }
              </div>         
  );
}

export default Achievements;