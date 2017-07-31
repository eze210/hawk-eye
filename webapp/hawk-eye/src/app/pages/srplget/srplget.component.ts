import { Component, OnInit } from '@angular/core';
import { ServerService } from '../../shared/server.service'

@Component({
  selector: 'app-srplget',
  templateUrl: './srplget.component.html',
  styleUrls: ['./srplget.component.scss']
})
export class SrplgetComponent implements OnInit {

  constructor(private ServerService : ServerService) { }
  photos = [];
  faces = {};

  loadSRPL() {
    this.ServerService.getSRPL().subscribe(data => this.faces = data);
  }

  ngOnInit() {
  	this.ServerService.getSRPL()
		.subscribe(photos => {
		    this.photos = photos["data"];
		    for (let photo of this.photos) {
		        photo.imageData = 'data:image/png;base64,' + photo[1];
		    };
		});
  }

}
