import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'ngx-biodata-form',
  templateUrl: './biodata-form.component.html',
  styleUrls: ['./biodata-form.component.scss']
})
export class BiodataFormComponent implements OnInit {
  constructor(private router: Router, private activatedRoute: ActivatedRoute) {}
  biodata_form: FormGroup;

  ngOnInit() {
    this.biodata_form = new FormGroup({
      username: new FormControl(''),
      firstname: new FormControl(''),
      lastname: new FormControl(''),
      email: new FormControl(''),
      image: new FormControl('')
    });
  }

  submit() {}
  goBack() {
    this.router.navigate(['/'], { relativeTo: this.activatedRoute });
  }
}
