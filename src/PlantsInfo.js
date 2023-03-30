import React from 'react';
import Topbar from './Topbar';
import PIStyles from './PlantsInfo.module.css';
import { useState, useEffect, useRef} from 'react';
import axios from 'axios';

function PlantsInfo() {
    useEffect(() => {
        return() => preview();
    });

    const imageInput = useRef();
 
  const onCickImageUpload = () => {
    imageInput.current.click();
  };
    const preview = () => {
        if(!files) return false;
        
        const imgEL = document.querySelector('.img_box');

        const reader = new FileReader();

        reader.onLoad = () =>
        (imgEL.style.backgroundImage = `url(${reader.result})`);

        reader.readAsDataURL(files[0]);
    }
    const [fileImage, setFileImage] = useState("");
    const [files, setFiles] = useState('');
    const [res, setRes] = useState({});
    
    const [watering, setWatering] = useState('');
    const [airp, setAirp] = useState('');
    const [sunp, setSunp] = useState('');
    const [purp, setPurp] = useState('');


    const onLoadFile = (e) => {
        const file = e.target.files;
        console.log(file);
        setFiles(file);
    }



    function handleSubmit(event) {
        event.preventDefault()
      }

    const handleClick = (e) => {
        const formdata = new FormData();
        formdata.append('image', files[0]);

        setFileImage(URL.createObjectURL(files[0]));
        const config = {
            Headers: {
                'content-type' : 'application/json',
            },
        };

        axios.post('https://rpgplant.kro.kr/service/inference/', formdata, config)
        .catch((error) =>{
            console.log(error);
        })
        .then((response) => {
            console.log(response.data[0]);
            setRes(response.data[0]);
        });
        console.log(res);
    }

    return(
        <>
            <Topbar />
            <div className={`${PIStyles.PlantsTile}`}>
                <div className={`${PIStyles.PlantsTitleCaption}`}>
                    {fileImage?res.plant_name:<div>식물 이름</div>}
                    <br />
                   

                </div>
                <br />
                <br />
                <br />
                <br />
                
                <div className={`${PIStyles.InnerTileCon}`}>
                {fileImage?res.description:<div></div>}
                </div>

                


            </div>
            <div className={`${PIStyles.PlantsInnerTile}`}>
                {fileImage?<div className={`${PIStyles.imgwrap}`}>
                <img className={`${PIStyles.imgc}`} src={fileImage} alt="" />
                </div>:<div className={`${PIStyles.imgwrap}`}>
                <div className={`${PIStyles.InnerTileText}`}><br /><br /><br /><br /><br />파일을 선택하여 업로드해 주세요.</div>

                    
                    </div>}
                
            
                <div className={`${PIStyles.InnerTTDiv}`}>
                <div className={`${PIStyles.InnerTileText}`}># 물주기</div>
                <br /><div className={`${PIStyles.InnerTileCon}`}>봄: {res.spring_water_cycle}</div>
                <br /><div className={`${PIStyles.InnerTileCon}`}>여름: {res.summer_water_cycle}</div>
                <br /><div className={`${PIStyles.InnerTileCon}`}>가을: {res.autumn_water_cycle}</div>

                <br /><div className={`${PIStyles.InnerTileCon}`}>겨울: {res.winter_water_cycle}</div>

                <div className={`${PIStyles.InnerTileText}`}># 식물 성장 형태</div>
                <br /><div className={`${PIStyles.InnerTileCon}`}>생태계: {res.eclogy_type}</div>
                <br /><div className={`${PIStyles.InnerTileCon}`}>잎의 색: {res.leaf_color}</div>

                <div className={`${PIStyles.InnerTileText}`}># 일조량</div>
              
                <br /><div className={`${PIStyles.InnerTileCon}`}>{res.light_demand}</div>
                <br />
              

                <div className={`${PIStyles.InnerTileText}`}># 온도 및 습도</div>
                <br /><div className={`${PIStyles.InnerTileCon}`}>성장 온도: {res.grow_temperature}</div>
                <br /><div className={`${PIStyles.InnerTileCon}`}>성장 습도: {res.grow_humidity}</div>
               
                </div>


                <br />
                <br />
                <br />
                


                <div className={`${PIStyles.upwrap}`}>
                {files[0]?<div className={`${PIStyles.InnerTileCon}`}>파일이 선택되었습니다. 업로드 버튼을 클릭해 주세요. <br />파일이름 : {files[0].name}</div>:null}

            <form className="upload_input" onSubmit={handleSubmit}>
                <input type="file" id="imgae" style={{ display: "none" }} accept="img/*" onChange={onLoadFile} ref={imageInput}/>

                <button className={`${PIStyles.Button}`} onClick={onCickImageUpload}>파일 선택</button>
                <button className={`${PIStyles.Button}`} onClick={handleClick}>업로드</button>
            
            </form>

            </div>

            </div>
            
            

            

        </>
    )
}

export default PlantsInfo;