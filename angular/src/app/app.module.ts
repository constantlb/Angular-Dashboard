import {BrowserModule} from '@angular/platform-browser';
import {NgModule} from '@angular/core';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {DashboardComponent} from './dashboard/dashboard.component';
import {LayoutModule} from '@angular/cdk/layout';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatButtonModule} from '@angular/material/button';
import {MatSidenavModule} from '@angular/material/sidenav';
import {MatIconModule} from '@angular/material/icon';
import {MatListModule} from '@angular/material/list';
import {LoginComponent} from './login/login.component';
import {GridsterModule} from 'angular-gridster2';
import {NgbModule, NgbActiveModal} from '@ng-bootstrap/ng-bootstrap';
import {FormsModule, ReactiveFormsModule} from '@angular/forms';
import {HttpClientModule} from '@angular/common/http';
import { ParentDynamicComponent } from './parent-dynamic/parent-dynamic.component';
import { WidgetWeatherLightComponent } from './widget-weather-light/widget-weather-light.component';
import {AuthGuard} from './auth.guard';
import { WidgetWeatherBigComponent } from './widget-weather-big/widget-weather-big.component';
import { AboutComponent } from './about/about.component';
import { ListOfUsersComponent } from './list-of-users/list-of-users.component';
import {LocalStorageService} from 'ngx-store';
import { WidgetWeatherDayComponent } from './widget-weather-day/widget-weather-day.component';
import { WidgetSoundcloudProfileComponent } from './widget-soundcloud-profile/widget-soundcloud-profile.component';
import { WidgetSoundcloudDiscoverComponent } from './widget-soundcloud-discover/widget-soundcloud-discover.component';
import { WidgetSoundcloudTopComponent } from './widget-soundcloud-top/widget-soundcloud-top.component';
import { WidgetNewsSubjectComponent } from './widget-news-subject/widget-news-subject.component';
import { WidgetNewsRegionComponent } from './widget-news-region/widget-news-region.component';
import { WidgetNewsMediaComponent } from './widget-news-media/widget-news-media.component';
import { LoginCallbackComponent } from './login-callback/login-callback.component';


@NgModule({
    declarations: [
        AppComponent,
        DashboardComponent,
        LoginComponent,
        ParentDynamicComponent,
        WidgetWeatherLightComponent,
        WidgetWeatherBigComponent,
        AboutComponent,
        ListOfUsersComponent,
        WidgetWeatherDayComponent,
        WidgetSoundcloudProfileComponent,
        WidgetSoundcloudDiscoverComponent,
        WidgetSoundcloudTopComponent,
        WidgetNewsSubjectComponent,
        WidgetNewsRegionComponent,
        WidgetNewsMediaComponent,
        LoginCallbackComponent
    ],
    imports: [
        NgbModule,
        GridsterModule,
        BrowserModule,
        AppRoutingModule,
        BrowserAnimationsModule,
        LayoutModule,
        MatToolbarModule,
        MatButtonModule,
        MatSidenavModule,
        MatIconModule,
        MatListModule,
        FormsModule,
        HttpClientModule,
        ReactiveFormsModule
    ],
    providers: [
        NgbActiveModal,
        AuthGuard,
        LocalStorageService
    ],
    bootstrap: [AppComponent]
})
export class AppModule {
}
