import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable()
export class InformationService {
  constructor(private http: HttpClient) {}
  content;

  tips_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/generaltips/';

  register_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/profile_create_api/';

  update_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/profile_update_api/';

  view_profile_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/profile_view_api/';

  login_url: string =
    'http://uraniumkid40.pythonanywhere.com/insuretech_apis/profile_view_api/';

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

  getProfile(data) {
    return this.http.post(this.view_profile_url, data).toPromise();
  }

  // Set Dummy Data for My Policies Component - using the data object
  setAutoData(e) {
    this.content = e;
    console.log('setting data:', e);
  }

  // Recieve/Get Dummy Data In My Policies Component
  getAutoData() {
    if (this.content) {
      console.log('gotten data:');
    }
    return this.content;
  }

  loginUser(content) {
    return this.http.post(this.register_url, content).toPromise();
  }
}
