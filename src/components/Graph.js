import React from 'react';
import '../pages/Home.css';

function Graph({data}) {
    const key=Object.keys(data)
    console.log(data);
    console.log(key.length)
    let url='http://127.0.0.1:5000/graph?'
    url=url+'tab='+data.tab
    for(let i=1;i<key.length;i++){
        url=url+'&'+key[i]+'='+data[key[i]]
    }
    console.log(url)
    return (
        <div className="mainbox">
        <div className="card1">
            <img alt="🥺" src={url} />
        </div>
        </div>
    )
}

export default Graph;