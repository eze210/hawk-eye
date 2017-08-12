import { BrowserModule, Title } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './pages/home/home.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { UtilsService } from './core/utils.service';
import { SrplComponent } from './pages/srpl/srpl.component';
import { FormsModule } from '@angular/forms';
import { FileSelectDirective } from 'ng2-file-upload';
import { SrplgetComponent } from './pages/srplget/srplget.component';
import { ServerService} from './shared/server.service'
import { HttpModule } from '@angular/http';
import { SrplsearchComponent } from './pages/srplsearch/srplsearch.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    HeaderComponent,
    FooterComponent,
    SrplComponent,
    FileSelectDirective,
    SrplgetComponent,
    SrplsearchComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpModule,
  ],
  providers: [
   Title,
   UtilsService,
   ServerService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
