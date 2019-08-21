import { ExtraOptions, RouterModule, Routes } from '@angular/router';
import { NgModule } from '@angular/core';
import { LoginComponent } from './@theme/components/login/login.component';
import { RegisterComponent } from './@theme/components/register/register.component';
import { BankFormComponent } from './@theme/components/bank-form/bank-form.component';
import { BiodataFormComponent } from './@theme/components/biodata-form/biodata-form.component';
import { WorkFormComponent } from './@theme/components/work-form/work-form.component';

const routes: Routes = [
  {
    path: 'pages',
    loadChildren: () =>
      import('app/pages/pages.module').then(m => m.PagesModule)
  },
  {
    path: 'login',
    component: LoginComponent
  },
  {
    path: 'register',
    component: RegisterComponent
  },
  { path: 'bank-form', component: BankFormComponent },
  {
    path: 'biodata-form',
    component: BiodataFormComponent
  },
  {
    path: 'work-form',
    component: WorkFormComponent
  },

  { path: '', redirectTo: 'pages', pathMatch: 'full' },
  { path: '**', redirectTo: 'pages' }
];

const config: ExtraOptions = {
  useHash: false
};

@NgModule({
  imports: [RouterModule.forRoot(routes, config)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
