import React,{useState} from 'react'
import Options from '../../components/Options';
import Table from '../../components/Table';
import Error from '../Error';
import Graph from '../../components/Graph';
import '../Home.css';

function HigherStudies(){
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

const options={x:["country","yearOfPassing","departmentId","course","program"],
             y:["NoOfStu"],
             year:["all","2019","2018","2017","2016","2015"],
             dep:["all","cse","is","ece","ee","cv","bt","ch","im","it","mba","me","ml","te"]
            };

const names={x:["country","year of passing","department","course","program"],
            y:["No. of students"],
            year:["all","2019","2018","2017","2016","2015"],
            dep:["all","computer science","information science","electronics and communication","electrical engineering","civil engineering","biotechnology","chemical engineering","industrial management","information technology","MBA","mechanical engineering","medical electronics","telecommunication"]
           };

  return(       
      <div>
      {component?
      (<Options submithandler= {submithandler} options={options} names={names} table="higher_studies" />):
          (type1==="data")?
          (<div><Table tabledata={data} fields={graph}/></div>)
          :(type1==="graph")?<Graph data={graph}/>:<Error />
      }
              </div>         
  );
}

export default HigherStudies;

