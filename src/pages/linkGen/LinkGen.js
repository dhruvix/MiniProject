import React,{useState} from 'react';
import './LinkGen.css';
import Logo from '../../components/Logo';

function LinkGen() {

    const [name, setName] = useState("");
    const [disp, setDisp] = useState(false);
    const [links, setLink] = useState([]);
    const [loading,setLoading]=useState(false)
    function handleName(event){
        setName(event.target.value);
    }

    function handleSubmit(){
        console.log("name passed",name);
        setLoading(true);
        fetch(`http://localhost:9000/api/linkgen?paper=${name}`).then(res=>res.json())
        .then(data => {
            console.log(data);
            setLink(data.links);
            console.log("returned list:",data.links);
            setLoading(false)
            setDisp(true);
        })
        .catch(err => {console.log(err); alert("no paper found")});
    }
    return (
        <div>
            <div style={{marginTop:'10px'}}>
                <Logo />
            </div>
        <div className="cardHolder">
            {
                loading ? 
                (<div className="paper-load">
                    <h3>Searching...</h3>
                </div>)
                :
                (<div className="body-part">
            <h3 style={{position:"relative", left:"70px"}}>Generate Research Paper Link</h3>
            <div className="form">
                <fieldset>
                    <input type="text" onChange={handleName} autoComplete="off" placeholder="enter the name of the research paper"/>
                </fieldset>
                <fieldset>
                    <input type="submit" value="Get Link" onClick={handleSubmit} />
                </fieldset>
            </div>
            {
            disp?(
                <div className="retbox">
                <h4>Generated links:</h4>
                {links.map((a,i)=>{
                return(<div key={i}>
                    <p><span role="img" aria-label="point">👉</span>{a}</p>
                    <a href={a} target="_blank" rel="noopener noreferrer">click to visit</a>
                </div>)
                })}
                </div>
            ):null
            }
        </div>)
            }
        </div>
        </div>
    )
}

export default LinkGen;



