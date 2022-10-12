import React, { Fragment } from "react";

import { isAuth } from "../../hoc/isAuth";
import MapBox from "./Map";
import NavBar from "../../components/NavBar";

import "./styles.scss";

const MapWrapp = () => (
  <div className="map-wrapp">
    <NavBar />
    <MapBox />
  </div>
);

export default isAuth(MapWrapp);
