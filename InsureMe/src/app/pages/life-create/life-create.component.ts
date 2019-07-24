import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'ngx-life-create',
  templateUrl: './life-create.component.html',
  styleUrls: ['./life-create.component.scss']
})
export class LifeCreateComponent implements OnInit {
  plans = [
    '5 year term',
    '10 year term',
    'Universal life',
    'Whole life',
    'I am unsure and need advice'
  ];

  // cancel_options = ['Yes', 'No'];
  // life_options = ['Yes', 'No'];
  options = ['Yes', 'No']

  life_insurance: FormGroup;
  constructor() {}

  ngOnInit() {
    this.life_insurance = new FormGroup({
      life_plan: new FormControl(''),
      cover_amount: new FormControl(''),
      height: new FormControl(''),
      weight: new FormControl(''),
      health_issues: new FormControl(''),
      total_existing: new FormControl(''),
      cancel_existing: new FormControl(''),
      existing_life_insurance: new FormControl(''),
      additional_comments: new FormControl('')
    });
  }

  submit() {
    console.log('[form values]', this.life_insurance.value);
  }
}
