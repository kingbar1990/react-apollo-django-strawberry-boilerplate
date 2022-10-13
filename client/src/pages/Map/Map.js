import React, { useEffect, useState } from "react";

import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet';

import MapContent from "./MapContent";

import geojson from "../../assets/Detail_Level_01_Regions_EPSG32629.json"
import geojson2 from "../../assets/Detail_Level_01_Regions_WGS84.json";
import geojson3 from "../../assets/Detail_Level_02_Communes_EPSG32629.json";
import geojson4 from "../../assets/Detail_Level_02_Communes_WGS84.json";
import geojson5 from "../../assets/Detail_Level_03_FarmLeaders_Farms_Fields_WGS84.json";

const MapBox = () => {

    // const [coordinates, setCoordinates] = useState([]);

    // useEffect(()=>{
    //     setCoordinates(JSON.parse(geojson.features).map(row=> [row[1], row[0]]))
    // },[])

    const setColor = ({ properties }) => {
        return { 
            "color": "#ff7800",
            "weight": 2,
            "opacity": 0.65
        };
      };

      const setColor2 = ({ properties }) => {
        return { 
            "color": "blue",
            "weight": 2,
            "opacity": 0.65
        };
      };

      const setColor3 = ({ properties }) => {
        return { 
            "color": "red",
            "weight": 2,
            "opacity": 0.65
        };
      };

      const setColor4 = ({ properties }) => {
        return { 
            "color": "green",
            "weight": 2,
            "opacity": 0.65
        };
      };

      const setColor5 = ({ properties }) => {
        return { 
            "color": "yellow",
            "weight": 2,
            "opacity": 0.65
        };
      };

    // React.useEffect(() => {
    //     const L = require("leaflet");
    
    //     delete L.Icon.Default.prototype._getIconUrl;
    
    //     L.Icon.Default.mergeOptions({
    //     iconRetinaUrl: require("leaflet/dist/images/marker-icon-2x.png"),
    //     iconUrl: require("leaflet/dist/images/marker-icon.png"),
    //     shadowUrl: require("leaflet/dist/images/marker-shadow.png")
    //     });
    // }, []);

    return(
        <div id="map">
            <MapContainer center={[32.333, -6.384]} zoom={5} scrollWheelZoom={true}>
                <TileLayer
                    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                    <MapContent />
                    {/* <GeoJSON key='geojson' data={geojson} style={setColor} />
                    <GeoJSON key='geojson2' data={geojson2} style={setColor2} />     
                    <GeoJSON key='geojson3' data={geojson3} style={setColor3} />   
                    <GeoJSON key='geojson4' data={geojson4} style={setColor4} />   
                    <GeoJSON key='geojson5' data={geojson5} style={setColor5} />    */}
            </MapContainer>
        </div>
    )
}

export default MapBox;