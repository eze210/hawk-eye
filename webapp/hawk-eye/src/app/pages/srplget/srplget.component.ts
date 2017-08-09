import { Component, OnInit } from '@angular/core';
import { ServerService } from '../../shared/server.service'

declare var google: any;

@Component({
  selector: 'app-srplget',
  templateUrl: './srplget.component.html',
  styleUrls: ['./srplget.component.scss']
})
export class SrplgetComponent implements OnInit {

  constructor(private ServerService : ServerService) { }
  photos = [];
  faces = {};
  coordinates = [];

  ngOnInit() {
  	this.ServerService.getSRPL()
		.subscribe(photos => {
		    this.photos = photos["data"];
		    for (let photo of this.photos) {
		        photo.imageData = 'data:image/png;base64,' + photo[1];
		    };
		});

    // Maps
    var directionsService = new google.maps.DirectionsService;
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7,
        center: {lat: 41.85, lng: -87.65}
      });
    directionsDisplay.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsDisplay);

    function calculateAndDisplayRoute(directionsService, directionsDisplay) {

      var waypts = [];
      var checkboxArray:any[] = [
          'winnipeg', 'regina','calgary'
      ];
      for (var i = 0; i < checkboxArray.length; i++) {
        waypts.push({
          location: checkboxArray[i],
          stopover: true
        });

      }

      directionsService.route({
        origin: {lat: 41.85, lng: -87.65},
        destination: {lat: 49.3, lng: -123.12},
        waypoints: waypts,
        optimizeWaypoints: true,
        travelMode: 'DRIVING'
      }, function(response, status) {
        if (status === 'OK') {
          directionsDisplay.setDirections(response);
        } else {
          window.alert('Directions request failed due to ' + status);
        }
      });
    }
  }

  getLocations(id) {
    this.ServerService.getSRPLLocations(id)
    .subscribe(locations => {
        this.coordinates = locations["data"]
    });
  }

}
