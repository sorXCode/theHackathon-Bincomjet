import { Component, OnInit, ViewChild } from '@angular/core';

@Component({
  selector: 'insurance-types',
  templateUrl: './insurance-types.component.html',
  styleUrls: ['./insurance-types.component.scss']
})
export class InsuranceTypesComponent implements OnInit {
  constructor() {}
  @ViewChild('item', { static: true }) accordion;
  ngOnInit() {}

  toggle() {
    this.accordion.toggle();
  }
}
