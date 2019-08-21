import { Router, ActivatedRoute } from '@angular/router';
import { FormGroup, FormControl } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { InformationService } from '../../providers/information.service';

@Component({
  selector: 'ngx-health-create',
  templateUrl: './health-create.component.html',
  styleUrls: ['./health-create.component.scss']
})
export class HealthCreateComponent implements OnInit {
  options = ['Yes', 'No'];
  health_insurance: FormGroup;

  constructor(
    private infoService: InformationService,
    private router: Router,
    private activeRoute: ActivatedRoute
  ) {}

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
    const data = this.health_insurance.value;
    this.infoService.setAutoData(data);
    this.router.navigate(['/pages/my-policies'], {
      relativeTo: this.activeRoute
    });
  }
}
