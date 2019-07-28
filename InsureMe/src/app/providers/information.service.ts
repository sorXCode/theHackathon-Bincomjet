import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class InformationService {
  constructor(private http: HttpClient) {}

  tips_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/generaltips/';

  register_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/profile_create_api/';

  update_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/profile_update_api/';

  fetchTips() {
    return this.http
      .get(this.tips_url)
      .toPromise()
      .then(res => res);
  }

  registerUser(data) {
    return this.http.post(this.register_url, data).toPromise();
  }

  updateProfile(data) {
    return this.http.post(this.update_url, data).toPromise();
  }
}
