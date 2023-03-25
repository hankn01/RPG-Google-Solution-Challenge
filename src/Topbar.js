import React from 'react';
import styles from './Topbar.module.css';


function Topbar() {

    return(
    <>
    
    <div className={`${styles.TopbarBackground}`}>
    <img className={`${styles.LOGO}`} src={process.env.PUBLIC_URL+"./img/RPG.png"} alt="RPG Logo"></img>
       <div className={`${styles.TopBarHome}`}>
            <h2 className={`${styles.TopBarText}`}>
                홈
            </h2>
       </div>
       <div className={`${styles.TopBarFindPlants}`}>
            <h2 className={`${styles.TopBarText}`}>
                식물 찾기
            </h2>
       </div>
       <div className={`${styles.TopBarManage}`}>
            <h2 className={`${styles.TopBarText}`}>
                식물 관리
            </h2>
       </div>
       
    </div>
    </>
    );


}

export default Topbar;