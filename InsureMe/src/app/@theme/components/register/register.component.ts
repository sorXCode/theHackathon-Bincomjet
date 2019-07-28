import { InformationService } from './../../../providers/information.service';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';
import { NbToastrService } from '@nebular/theme';

@Component({
  selector: 'ngx-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  reg_form: FormGroup;
  loggedIn = false;
  constructor(
    private router: Router,
    private activatedRoute: ActivatedRoute,
    private toastrService: NbToastrService,
    private infoService: InformationService
  ) {}

  ngOnInit() {
    this.reg_form = new FormGroup({
      email: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required)
      // r_password: new FormControl('', Validators.required)
    });
  }

  register() {
    const password = this.reg_form.value.password;
    // const repeated = this.reg_form.value.r_password;
    // if (password !== repeated) {
    //   // this.showToast('top-right', 'Passwords do not match!');
    //   alert('Passwords do not match!');
    // }
    const data = {
      email: this.reg_form.value.email,
      password: this.reg_form.value.password
    };
    console.log('[form values]:', this.reg_form.value);
    this.infoService
      .registerUser(data)
      .then(res => res)
      .then(data => {
        console.log(data);
        const token = data['token'];
        sessionStorage.setItem('token', token);
        this.loggedIn = true;
        this.router.navigate(['/'], { relativeTo: this.activatedRoute });
        console.log('Navigated to Home!');
      })
      .catch(err => {
        console.log(err);
        this.loggedIn = false;
        alert('Error signing up!');
      });
  }
  gotoLogin() {
    this.router.navigate(['/login'], { relativeTo: this.activatedRoute });
  }
  goBack() {
    this.router.navigate(['/'], { relativeTo: this.activatedRoute });
  }

  // showToast(position, message) {
  //   this.toastrService.show(message || 'User successfully registered', {
  //     position,
  //     message
  //   });
  // }
}
