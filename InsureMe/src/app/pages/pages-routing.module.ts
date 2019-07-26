import { UserProfileComponent } from './user-profile/user-profile.component';
import { LifePoliciesComponent } from './life-policies/life-policies.component';
import { MyPoliciesComponent } from './my-policies/my-policies.component';
import { LifeClaimsComponent } from './claims/life-claims/life-claims.component';
import { HealthClaimsComponent } from './claims/health-claims/health-claims.component';
import { AutoClaimsComponent } from './claims/auto-claims/auto-claims.component';
import { LifeCreateComponent } from './life-create/life-create.component';
import { HealthCreateComponent } from './health-create/health-create.component';
import { AutoCreateComponent } from './auto-create/auto-create.component';
import { RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';

import { PagesComponent } from './pages.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { NotFoundComponent } from './miscellaneous/not-found/not-found.component';
import { InsuranceTypesComponent } from './insurance-types/insurance-types.component';
import { HealthPoliciesComponent } from './health-policies/health-policies.component';

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
        path: 'claims/auto-claims',
        component: AutoClaimsComponent
      },
      {
        path: 'claims/health-claims',
        component: HealthClaimsComponent
      },
      {
        path: 'claims/life-claims',
        component: LifeClaimsComponent
      },
      {
        path: 'my-policies',
        component: MyPoliciesComponent
      },
      {
        path: 'health-policies',
        component: HealthPoliciesComponent
      },
      {
        path: 'life-policies',
        component: LifePoliciesComponent
      },
      {
        path: 'user-profile',
        component: UserProfileComponent
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
