import React from 'react';
import Topbar from './Topbar';
import PIStyles from './PlantsInfo.module.css';


function PlantsInfo() {
    return(
        <>
            <Topbar />
            <div className={`${PIStyles.PlantsTile}`}>
                <div className={`${PIStyles.PlantsTitleCaption}`}>
                    식물 이름
                </div>

            </div>
            <div className={`${PIStyles.PlantsInnerTile}`}>
                <div className={`${PIStyles.InnerTileText}`}># 물주기</div>
                <div className={`${PIStyles.InnerTileText}`}># 환기</div>
                <div className={`${PIStyles.InnerTileText}`}># 일조량</div>
                <div className={`${PIStyles.InnerTileText}`}># 가지치기</div>
            </div>


            

        </>
    )
}

export default PlantsInfo;