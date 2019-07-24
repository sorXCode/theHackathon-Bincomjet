import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'auto-create',
  templateUrl: './auto-create.component.html',
  styleUrls: ['./auto-create.component.scss']
})
export class AutoCreateComponent implements OnInit {
  auto_insurance: FormGroup;
  types = ['Van', 'Lorry', 'Jeep', 'Car', 'Cycle'];
  purposes = ['Commercial', 'Private'];
  loading_types = ['General cartage', 'Passengers only', 'Goods only'];
  constructor() {}

  ngOnInit() {
    this.auto_insurance = new FormGroup({
      model: new FormControl(''),
      reg_no: new FormControl(''),
      fuel_capacity: new FormControl(''),
      engine_num: new FormControl(''),
      vehicle_type: new FormControl(''),
      cost_price: new FormControl(''),
      date_of_purchase: new FormControl(''),
      avg_maintenance: new FormControl(''),
      vehicle_faults: new FormControl(''),
      chassis_num: new FormControl(''),
      mileage: new FormControl(''),
      purpose: new FormControl(''),
      loading_type: new FormControl('')
    });
  }

  submit() {
    console.log('form values:', this.auto_insurance.value);
  }
}
