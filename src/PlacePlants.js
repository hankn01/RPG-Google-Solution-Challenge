import React from 'react';
import Topbar from './Topbar';
import PPStyles from './PlacePlants.module.css';

function PlacePlants() {
    return(
        <>
        <Topbar />
            <div className={`${PPStyles.PlantsNameCaption}`}>
                식물 이름
            </div>


        </>
    );
}

export default PlacePlants;