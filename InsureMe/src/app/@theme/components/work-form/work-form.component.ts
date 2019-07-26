import { FormGroup, FormControl } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'ngx-work-form',
  templateUrl: './work-form.component.html',
  styleUrls: ['./work-form.component.scss']
})
export class WorkFormComponent implements OnInit {
  work_form: FormGroup;

  constructor(private router: Router, private activatedRoute: ActivatedRoute) {}

  ngOnInit() {
    this.work_form = new FormGroup({
      company_name: new FormControl(''),
      role: new FormControl('')
    })
  }
  goBack() {
    this.router.navigate(['/'], { relativeTo: this.activatedRoute });
  }
  submit() {
    console.log('form values:', this.work_form.value)
  }
}
