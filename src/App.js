import React, { useEffect, useState, useRef } from "react";
import {BrowserRouter, Route, Routes } from 'react-router-dom';
import axios from "axios";
import Home from './Home';
import Searchplants from "./Searchplants";
import PlantsInfo from './PlantsInfo';
import PlacePlants from "./PlacePlants";

function App() {
  return(

    <>
    <BrowserRouter>
     
      <Routes>
        <Route path="/" element={<PlantsInfo />} />
        <Route path="/page1" element={<Searchplants />} />
        <Route path="/page2" element={<PlantsInfo />} />
        <Route path="/page3" element={<PlacePlants />} />
      </Routes>
    </BrowserRouter>
      
    </>
  )


}

/*
const Survey = () => {
    
  const onSubmit = async (e) => {
    e.preventDefault();
    e.persist();

    let files = e.target.profile_files.files;
    let formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i]);
    }

    let dataSet = {
      name: "Hong gil dong",
      phone: "010-1234-1234",
      birth: "2001-09-11",
    };

    formData.append("image", JSON.stringify(dataSet));

    const postSurvey = await axios({
      method: "POST",
      url: `http://34.22.73.155:8000/service/image_test/`,
      mode: "cors",
      headers: {
        "Content-Type": "multipart/form-data",
      },
      data: formData,
    });

    console.log(postSurvey);
  };

  return (
    <form onSubmit={(e) => onSubmit(e)}>
      <input
        type="file"
        name="profile_files"
        multiple="multiple"
      />

      <button type="submit">제출</button>
    </form>
  );
};

export default Survey;

*/

/*
const [image, setImage] = useState("");

const handleSubmit = (e) => {
  e.preventDefault();
  const formData = new FormData();
  console.log("이미지");
  console.log(image);
  formData.append('image', image);
  // 여기서 `image`는 base64로 인코딩된 이미지 데이터입니다.
  // 나머지 필드를 필요에 따라 추가할 수 있습니다.
  // ...

  console.log("전송되는 데이터입니다.");
  console.log(formData.image);
  const postSurvey = axios({
    method: "POST",
    url: `http://34.22.73.155:8000/service/image_test/`,
    mode: "cors",
    headers: {
      "Content-Type": "multipart/form-data",
    },
    data: formData,
  }).then((response) =>{
    console.log(response);
  });
  // formData 객체를 사용하여 서버로 데이터 전송
  // ...
};

const handleFileChange = (e) => {
  const file = e.target.files[0];
  const reader = new FileReader();

  reader.onload = () => {
    setImage(reader.result);
    console.log("리더리설트");
    console.log(reader.result);
    // 여기서 `reader.result`는 base64로 인코딩된 이미지 데이터입니다.
  };

  reader.readAsDataURL(file);
};

return (
  <form onSubmit={handleSubmit}>
    <input type="file" onChange={handleFileChange} />
    <button type="submit">Submit</button>
  </form>
);

}

export default App;
*/

export default App;