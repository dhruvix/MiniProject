import React,{useState} from 'react';
import POptionsUG from './POptionsUG';
import POptionsPG from './POptionsPG';

function POptions({submithandler}) {

    const [op, setOp] = useState('ug');

    function changeOp(val){
        setOp(val);
        console.log("changed to",val)
    }

    return (
        <div>
            {
                (op === "ug") ?
                    (<POptionsUG submithandler={submithandler} changeOp={changeOp} />)
                    :
                    (<POptionsPG submithandler={submithandler} changeOp={changeOp} />)
            }
        </div>
    )
}

export default POptions;



