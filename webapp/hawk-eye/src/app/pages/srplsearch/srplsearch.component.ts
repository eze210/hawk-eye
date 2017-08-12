import { Component, OnInit } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';
const URL = 'http://172.17.0.2:5200/search/srpl';

@Component({
  selector: 'app-srplsearch',
  templateUrl: './srplsearch.component.html',
  styleUrls: ['./srplsearch.component.scss']
})
export class SrplsearchComponent implements OnInit {
	
  title = 'Search in SRPL';
  data
  photos = [];
  constructor(private http: Http) {
    //this.data = {
    //  name: ''
    //};
  }


 fileChange(event) {
    let fileList: FileList = event.target.files;
    if(fileList.length > 0) {
        let file: File = fileList[0];
        let formData:FormData = new FormData();
        formData.append('uploadFile', file, file.name);
        let headers = new Headers();
        this.http.post(URL, formData)
            .map(res => res.json())
            .catch(error => Observable.throw(error))
            .subscribe(photos => {
              	this.photos = photos["matches"];
						    for (let photo of this.photos) {
						        photo = 'data:image/png;base64,' + photo;
						    };
            });
    }
  }

  ngOnInit() {

  }

}
