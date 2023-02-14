// Note: This example requires that you consent to location sharing when
// prompted by your browser. If you see the error "The Geolocation service
// failed.", it means you probably did not give permission for the browser to
// locate you.
let map, infoWindow;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 6,
  });
  infoWindow = new google.maps.InfoWindow();

  const locationButton = document.createElement("button");

  locationButton.textContent = "Pan to Current Location";
  locationButton.classList.add("custom-map-control-button");
  map.controls[google.maps.ControlPosition.TOP_CENTER].push(locationButton);
  locationButton.addEventListener("click", () => {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          const pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude,
          };

          infoWindow.setPosition(pos);
          infoWindow.setContent("Location found.");
          infoWindow.open(map);
          map.setCenter(pos);
        },
        () => {
          handleLocationError(true, infoWindow, map.getCenter());
        }
      );
    } else {
      // Browser doesn't support Geolocation
      handleLocationError(false, infoWindow, map.getCenter());
    }
  });
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
  infoWindow.setPosition(pos);
  infoWindow.setContent(
    browserHasGeolocation
      ? "Error: The Geolocation service failed."
      : "Error: Your browser doesn't support geolocation."
  );
  infoWindow.open(map);
}

window.initMap = initMap;

/*
*for searching
*/

 /** Initializes Search Input for the widget. */
 function initializeSearchInput() {
  const searchInputEl = widgetEl.querySelector('.input-box');
  widget.placeIdsToAutocompleteResults = new Map();

  // Set up Autocomplete on the search input.
  const autocomplete = new google.maps.places.Autocomplete(searchInputEl, {
    types: ['establishment'],
    fields: [
      'place_id', 'name', 'types', 'geometry.location', 'formatted_address', 'photo', 'url',
      'website', 'formatted_phone_number', 'opening_hours',
      'rating', 'user_ratings_total', 'price_level', 'review',
    ],
    bounds: widget.mapBounds,
    strictBounds: true,
  });
  
  autocomplete.addListener('place_changed', () => {
    const place = autocomplete.getPlace();
    widget.placeIdsToAutocompleteResults.set(place.place_id, place);
    widget.selectPlaceById(place.place_id, /* panToMarker= */ true);
    searchInputEl.value = '';
  });
}
