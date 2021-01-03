import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {DashboardComponent} from './dashboard/dashboard.component';
import {LoginComponent} from './login/login.component';
import {AuthGuard} from './auth.guard';
import {AboutComponent} from './about/about.component';
import {ListOfUsersComponent} from './list-of-users/list-of-users.component';
import {LoginCallbackComponent} from './login-callback/login-callback.component';


const routes: Routes = [

  {path: '', redirectTo: 'login', pathMatch: 'full'},
  {path: 'login', component: LoginComponent},
  {path: 'about.json', component: AboutComponent},
  {path: 'dashboard', canActivate: [AuthGuard], component: DashboardComponent},
  {path: 'listofusers', component: ListOfUsersComponent},
  {path: 'login/callback', component: LoginCallbackComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes, { relativeLinkResolution: 'legacy' })],
  exports: [RouterModule]
})
export class AppRoutingModule { }
