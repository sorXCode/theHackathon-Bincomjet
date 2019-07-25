import { FormGroup, Validators, FormControl } from '@angular/forms';
import { Router, ActivatedRoute } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {
  login_form: FormGroup;
  constructor(private router: Router, private activatedRoute: ActivatedRoute) {}

  ngOnInit() {
    this.login_form = new FormGroup({
      email: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required)
    });
  }

  login() {
    console.log('[form values]:', this.login_form.value);
  }

  gotoRegister() {
    this.router.navigate(['/register'], { relativeTo: this.activatedRoute });
  }

  goBack() {
    this.router.navigate(['/'], { relativeTo: this.activatedRoute });
  }
}
