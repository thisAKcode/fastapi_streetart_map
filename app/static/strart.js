center = [59.377226772242814, 13.516237456465513];



function makeMap() {
    var TILE_URL = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
    var MB_ATTR = 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';
    mymap = L.map('mapid').setView(center, 14);
    L.tileLayer(TILE_URL, {attribution: MB_ATTR}).addTo(mymap);
}

var layer = L.layerGroup();


function centerMap(location_id) {
    var lociEndPoint = "/location/" + location_id
    $.getJSON(lociEndPoint, 
    function(obj) {  // function(obj) {} used to get data
        var toCenterPoint = obj.data[0]  // grab first coordinate pair to be used as center
        var markers = obj.data.map(function(arr) { 
            return L.marker([arr[0], arr[1]])
        });
        mymap.setView(toCenterPoint, 14, { animation: true });
        var group = new L.featureGroup(markers);
        mymap.fitBounds(group.getBounds());
    });
};

// TO DO numbered markers add'
// Markers adding numbers
/* https://stackoverflow.com/a/23880244/12163779
   https://stackoverflow.com/a/55268599/12163779 */
function renderData(location_id) {
    var lociEndPoint = "/location/" + location_id;
    $.getJSON(lociEndPoint, 
    function(obj) {  // for each subArray in the data array https://stackoverflow.com/a/47461128
        console.log('here');
        console.log(obj.data);
        var markers = obj.data.map(function(arr) { 
            var _circles = L.circleMarker([arr[0], arr[1]], { 
                radius: 5,
                fillColor: 'blue',
                color: 'blue',
                weight: 0.5,
                opacity: 1,
                fillOpacity: 0.5,
                pane: 'markerPane'  }).bindTooltip(arr[2], {pane: 'tooltipPane', sticky: true, 
                                                            permanent: false, opacity: 0.7}).openTooltip() 
            return _circles 
        });
        mymap.removeLayer(layer);
        layer = L.layerGroup(markers);
        mymap.addLayer(layer);
    });
};

function fixPopup(location_id) {
    var lociEndPoint = "/location/" + location_id
    $.getJSON(lociEndPoint, 
    function(obj) {  // for each subArray in the data array https://stackoverflow.com/a/47461128
        var markers = obj.data.map(function(arr) { 
            var _popups = L.circleMarker([arr[0], arr[1]], { radius: 5,
                fillColor: 'blue',
                color: 'blue',
                weight: 0.5,
                opacity: 0.1,
                fillOpacity: 0.1,
                pane: 'markerPane'  }).bindPopup(arr[2]).openPopup() 
            return _popups 
        });
        layer = L.layerGroup(markers);
        mymap.addLayer(layer);
    });
};


$(function() {
    makeMap();
    renderData('Karlstad center'); // pick up location with such name to render first 
    $('#loc_option').change(function() {
        var val = $('#loc_option option:selected').val();
        
        renderData(val);
        //fixPopup(val);
        centerMap(val);
    });
});