import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import * as data from '../config/config.json';

@Injectable()
export class ServerService {
  
  public url;

	constructor (
    private http: Http
  ) {
    this.url = 'http://' + (<any>data).api_ip + ':' + (<any>data).api_port;
  }

  getSRPL(typeId) {
    return this.http.get(this.url + '/faces/' + typeId)
    .map((res:Response) => res.json());
  }

  getSRPLLocations(id) {
  	return this.http.get(this.url + '/locations/srpl/' + id)
  	.map((res : Response) => res.json());
  }

}
