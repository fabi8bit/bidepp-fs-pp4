function initMap() {
    var map = new google.maps.Map(document.getElementById("map"), {
        zoom: zoom_factor,
        center: {
            lat: hotelLat,
            lng: hotelLng
        },
        mapId: '219bf99537910ddc'
    });

    let infowindow = new google.maps.InfoWindow();

    var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    var locations = locations_list;

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length],
            
        });
    });

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });

    
    
}