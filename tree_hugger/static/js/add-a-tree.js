$(document).ready(init);

function init() {
  if(!("url" in window) && ("webkitURL" in window)) window.URL = window.webkitURL;

  $('#location_button').click(captureTreeLocation);
  $('#leaf_photo_input').on('change', capturedLeafPhoto);
  $('#tree_photo_input').on('change', capturedTreePhoto);
}

function captureTreeLocation() {
  if(!Modernizr.geolocation) alert('This browser does not support geolocation. Please try another browser.');
  console.log('getting location')
  navigator.geolocation.getCurrentPosition(
    function(position) {
      console.log(position);
      $('#location_latitude').text(position.coords.latitude);
      $('#location_longitude').text(position.coords.longitude);
      $('#location_accuracy').text(position.coords.accuracy);
    },
    function(err) {
      console.log(err);
    }
  )
}

function capturedLeafPhoto(evt) {
  if(event.target.files.length == 1 && event.target.files[0].type.indexOf("image/") == 0) {
    $("#leaf_photo_preview").attr("src",URL.createObjectURL(event.target.files[0]));
  }
}

function capturedTreePhoto(evt) {
  if(event.target.files.length == 1 && event.target.files[0].type.indexOf("image/") == 0) {
    $("#tree_photo_preview").attr("src",URL.createObjectURL(event.target.files[0]));
  }
}
