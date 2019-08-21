import { InformationService } from './../../providers/information.service';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ngx-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.scss']
})
export class UserProfileComponent implements OnInit {
  firstname: string;
  lastname: string;
  username: string;
  image: string;
  wallet_balance: string;
  email: string;
  profile;

  loading = false;
  error = false;

  constructor(private infoService: InformationService) {}

  ngOnInit() {
    const token = sessionStorage.getItem('token');
    const data = {
      token
    };
    this.infoService
      .getProfile(data)
      .then(res => res)
      .then(data => {
        this.loading = true;
        // console.log(data);
        if (sessionStorage.getItem('profile') === null) {
          sessionStorage.setItem('profile', JSON.stringify(data));
        } else {
          console.log('Profile saved already, not saving anymore!');
        }
        if (data) {
          if (data && data['firstname']) {
            this.firstname = data['firstname'];
            // console.log('firstname:', this.firstname);
          }
          if (data && data['lastname']) {
            this.lastname = data['lastname'];
          }
          if (data && data['username']) {
            this.username = data['username'];
          }
          if (data && data['image']) {
            this.image = data['image'];
          }
          if (data && data['balance']) {
            this.wallet_balance = data['balance'];
            console.log('purse:', this.wallet_balance)
          }
          if (data && data['email']) {
            this.email = data['email'];
          }
        }
        this.loading = false;
        this.error = false;
      })
      .catch(err => {
        // console.log(err);
        // this.error = true;
        this.loading = true;
        if (sessionStorage.getItem('profile') !== null) {
          this.profile = JSON.parse(sessionStorage.getItem('profile'));
          console.log(this.profile);
          if (this.profile) {
            if (this.profile && this.profile['firstname']) {
              this.firstname = this.profile['firstname'];
            }
            if (this.profile && this.profile['lastname']) {
              this.lastname = this.profile['lastname'];
            }
            if (this.profile && this.profile['username']) {
              this.username = this.profile['username'];
            }
            if (this.profile && this.profile['image']) {
              this.image = this.profile['image'];
            }
            if (this.profile && this.profile['balance']) {
              this.wallet_balance = this.profile['balance'];
            }
            if (this.profile && this.profile['email']) {
              this.email = this.profile['email'];
            }
          }
        }
        this.loading = false;
      });
  }
}
