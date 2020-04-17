import React from 'react';
import Error from '../pages/Error';
import Table1 from './Table1';

function Table({tabledata,fields}) {

    console.log("length:",tabledata.length)
    return (
        <div>
        {
            (tabledata.length === 0 || !tabledata)?(<Error />)
            :
            (<Table1 tabledata={tabledata} fields={fields} />)
        }
        </div>
    )
}

export default Table;
