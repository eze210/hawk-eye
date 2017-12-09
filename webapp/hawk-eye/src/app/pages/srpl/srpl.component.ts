import { Component, OnInit } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';
import { RadioControlValueAccessor } from '@angular/forms';
import * as data from '../../config/config.json';

@Component({
  selector: 'app-srpl',
  templateUrl: './srpl.component.html',
  styleUrls: ['./srpl.component.scss']
})
export class SrplComponent implements OnInit {
  public URL;
  title = 'Upload Image';
  data
  constructor(private http: Http) {
    this.data = {
      name: '',
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
        formData.append('name', this.data["name"]);
        formData.append('typeId', this.data["myType"]);
        let headers = new Headers();
        this.http.post(this.URL + '/faces', formData)
            .map(res => res.json())
            .catch(error => Observable.throw(error))
            .subscribe(
                data => alert('success'),
                error => alert(error)
            )
    }
  }

  ngOnInit() {
  }

}

export class RadioButtonComp {
  myType = '0';
}