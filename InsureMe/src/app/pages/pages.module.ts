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
import { CreateNewComponent } from './create-new/create-new.component';
import { HealthCreateComponent } from './health-create/health-create.component';
import { LifeCreateComponent } from './life-create/life-create.component';
import { RenewFormComponent } from './renew-form/renew-form.component';

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
    CreateNewComponent,
    HealthCreateComponent,
    LifeCreateComponent,
    RenewFormComponent
  ]
})
export class PagesModule {}
