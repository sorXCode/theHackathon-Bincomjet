import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ngx-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  reg_form: FormGroup;
  constructor(private router: Router, private activatedRoute: ActivatedRoute) {}

  ngOnInit() {
    this.reg_form = new FormGroup({
      email: new FormControl('', Validators.required),
      password: new FormControl('', Validators.required),
      r_password: new FormControl('', Validators.required)
    });
  }

  register() {
    const password = this.reg_form.value.password;
    const repeated = this.reg_form.value.r_password;
    if (password !== repeated) {
      console.error('Passwords do not match!');
    }
    console.log('[form values]:', this.reg_form.value);
  }
  gotoLogin() {
    this.router.navigate(['/login'], { relativeTo: this.activatedRoute });
  }
  goBack() {
    this.router.navigate(['/'], { relativeTo: this.activatedRoute });
  }
}
