import React from 'react';
import SeStyles from './Searchplants.module.css';
import Topbar from './Topbar';

function Searchplants() {
    return(
        <>
            <Topbar />
            <input className={`${SeStyles.PlantSe}`}></input>
            <img className={`${SeStyles.SearchButton}`} src={process.env.PUBLIC_URL+"./img/Search.png"} alt="Search"></img>
            <div className={`${SeStyles.RecentHistoryCaption}`}>
                # 최근 검색 기록
            </div>

        </>
    )
}

export default Searchplants;