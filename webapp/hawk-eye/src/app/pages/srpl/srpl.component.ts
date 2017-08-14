import { Component, OnInit } from '@angular/core';
import { Http, Response, RequestOptions, Headers } from '@angular/http';
import 'rxjs/add/operator/map';
import {Observable} from 'rxjs/Observable';
import { RadioControlValueAccessor } from '@angular/forms';
const URL = 'http://172.17.0.2:5200/faces';

@Component({
  selector: 'app-srpl',
  templateUrl: './srpl.component.html',
  styleUrls: ['./srpl.component.scss']
})
export class SrplComponent implements OnInit {
  title = 'Upload Image';
  data
  constructor(private http: Http) {
    this.data = {
      name: '',
      myType: '0'
    };
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
        this.http.post(URL, formData)
            .map(res => res.json())
            .catch(error => Observable.throw(error))
            .subscribe(
                data => console.log('success'),
                error => console.log(error)
            )
    }
  }

  ngOnInit() {
  }

}

export class RadioButtonComp {
  myType = '0';
}