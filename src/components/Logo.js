import React from 'react';
import Tilt from 'react-tilt';
import logoface from './logoface.png';
import {useHistory} from 'react-router-dom';
import './Logo.css';
import 'tachyons';

function Logo() {
    const history = useHistory();
    return (
        <div className='ma4 mt0'>
            <Tilt className="Tilt br2 shadow-2" options={{ max: 55}} style={{ height: 100, width: 100 }} >
                <div className="Tilt-inner pa3">
                    <img style={{ paddingTop: '3px'}} alt='logo' src={logoface} onClick={()=>history.push('/home')} />
                </div>
            </Tilt>
        </div>
    )
}

export default Logo;