import { Component, OnInit, ViewChild } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';

@Component({
  selector: 'insurance-types',
  templateUrl: './insurance-types.component.html',
  styleUrls: ['./insurance-types.component.scss']
})
export class InsuranceTypesComponent implements OnInit {
  constructor(private router: Router, private activatedRoute: ActivatedRoute) {}
  @ViewChild('item', { static: true }) accordion;
  ngOnInit() {}

  toggle() {
    this.accordion.toggle();
  }

  gotoAuto() {
    this.router.navigate(['/pages/auto-create'], {
      relativeTo: this.activatedRoute
    });
  }
}