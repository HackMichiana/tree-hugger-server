(function() {
  'use strict';
  $(document).ready(init);

  var map;
  var trees;

  function init() {
    var mapOptions = {
      center: { lat: 41.6725, lng: -86.2},
      zoom: 13
    };
    map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    // Request current location
    navigator.geolocation.getCurrentPosition(function(pos){
        map.setCenter({lat: pos.coords.latitude, lng: pos.coords.longitude})
        map.setZoom(15)
    });

    // fetch trees
    trees = window.trees = new TreeCollection();
    trees.fetch({data:{limit:1000}});
  }


  var Tree = Backbone.Model.extend({
    initialize: function(options) {},
    createMarker: function() {
      var marker = new google.maps.Marker({position: {lat: this.get('latitude'), lng: this.get('longitude')}, map: map})
      this.set('marker', marker);
    },
    removeMarker: function() {
      this.get('marker').setMap(null);
    }
  })

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
