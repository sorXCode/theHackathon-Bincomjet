import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'ngx-auto-claims',
  templateUrl: './auto-claims.component.html',
  styleUrls: ['./auto-claims.component.scss']
})
export class AutoClaimsComponent implements OnInit {
  types = [
    'Own Damage',
    'Collision',
    'Theft',
    'Windscreen Damage'
  ];
  auto_claims: FormGroup;

  choices = ['Yes', 'No'];
  constructor() {}

  ngOnInit() {
    this.auto_claims = new FormGroup({
      damage_type: new FormControl(''),
      person_injured: new FormControl(''),
      image_url: new FormControl(''),
      damage_description: new FormControl('')
    })
  }

  submit() {
    console.log('Form values:', this.auto_claims.value)
  }
}
