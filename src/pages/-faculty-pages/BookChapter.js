import React,{useState} from 'react'
import Table from '../../components/Table1';
import Error from '../Error';
import Options from '../../components/Options';
import Graph from '../../components/Graph';
import '../Home.css';

function BookChapter(){
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

const options={x:["departmentId","year"],
             y:["No of Books"],
             year:["all","2019"],
             dep:["all","cse","is","ece","ee","cv","bt","ch","im","it","mba","me","ml","te","ar","chy","data","mat","mca","phy"]
            };

const names={x:["department","year"],
            y:["No. of Books"],
            year:["all","2019"],
            dep:["all","computer science","information science","electronics and communication","electrical engineering","civil engineering","biotechnology","chemical engineering","industrial management","information technology","MBA","mechanical engineering","medical electronics","telecommunication","architecture","chemistry","data science","mathematics","MCA","physics"]
           };

   return(       
      <div>
      {component?(<Options submithandler= {submithandler} options={options} names={names} table="book_chapter"/>):
          (type1==="data")?
          (<div><Table tabledata={data} fields={graph}/></div>)
          :(type1==="graph")?<Graph data={graph}/>:<Error />
      }
              </div>         
  );
}

export default BookChapter;