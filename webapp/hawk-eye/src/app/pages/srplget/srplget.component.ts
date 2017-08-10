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
  ngOnInit() {
  	this.ServerService.getSRPL()
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

  getLocations(id) {
    this.ServerService.getSRPLLocations(id)
    .subscribe(locations => {
        this.coordinates = locations["data"];
        var marker;
        var infowindow = new google.maps.InfoWindow();
        for(var i = 0; i < this.coordinates.length; i++) {
          marker = new google.maps.Marker({
            position: new google.maps.LatLng(this.coordinates[i][0], this.coordinates[i][1]),
            map: this.map
          });

          google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
              infowindow.setContent("1");
              infowindow.open(this.map, marker);
            }
          })(marker, i));
        }
    });
  }

}
