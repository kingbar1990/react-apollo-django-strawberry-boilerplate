import React, { useEffect, useState, useRef } from "react";

import { MapContainer, TileLayer, GeoJSON, useMap } from 'react-leaflet';

import geojson from "../../assets/Detail_Level_01_Regions_EPSG32629.json"
import geojson2 from "../../assets/Detail_Level_01_Regions_WGS84.json";
import geojson3 from "../../assets/Detail_Level_02_Communes_EPSG32629.json";
import geojson4 from "../../assets/Detail_Level_02_Communes_WGS84.json";
import geojson5 from "../../assets/Detail_Level_03_FarmLeaders_Farms_Fields_WGS84.json";

const MapContent = () => {
    const geoJson = useRef(null);
    const map = useMap();
  
    const highlightFeature = (e) => {
      const layer = e.target;
  
      layer.setStyle({
        color: 'blue',
        dashArray: '',
        fillOpacity: 0.3,
        weight: 5,
      });
    };
  
    const resetHighlight = (e) => {
      geoJson.current?.resetStyle(e.target);
    };
  
    const zoomToFeature = (e) => {
      map.fitBounds(e.target.getBounds());
    };
  
    return (
              <GeoJSON
                data={geojson2}
                key='usa-states'
                ref={geoJson}
                style={() => {
                  return {
                    color: 'blue',
                    // dashArray: '3',
                    fillColor: 'blue',
                    fillOpacity: 0.2,
                    opacity: 1,
                    weight: 2,
                  };
                }}
                onEachFeature={(__, layer) => {
                  layer.on({
                    click: (e) => {
                      zoomToFeature(e);
                    },
                    mouseout: (e) => {
                      resetHighlight(e);
                    },
                    mouseover: (e) => {
                      highlightFeature(e);
                    },
                  });
                }}
              />
    );
  };

  export default MapContent;