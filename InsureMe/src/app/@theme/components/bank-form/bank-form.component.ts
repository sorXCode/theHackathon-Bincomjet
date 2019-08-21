import { ActivatedRoute, Router } from '@angular/router';
import { FormGroup, FormControl } from '@angular/forms';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'ngx-bank-form',
  templateUrl: './bank-form.component.html',
  styleUrls: ['./bank-form.component.scss']
})
export class BankFormComponent implements OnInit {
  banks = [
    'Access Bank Plc',
    'Fidelity Bank Plc',
    'First City Monument Bank Plc',
    'First Bank of Nigeria Limited'
  ];

  bank_form: FormGroup;
  constructor(private router: Router, private activatedRoute: ActivatedRoute) {}

  ngOnInit() {
    this.bank_form = new FormGroup({
      bank_name: new FormControl(''),
      account_name: new FormControl(''),
      account_number: new FormControl(''),
      bvn: new FormControl(''),
      phone_number: new FormControl('')
    });
  }

  submit() {
    console.log('form values:', this.bank_form.value);
  }
  goBack() {
    this.router.navigate(['/'], { relativeTo: this.activatedRoute });
  }
}
