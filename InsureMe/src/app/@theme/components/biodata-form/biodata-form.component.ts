import { InformationService } from './../../../providers/information.service';
import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'ngx-biodata-form',
  templateUrl: './biodata-form.component.html',
  styleUrls: ['./biodata-form.component.scss']
})
export class BiodataFormComponent implements OnInit {
  imageObj: any;
  biodata_form: FormGroup;
  constructor(
    private router: Router,
    private activatedRoute: ActivatedRoute,
    private infoService: InformationService
  ) {}

  ngOnInit() {
    this.biodata_form = new FormGroup({
      username: new FormControl(''),
      firstname: new FormControl(''),
      lastname: new FormControl(''),
      email: new FormControl(''),
      image: new FormControl('')
    });
  }

  handleImg(e) {
    console.log('image:', e);
    const file = e.target.files[0];
    this.imageObj = file.name;
  }

  submit() {
    console.log(
      'form values:',
      this.biodata_form.value,
      'image: ',
      this.imageObj
    );
    const username = this.biodata_form.value.username;
    const firstname = this.biodata_form.value.firstname;
    const lastname = this.biodata_form.value.lastname;
    const email = this.biodata_form.value.email;
    // const image = this.imageObj;
    const image = this.biodata_form.value.image;
    const token = sessionStorage.getItem('token');

    const data = {
      username,
      firstname,
      lastname,
      email,
      image,
      // Add token
      token
    };
    // Do API transaction here
    console.table(data);
    this.infoService
      .updateProfile(data)
      .then(res => res)
      .then(data => {
        console.log(data);
      });
  }
  goBack() {
    this.router.navigate(['/'], { relativeTo: this.activatedRoute });
  }
}
