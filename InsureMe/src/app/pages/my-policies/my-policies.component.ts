import { InformationService } from './../../providers/information.service';
import { Component, OnInit } from '@angular/core';
import { NbSortDirection, NbSortRequest, NbTreeGridDataSource, NbTreeGridDataSourceBuilder } from '@nebular/theme';


@Component({
  selector: 'ngx-my-policies',
  templateUrl: './my-policies.component.html',
  styleUrls: ['./my-policies.component.scss']
})
export class MyPoliciesComponent implements OnInit {
  comments;
  cover;
  currentCover;
  history;
  height;
  weight;
  constructor(private infoService: InformationService) {}

  ngOnInit() {
    const autoData = this.infoService.getAutoData();
    if (autoData) {
      console.log(autoData);
      this.comments = autoData['additional_comments'];
      this.cover = autoData['cover_amount'];
      this.currentCover = autoData['current_cover'];
      this.history = autoData['health_history'];
      this.height = autoData['height'];
      this.weight = autoData['weight'];
    }
  }
}
