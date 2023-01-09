var CENTER = [59.09827437369457, 13.115860356662202];

function makeMap() {
    var TILE_URL = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    var MB_ATTR = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    mymap = L.map('mapid').setView(CENTER, 5);
    L.tileLayer(TILE_URL, {attribution: MB_ATTR}).addTo(mymap);
}


var layer = L.layerGroup();
//var myLayer = L.geoJSON();
//myLayer.addData(geojsonFeature);

function centerMap() {
    mymap.setView(CENTER, 1.5, { animation: true });
    };

//image_two    
function style_popup(feature, layer) {
        // does this feature have a property named popupContent?
        if (feature.properties && feature.properties.image_two) {
            let _image_in =  "<img src='"+ feature.properties.image_two+"'/>"
            layer.bindPopup(_image_in);
        }
    }

function relevantPopup(feature_in){
    return "<img src='"+ feature_in.properties.image_two+"'/>" 
}

function pointAdder(_features) {
    let _pointLayer = L.geoJSON(_features, {
        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng, geojsonMarkerOptions).bindPopup(relevantPopup(feature), {
                maxWidth: "auto"
              });
        }
    })
    return _pointLayer
}

var geojsonMarkerOptions = {
    radius: 5,
        fillColor: 'blue',
        color: 'blue',
        weight: 0.5,
        opacity: 0.1,
        fillOpacity: 0.3,
};    

function _render_pts(_features){
    let _ptsFeatures = pointAdder(_features)
        console.log(typeof(_ptsFeatures))
        _ptsFeatures.addTo(mymap);
};

function _render_items() {
    var artEndpoint = "/map2/";
    $.getJSON(artEndpoint, 
    function(obj) {  // for each subArray in the data array https://stackoverflow.com/a/47461128
        var _features = obj.data.map(function(_item_1b1) {
           return _item_1b1
        });
        let geomTypes = _features.map(function (marker) {
            return marker.geometry.type;
          });        
        if (geomTypes[0] == 'Point') {
            _render_pts(_features) 
        } else {
            console.log('I only can process points by now') // code is executed
        }
    });
};

function onEachFeature(feature, layer) {
    // does this feature have a property named popupContent?
    if (feature.properties && feature.properties.popupContent) {
        layer.bindPopup('test');
    }
}

$(function() {
    makeMap();
    _render_items();
    centerMap();
});