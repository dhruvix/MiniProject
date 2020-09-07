import React from 'react';
import Table1 from './Table1';

function Analy({data}) {
    console.log(data)
    return (
        <div>
            {
                data.map((item)=>{
                   const keys= Object.keys(item)
                   const key=keys[0]
                   console.log(item[key])
                    return(
                        <Table1 tabledata={item[key]} fields={item[key]} />
                    )
                })
            }
        </div>
    )
}

export default Analy;

