import { FormGroup, FormControl } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ngx-health-create',
  templateUrl: './health-create.component.html',
  styleUrls: ['./health-create.component.scss']
})
export class HealthCreateComponent implements OnInit {
  options = ['Yes', 'No'];
  health_insurance: FormGroup;

  constructor() {}

  ngOnInit() {
    this.health_insurance = new FormGroup({
      cover_amount: new FormControl(''),
      height: new FormControl(''),
      weight: new FormControl(''),
      current_cover: new FormControl(''),
      health_history: new FormControl(''),
      additional_comments: new FormControl('')
    });
  }

  submit() {
    console.log('form values:', this.health_insurance.value);
  }
}
