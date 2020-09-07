import React, { useState } from 'react'
import axios from 'axios'
import Logo from '../../components/Logo';
import Analy from '../../components/Analy';

function Upload() {
    const [file,setFile] = useState();
    const [dis, setDis] = useState(true);
    const [res, setRes] = useState(false);
    const [anal, setAnal] = useState({});

    function change(e){
        let file = e.target.files[0]
        setFile(file)
    }
    function upload(e){
     
        let formData = new FormData();
        formData.append('file',file)
        formData.append('name',"harsha")
    //   axios({
    //       url:'http://127.0.0.1:5000/file',
    //       method:"get",
    //       data:file
    //   }).then(res=>{
    //       console.log(res)
    //   })
      axios.post('http://127.0.0.1:5000/file',
     formData
    ).then(function (res) {
      console.log('SUCCESS!!');
      setAnal(res.data);
      setDis(false);
      alert("file uploaded!")
    })
    .catch(function () {
      console.log('FAILURE!!');
      alert("file couldn't be uploaded.");
    });
    }

    function analytics(){
        setRes(true);
    }

    return (
        <div>
            <div style={{ marginTop: '10px' }}>
                <Logo />
            </div>
            {
                !res ? 
                (
                    <div className="center">
                        <div className="body-part">
                            <h3 style={{ "textAlign": "center" }}>Student analytics</h3>
                            <div className="form">
                                <fieldset>
                                    <input type="file" className="fileup" onChange={change}></input><br />
                                </fieldset>
                                <fieldset>
                                    <input type="submit" value="Upload" onClick={upload} />
                                    <input type="submit" value="Analytics" disabled={dis} onClick={analytics} />
                                </fieldset>
                            </div>
                        </div>
                    </div>
                )
                    :
                (
                    <Analy data={anal} />
                )
            }
        </div>
    )
}

export default Upload;

