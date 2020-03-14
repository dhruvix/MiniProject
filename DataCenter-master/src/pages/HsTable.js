import React from 'react';
import './Tables.css'

function HsTable({hsdata}) {
    
    // var b=JSON.parse(hsdata)
    var i;
    return (
        <div className="tabular">
            <table className="tabl">
                <tr>
                    <th>serial no.</th>
                    <th>name</th>
                    <th>USN</th>
                    <th>year of passing</th>
                    <th>program</th>
                    <th>course</th>
                    <th>university</th>
                    <th>country</th>
                    <th>year of joining</th>
                    <th>department id</th>
                </tr>
            {
                hsdata.map((a,i)=>{
                    return(
                        <tr>
                        <td>{a.slNo}</td>
                        <td>{a.studentName}</td>
                        <td>{a.usn}</td>
                        <td>{a.yearOfPassing}</td>
                        <td>{a.program}</td>
                        <td>{a.course}</td>
                        <td>{a.university}</td>
                        <td>{a.country}</td>
                        <td>{a.yearOfJoining}</td>
                        <td>{a.departmentId}</td>
                        </tr>
                    );
                })
            } 
            </table>
        </div>
    ) 
}
 
export default HsTable;
