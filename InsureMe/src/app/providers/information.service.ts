import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class InformationService {
  constructor(private http: HttpClient) {}

  tips_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/generaltips/';

  fetchTips() {
    return this.http
      .get(this.tips_url)
      .toPromise()
      .then(res => res);
  }
}
