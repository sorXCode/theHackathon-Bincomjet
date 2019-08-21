import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AutoCreateComponent } from './auto-create/auto-create.component';
import { NgModule } from '@angular/core';
import {
  NbMenuModule,
  NbAccordionModule,
  NbIconModule,
  NbInputModule,
  NbCardModule,
  NbButtonModule,
  NbActionsModule,
  NbUserModule,
  NbCheckboxModule,
  NbSelectModule,
  NbRadioModule,
  NbDatepickerModule,
  NbSpinnerModule,
  NbTreeGridModule
} from '@nebular/theme';
import { NgCircleProgressModule } from 'ng-circle-progress';

import { ThemeModule } from '../@theme/theme.module';
import { PagesComponent } from './pages.component';
import { DashboardModule } from './dashboard/dashboard.module';
import { PagesRoutingModule } from './pages-routing.module';
import { MiscellaneousModule } from './miscellaneous/miscellaneous.module';
import { InsuranceTypesComponent } from './insurance-types/insurance-types.component';
import { CreateNewComponent } from './create-new/create-new.component';
import { HealthCreateComponent } from './health-create/health-create.component';
import { LifeCreateComponent } from './life-create/life-create.component';
import { RenewFormComponent } from './renew-form/renew-form.component';
import { AutoClaimsComponent } from './claims/auto-claims/auto-claims.component';
import { HealthClaimsComponent } from './claims/health-claims/health-claims.component';
import { LifeClaimsComponent } from './claims/life-claims/life-claims.component';
import { MyPoliciesComponent } from './my-policies/my-policies.component';
import { HealthPoliciesComponent } from './health-policies/health-policies.component';
import { LifePoliciesComponent } from './life-policies/life-policies.component';
import { UserProfileComponent } from './user-profile/user-profile.component';
import { BiodataComponent } from './biodata/biodata.component';
import { BankDetailsComponent } from './bank-details/bank-details.component';
import { WorkDetailsComponent } from './work-details/work-details.component';
UserProfileComponent;
@NgModule({
  imports: [
    PagesRoutingModule,
    ThemeModule,
    NbMenuModule,
    DashboardModule,
    NbAccordionModule,
    NbIconModule,
    MiscellaneousModule,
    NbInputModule,
    NbCardModule,
    NbButtonModule,
    NbActionsModule,
    NbUserModule,
    NbCheckboxModule,
    NbRadioModule,
    NbDatepickerModule,
    FormsModule,
    ReactiveFormsModule,
    NbSelectModule,
    NbSpinnerModule,
    NbTreeGridModule,
    NgCircleProgressModule.forRoot({
      backgroundOpacity: 1,
      backgroundStrokeWidth: 30,
      backgroundPadding: 5,
      space: 1,
      maxPercent: 100,
      unitsFontSize: '25',
      outerStrokeWidth: 13,
      innerStrokeWidth: 3,
      titleFontSize: '50',
      showSubtitle: false,
      responsive: false
    })
  ],
  declarations: [
    PagesComponent,
    InsuranceTypesComponent,
    AutoCreateComponent,
    CreateNewComponent,
    HealthCreateComponent,
    LifeCreateComponent,
    RenewFormComponent,
    AutoClaimsComponent,
    HealthClaimsComponent,
    LifeClaimsComponent,
    MyPoliciesComponent,
    HealthPoliciesComponent,
    LifePoliciesComponent,
    UserProfileComponent,
    BiodataComponent,
    BankDetailsComponent,
    WorkDetailsComponent
  ]
})
export class PagesModule {}
