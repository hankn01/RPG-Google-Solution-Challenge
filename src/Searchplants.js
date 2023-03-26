import React from 'react';
import SeStyles from './Searchplants.module.css';
import Topbar from './Topbar';

function Searchplants() {
    return(
        <>
            <Topbar />
            <input className={`${SeStyles.PlantSe}`}></input>


        </>
    )
}

export default Searchplants;