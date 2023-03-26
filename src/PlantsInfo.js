import React from 'react';
import Topbar from './Topbar';
import PIStyles from './PlantsInfo.module.css';


function PlantsInfo() {
    return(
        <>
            <Topbar />
            <div className={`${PIStyles.PlantsTile}`}></div>
            <div className={`${PIStyles.PlantsInnerTile}`}></div>


            

        </>
    )
}

export default PlantsInfo;