import React, { useEffect, useState, useRef } from "react";

import { MapContainer, TileLayer, GeoJSON, useMap, getSource } from 'react-leaflet';

import L from 'leaflet';

import geojson from "../../assets/Detail_Level_01_Regions_EPSG32629.json"
import geojson2 from "../../assets/Detail_Level_01_Regions_WGS84.json";
import geojson3 from "../../assets/Detail_Level_02_Communes_EPSG32629.json";
import geojson4 from "../../assets/Detail_Level_02_Communes_WGS84.json";
import geojson5 from "../../assets/Detail_Level_03_FarmLeaders_Farms_Fields_WGS84.json";

const MapContent = props => {
    const geoJsonRegions = useRef(null);
    const geoJsonProvinces = useRef(null);
    const geoJsonFarms = useRef(null)
    const map = useMap();

    const [getRegionsWithCodes, setRegions] = useState([])
    const [zoomedRegion, setZoomedRegion] = useState(null)

    useEffect(()=> {
        L.geoJSON(geojson4.features, {
            onEachFeature: function(feature, layer) {
                setRegions([...getRegionsWithCodes, {
                    region: geojson4,
                    regionCode: feature.properties.Code_Region
                }]);
            }
        })
    },[])

    useEffect(() => {
        let getZoomedRegion = null;
        if(props.zoomState.code && (getRegionsWithCodes.length > 0)) {
            getZoomedRegion = getRegionsWithCodes.find(r => r.regionCode === props.zoomState.code)
        }
        getZoomedRegion && setZoomedRegion(getZoomedRegion.region)
    },[props.zoomState.code])
  
    const highlightFeature = (e, type) => {
      const layer = e.target;
      if (type === 'provinces') {
        layer.setStyle({
            color: '#c7c115',
            dashArray: '',
            fillOpacity: 0.3,
            weight: 5,
          });
      } else {
        layer.setStyle({
            color: '#0c00bf',
            dashArray: '',
            fillOpacity: 0.3,
            weight: 5,
          });
      }
    };
  
    const resetHighlight = (e, type) => {
      if (type === 'provinces') {
        geoJsonProvinces.current?.resetStyle(e.target);
      } else {
        geoJsonRegions.current?.resetStyle(e.target);
      }
    };
  
    const zoomToFeature = (e, type) => {
        map.fitBounds(e.target.getBounds());
        props.setZoomState({
            type: 'provinces',
            code: null,
        })
        setTimeout(()=>{
            if (type === 'regions') {
                props.setZoomState({
                    type: 'provinces',
                    code: e.target.feature.properties.Code_Region,
                })
            }
        }, 300)
    };

    useEffect(()=>{
        if (props.zoomState.code && props.zoomState.type === "regions" ) {
            map.fitBounds(geoJsonRegions.current.getBounds())
        }
    },[props.zoomState.type])
  
    return (
        <>
            {props.zoomState.type === "regions" &&
                <GeoJSON
                    data={geojson2}
                    key='regions'
                    ref={geoJsonRegions}
                    style={() => {
                    return {
                        color: '#0c00bf',
                        // dashArray: '3',
                        fillColor: '#0c00bf',
                        fillOpacity: 0.2,
                        opacity: 1,
                        weight: 2,
                    };
                    }}
                    onEachFeature={(__, layer) => {
                    layer.on({
                        click: (e) => {
                        zoomToFeature(e, 'regions');
                        },
                        mouseout: (e) => {
                        resetHighlight(e, 'regions');
                        },
                        mouseover: (e) => {
                        highlightFeature(e, 'regions');
                        },
                    });
                    }}
                />
            }
              {(zoomedRegion && props.zoomState.type === "provinces") &&
                <>
                    <GeoJSON
                        data={zoomedRegion}
                        key='provinces'
                        ref={geoJsonProvinces}
                        style={() => {
                            return {
                            color: '#c7c115',
                            // dashArray: '3',
                            fillColor: '#c7c115',
                            fillOpacity: 0.2,
                            opacity: 1,
                            weight: 2,
                            };
                        }}
                        onEachFeature={(__, layer) => {
                            layer.on({
                            click: (e) => {
                                zoomToFeature(e, 'regions');
                            },
                            mouseout: (e) => {
                                resetHighlight(e, 'provinces');
                            },
                            mouseover: (e) => {
                                highlightFeature(e, 'provinces');
                            },
                            });
                        }}
                    />
                    <GeoJSON
                        data={geojson5}
                        key='farms'
                        ref={geoJsonFarms}
                        style={() => {
                            return {
                            color: 'red',
                            // dashArray: '3',
                            fillColor: 'red',
                            fillOpacity: 0.2,
                            opacity: 1,
                            weight: 2,
                            };
                        }}
                        // onEachFeature={(__, layer) => {
                        //     layer.on({
                        //     click: (e) => {
                        //         zoomToFeature(e, 'regions');
                        //     },
                        //     mouseout: (e) => {
                        //         resetHighlight(e, 'provinces');
                        //     },
                        //     mouseover: (e) => {
                        //         highlightFeature(e, 'provinces');
                        //     },
                        //     });
                        // }}
                    />
                </>
                
                
              }
        </>
    );
  };

  export default MapContent;