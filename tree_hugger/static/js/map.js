(function() {
  'use strict';
  $(document).ready(init);

  var map;
  var trees;
  var KNOWN_HASHES = {
    '#add-tree': '#modal_add_tree'
  }

  function init() {
    var mapOptions = {
      center: { lat: 41.6725, lng: -86.2},
      zoom: 13,
      // mapTypeControl: true,
      // mapTypeControlOptions: {
      //   style: google.maps.MapTypeControlStyle.DEFAULT,
      //   mapTypeIds: [
      //     google.maps.MapTypeId.ROADMAP,
      //     google.maps.MapTypeId.TERRAIN
      //   ]
      // },
      streetViewControl: false,
      panControl: false,
      zoomControl: true,
      zoomControlOptions: {
        style: google.maps.ZoomControlStyle.SMALL,
        position: google.maps.ControlPosition.RIGHT_BOTTOM
      }
    };
    map = new google.maps.Map(document.getElementById('map_canvas'), mapOptions);

    // Request current location
    navigator.geolocation.getCurrentPosition(function(pos){
        map.setCenter({lat: pos.coords.latitude, lng: pos.coords.longitude})
        map.setZoom(15)
    });

    // If not auth, bail & show login
    if(!USERNAME) {
      $('#modal_login_signup').modal('show');
      return;
    }


    // fetch trees
    trees = window.trees = new TreeCollection();
    trees.fetch({data:{limit:1000}});

    // if known hash, show modal
    if(_.has(KNOWN_HASHES, window.location.hash)) {
      setTimeout(function() { $(KNOWN_HASHES[window.location.hash]).modal('show'); }, 750);
    }
  }

  var Tree = Backbone.Model.extend({
    initialize: function(options) {},
    addInfoWindow: function(marker) {
      google.maps.event.addListener(marker, 'click', function(e) {
        var infowindow = new google.maps.InfoWindow();
        infowindow.open(marker.map, marker)
        var infoDiv = document.createElement('div')
        infoDiv.innerHTML = "<h4>An Tree.</h4>"
          + "Condition: " + marker.data.attributes.condition + "<br />"
          + "Height class: " + marker.data.attributes.height + "<br />"
          + "Diameter: " + marker.data.attributes.diameter + "<br />"
        infowindow.setContent(infoDiv)
        marker.data.attributes.images.forEach(function(anImage){
          var img = document.createElement('img')
          img.src = anImage.image
          img.style.maxWidth = '128px'
          img.style.maxHeight = '128px'
          img.style.padding = '10px'
          infoDiv.appendChild(img)
        })
      })
    },
    createMarker: function() {
      var marker = new google.maps.Marker({position: {lat: this.get('latitude'), lng: this.get('longitude')}, map: map})
      marker.data = this;
      this.addInfoWindow(marker);
      this.set('marker', marker);
    },
    removeMarker: function() {
      this.get('marker').setMap(null);
    }
  });

  var TreeCollection = Backbone.Collection.extend({
    url: '/api/v1/tree/',
    model: Tree,
    initialize: function(options) {
      this.on('add', this._onAdd.bind(this));
      this.on('remove', this._onRemove.bind(this));
    },
    _onAdd: function(model) { model.createMarker(); },
    _onRemove: function(model) { model.removeMarker(); },
  });
}());
