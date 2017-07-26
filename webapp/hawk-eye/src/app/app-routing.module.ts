import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { SrplComponent } from './pages/srpl/srpl.component';


const routes: Routes = [
  {
    path: '',
    component: HomeComponent
  },
  {
    path: 'srpl',
    component: SrplComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
