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
  NbDatepickerModule
} from '@nebular/theme';

import { ThemeModule } from '../@theme/theme.module';
import { PagesComponent } from './pages.component';
import { DashboardModule } from './dashboard/dashboard.module';
import { PagesRoutingModule } from './pages-routing.module';
import { MiscellaneousModule } from './miscellaneous/miscellaneous.module';
import { InsuranceTypesComponent } from './insurance-types/insurance-types.component';
import { BankFormComponent } from './bank-form/bank-form.component';
import { BiodataFormComponent } from './biodata-form/biodata-form.component';
import { CreateNewComponent } from './create-new/create-new.component';
import { HealthCreateComponent } from './health-create/health-create.component';
import { LifeCreateComponent } from './life-create/life-create.component';
import { RenewFormComponent } from './renew-form/renew-form.component';
import { WorkFormComponent } from './work-form/work-form.component';

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
    NbSelectModule
  ],
  declarations: [
    PagesComponent,
    InsuranceTypesComponent,
    AutoCreateComponent,
    BankFormComponent,
    BiodataFormComponent,
    CreateNewComponent,
    HealthCreateComponent,
    LifeCreateComponent,
    RenewFormComponent,
    WorkFormComponent
  ]
})
export class PagesModule {}
