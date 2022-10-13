import React, { Fragment, useState } from "react";

import { isAuth } from "../../hoc/isAuth";
import MapBox from "./Map";
import NavBar from "../../components/NavBar";

import "./styles.scss";

const MapWrapp = () => {
  const [zoomState, setZoomState] = useState({
    type: "regions",
    code: null
  })
  return(
    <div className="map-wrapp">
      <NavBar zoomState={zoomState} setZoomState={setZoomState}/>
      <MapBox zoomState={zoomState} setZoomState={setZoomState}/>
    </div>
  )
};

export default isAuth(MapWrapp);
