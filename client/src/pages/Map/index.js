import React, { Fragment } from "react";

import { isAuth } from "../../hoc/isAuth";
import MapBox from "./Map";

const MapWrapp = () => (
  <Fragment>
    <MapBox />
  </Fragment>
);

export default isAuth(MapWrapp);
