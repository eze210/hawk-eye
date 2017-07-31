import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { SrplComponent } from './pages/srpl/srpl.component';
import { SrplgetComponent } from './pages/srplget/srplget.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'srpl',
    component: SrplComponent
  },
  {
    path: 'srplget',
    component: SrplgetComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
