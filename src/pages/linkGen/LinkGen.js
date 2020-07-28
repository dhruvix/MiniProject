import React,{useState} from 'react';
import './LinkGen.css';
import Logo from '../../components/Logo';

function LinkGen() {

    const [name, setName] = useState("");
    const [disp, setDisp] = useState(false);
    const [links, setLink] = useState([]);
    const [loading,setLoading]=useState(false);
    const [timing, setTime] = useState(0);
    function handleName(event){
        setName(event.target.value);
    }

    function handleSubmit(){
        console.log("name passed",name);
        setLoading(true);
        fetch(`http://localhost:9000/api/linkgen?paper=${name}`).then(res=>res.json())
        .then(data => {
            console.log(data);
            if(data.message==="success" && data.links.length>0){
                setLink(data.links);
                setTime(data.time)
                setLoading(false);
                setDisp(true);
            }
            else{
                console.warn(data.message);
                setLoading(false);
                alert("error in fetching papers");
            } 
        })
        .catch(err => {
            console.log(err);
            setLoading(false);
            alert("no paper found")
        });
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
                    <input type="text" value={name} onChange={handleName} autoComplete="off" placeholder="enter the name of the research paper"/>
                </fieldset>
                <fieldset>
                    <input type="submit" value="Get Link" onClick={handleSubmit} />
                </fieldset>
            </div>
            {
            disp?(
                <div className="retbox">
                <h4>Generated links:</h4>
                <div>
                {links.map((a,i)=>{
                return(
                    <div key={i} className="retlink" onClick={()=>window.open(a.url,"_blank")}>&#10149; {a.site} </div>
                    )
                })}
                </div>
                <h6 style={{marginTop:"10px"}}>Search took {timing}ms</h6>
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



