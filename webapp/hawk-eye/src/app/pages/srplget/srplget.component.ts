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
  map;
  marker = [];
  ngOnInit() {
  	this.ServerService.getSRPL(0)
		.subscribe(photos => {
		    this.photos = photos["data"];
		    for (let photo of this.photos) {
		        photo.imageData = 'data:image/png;base64,' + photo[1];
		    };
		});

    // Maps
    this.map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7,
        center: {lat: -34.7739036, lng: -58.320372}
      });
  }

  getLocations(id, name) {
    //Loop through all the markers and remove
    for (var i = 0; i < this.marker.length; i++) {
        this.marker[i].setMap(null);
    }
    this.map = new google.maps.Map(document.getElementById('map'), {
      zoom: 7,
      center: {lat: -34.7739036, lng: -58.320372}
    });
    this.marker = [];
    this.ServerService.getSRPLLocations(id)
    .subscribe(locations => {
        this.coordinates = locations["data"];
        var infowindow = new google.maps.InfoWindow();
        for(var i = 0; i < this.coordinates.length; i++) {
          var date = this.coordinates[i][2];
          this.marker = new google.maps.Marker({
            position: new google.maps.LatLng(this.coordinates[i][0], this.coordinates[i][1]),
            map: this.map
          });

          google.maps.event.addListener(this.marker, 'click', (function(marker, i) {
            return function() {
              infowindow.setContent(name + " - " + date);
              infowindow.open(this.map, marker);
            }
          })(this.marker, i));
        }
    });
  }

}
