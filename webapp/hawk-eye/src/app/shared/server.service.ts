import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class ServerService {

	public url = 'http://172.17.0.2:5200'

	constructor (
    private http: Http
  ) {}

  getSRPL(typeId) {
    return this.http.get(this.url + '/faces/' + typeId)
    .map((res:Response) => res.json());
  }

  getSRPLLocations(id) {
  	return this.http.get(this.url + '/locations/srpl/' + id)
  	.map((res : Response) => res.json());
  }

}
