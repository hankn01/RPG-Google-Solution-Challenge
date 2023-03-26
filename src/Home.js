import React from 'react';
import Topbar from './Topbar.js';
import HStyles from './Home.module.css';

function Home(){


    return(
    <>
    
    <Topbar />
    <div className={`${HStyles.LoginForm}`}>
        <input className={`${HStyles.Input}`}></input>
        <input className={`${HStyles.Input}`}></input>
        <br />
        <button className={`${HStyles.Button}`}>로그인</button>
        <button className={`${HStyles.Button}`}>회원가입</button>
    </div>
    </>
    );



}
export default Home;