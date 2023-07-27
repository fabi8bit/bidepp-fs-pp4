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
    // var labels = hotel_list;
    

    // var locations = [
    //     { lat: 40.785091, lng: -73.968285 },
    //     { lat: 41.084045, lng: -73.874245 },
    //     { lat: 40.754932, lng: -73.984016 }
    // ];
    
    // var locations = [
    //     { lat: hotelLat, lng: hotelLng },
        
    // ];

    var locations = locations_list

    var markers = locations.map(function(location, i) {
        return new google.maps.Marker({
            position: location,
            label: labels[i % labels.length],
            
        });
    });

    

    var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });

    marker.addEventListener('mouseover', function() {
        infowindow.open(map, marker);
        infowindow.setContent("<div>dio can</div>")
        console.log("Hello world!");
    })
    
}