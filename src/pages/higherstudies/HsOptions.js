// import React,{useState} from 'react'
// import axios from 'axios';
// import '../Home.css';


// function HsOptions({submithandler}) {
//     const [hstudies, setIt] = useState({tab:"higher_studies",x:"country",y:"NoOfStu",dep:"all",year:"all"})

//     function handleChange(event) {
//         event.persist()
//       setIt({...hstudies,[event.target.name]:event.target.value}); 
//    }

//     async function submitHandler(e) {
//         e.preventDefault()
//         e.persist()
//         if (e.target.value === "data") {
//          await axios.post('/data',hstudies).then(res => {
//               submithandler(res.data,e.target.value,hstudies)
//           }).catch(err => console.log(err))
//         }
//         if (e.target.value === "graph"){
//           submithandler(null,e.target.value,hstudies);
//         }
//     }


//     return(
//       <div className="mainbox">
//         <div className="card1">

//           <form >
//             <div>
            
//               <h3>Choose parameters</h3>
//               <div className="together">
//                 <h5>x:</h5>
//                 <select className="select-css" id="x" name="x" onChange={handleChange}>
//                   <option value="country">country</option>
//                   <option value="yearOfPassing">year of passing</option>
//                   <option value="departmentId">department</option>
//                   <option value="course">course</option>
//                   <option value="program">program</option>
//                 </select>
//               </div>

//               <div className="together">
//                 <h5>y:</h5>
//                 <select className="select-css" id="y" name="y" onChange={handleChange}>
//                   <option value="NoOfStu">no. of students</option>
//                 </select>
//               </div>

//               <div className="together">
//                 <h5>year:</h5>
//                 <select className="select-css" id="year" name="year" onChange={handleChange}>
//                   <option value="all">all</option>
//                   <option value="2019">2019</option>
//                   <option value="2018">2018</option>
//                   <option value="2017">2017</option>
//                   <option value="2016">2016</option>
//                   <option value="2015">2015</option>
//                 </select>
//               </div>

//               <div className="together">
//                 <h5>department:</h5>
//                 <select className="select-css" id="dep" name="dep" onChange={handleChange}>
//                   <option value="all">all</option>
//                   <option value="cse">computer science</option>
//                   <option value="is">information science</option>
//                   <option value="ece">electronics and communication</option>
//                   <option value="ee">electrical engineering</option>
//                   <option value="cv">civil engineering</option>
//                   <option value="bt">biotechnology</option>
//                   <option value="ch">chemical engineering</option>
//                   <option value="im">industrial management</option>
//                   <option value="it">information technology</option>
//                   <option value="mba">MBA</option>
//                   <option value="me">mechanical engineering</option>
//                   <option value="ml">medical electronics</option>
//                   <option value="te">telecommunication</option>
//                 </select>
//               </div>

//               <h4>Data or Graph:</h4>
//               <div className="buttline">
//                 <button type="submit" className="butt" value="data" onClick={submitHandler}>data</button>
//                 <button type="submit" value="graph" className="butt" onClick={submitHandler}>graph</button>
//               </div>

//             </div>
//           </form>
        
//         </div>
//       </div>
//     )
// }

// export default HsOptions
