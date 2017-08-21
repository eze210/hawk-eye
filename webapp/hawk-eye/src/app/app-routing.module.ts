import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { SrplComponent } from './pages/srpl/srpl.component';
import { SrplgetComponent } from './pages/srplget/srplget.component';
import { SreComponent } from './pages/sre/sre.component';
import { SrplsearchComponent } from './pages/srplsearch/srplsearch.component';

const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'upload',
    component: SrplComponent
  },
  {
    path: 'srplget',
    component: SrplgetComponent
  },
  {
    path: 'sre',
    component: SreComponent
  },
  {
    path: 'search',
    component: SrplsearchComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
