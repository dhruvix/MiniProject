import React from 'react';
import './Tables.css';
import ReactToExcel from 'react-html-table-to-excel';


function Table1({tabledata,fields}) {
    console.log("type:",typeof(tabledata))
    console.log("returned data:",tabledata)
    const keys=Object.keys(tabledata[0])
    console.log("headers:",keys)
    
    return (
        <div>
            <div className="tabular">
            <table id="tab1" className="tabl">
                <tr>
                {
                    keys.map((k)=>{
                        return(
                            <th>{k}</th>
                        )
                    })
                }
                </tr>
            {
                tabledata.map((a)=>{
                    return(
                        <tr>
                        {
                            keys.map((k)=>{
                                return(
                                    <td>{a[k]}</td>
                                )
                            })
                        }
                        </tr>
                    );
                })
            } 
            </table>
            <ReactToExcel className="butt" table="tab1" filename={fields['tab']} sheet="sheet1" buttonText="Generate Excel File" />
        </div>
        </div>
    ) 
}
 
export default Table1;                    