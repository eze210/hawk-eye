import { Component, OnInit } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';
import { RadioControlValueAccessor } from '@angular/forms';
import * as data from '../../config/config.json';

@Component({
  selector: 'app-srplsearch',
  templateUrl: './srplsearch.component.html',
  styleUrls: ['./srplsearch.component.scss']
})
export class SrplsearchComponent implements OnInit {
	public URL;
  title = 'Search by Image';
  data
  photos = [];
  constructor(private http: Http) {
    this.data = {
      myType: '0'
    };
    this.URL = 'http://' + (<any>data).api_ip + ':' + (<any>data).api_port;
  }


 fileChange(event) {
    let fileList: FileList = event.target.files;
    if(fileList.length > 0) {
        let file: File = fileList[0];
        let formData:FormData = new FormData();
        formData.append('uploadFile', file, file.name);
        formData.append('typeId', this.data["myType"]);
        let headers = new Headers();
        this.http.post(this.URL + '/search', formData)
            .map(res => res.json())
            .catch(error => Observable.throw(error))
            .subscribe(photos => {
              	this.photos = photos["matches"];
						    for (let photo of this.photos) {
						        photo.imagedata = 'data:image/png;base64,' + photo[1];
						    };
            });
    }
  }

  ngOnInit() {

  }

}
