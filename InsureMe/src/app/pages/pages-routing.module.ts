import { LifeCreateComponent } from './life-create/life-create.component';
import { HealthCreateComponent } from './health-create/health-create.component';
import { AutoCreateComponent } from './auto-create/auto-create.component';
import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { NotFoundComponent } from './miscellaneous/not-found/not-found.component';
import { InsuranceTypesComponent } from './insurance-types/insurance-types.component';

const routes: Routes = [
  {
    path: '',
    component: PagesComponent,
    children: [
      {
        path: 'iot-dashboard',
        component: DashboardComponent
      },
      {
        path: 'insurance-types',
        component: InsuranceTypesComponent
      },
      {
        path: 'auto-create',
        component: AutoCreateComponent
      },
      {
        path: 'health-create',
        component: HealthCreateComponent
      },
      {
        path: 'life-create',
        component: LifeCreateComponent
      },
      {
        path: '',
        redirectTo: 'iot-dashboard',
        pathMatch: 'full'
      },
      {
        path: '**',
        component: NotFoundComponent
      }
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PagesRoutingModule {}
