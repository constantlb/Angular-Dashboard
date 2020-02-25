import {ChangeDetectionStrategy, ChangeDetectorRef, Component, EventEmitter, OnInit, ViewChild, ViewEncapsulation} from '@angular/core';
import {BreakpointObserver, Breakpoints} from '@angular/cdk/layout';
import {Observable} from 'rxjs';
import {map, shareReplay} from 'rxjs/operators';
import {DisplayGrid, GridsterConfig, GridsterItem, GridType} from 'angular-gridster2';
import {NgbModal} from '@ng-bootstrap/ng-bootstrap';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {StorageService} from '../storage.service';
import {log} from 'util';

@Component({
    selector: 'app-dashboard',
    templateUrl: './dashboard.component.html',
    styleUrls: ['./dashboard.component.css'],
    encapsulation: ViewEncapsulation.None,
    changeDetection: ChangeDetectionStrategy.OnPush
})

export class DashboardComponent implements OnInit {

    inputLocal = {
        weatherPlaceLight: '',
        refreshTime: '',
        weatherPlaceBig: '',
        weatherPlaceDay: '',
        soundcloudUsername: '',
        soundcloudMusictype: '',
        soundcloudArtist: '',
        soundCloudCountry: '',
        soundCloudGenre: '',
        newsSubject: '',
        newsRegion: '',
        newsRegionCat: '',
        newsMedia: ''
    };

    receiveFromPost = {
        idWidget: ''
    };

    infoWidget;


    // @ts-ignore
    @ViewChild('modalAdd') modalAdd;
    // @ts-ignore
    @ViewChild('modalWeather') modalWeather;
    // @ts-ignore
    @ViewChild('modalWeatherLight') modalWeatherLight;
    // @ts-ignore
    @ViewChild('modalWeatherBig') modalWeatherBig;
    // @ts-ignore
    @ViewChild('modalWeatherDay') modalWeatherDay;
    // @ts-ignore
    @ViewChild('modalSoundcloud') modalSoundcloud;
    // @ts-ignore
    @ViewChild('modalSoundcloudProfile') modalSoundcloudProfile;
    // @ts-ignore
    @ViewChild('modalSoundcloudDiscover') modalSoundcloudDiscover;
    // @ts-ignore
    @ViewChild('modalSoundcloudTop') modalSoundcloudTop;
    // @ts-ignore
    @ViewChild('modalNews') modalNews;
    // @ts-ignore
    @ViewChild('modalNewsSubject') modalNewsSubject;
    // @ts-ignore
    @ViewChild('modalNewsRegion') modalNewsRegion;
    // @ts-ignore
    @ViewChild('modalNewsMedia') modalNewsMedia;


    resizeEvent: EventEmitter<any> = new EventEmitter<any>();
    isHandset$: Observable<boolean> = this.breakpointObserver.observe(Breakpoints.Handset)
        .pipe(
            map(result => result.matches),
            shareReplay()
        );

    baseUrl = 'http://localhost:5000';
    requestWidget = this.baseUrl + '/users/' + this.store.getData('id') + '/widgets';
    id;
    data;

    constructor(private breakpointObserver: BreakpointObserver, private modalService: NgbModal, private http: HttpClient,
                private store: StorageService, private ref: ChangeDetectorRef) {
        this.id = this.store.getData('id');
    }

    options: GridsterConfig;
    dashboard: Array<GridsterItem>;

    public open(): void {
        this.modalService.open(this.modalAdd);
    }

    public openModalWeather(): void {
        this.modalService.open(this.modalWeather);
    }

    public openModalWeatherLight(): void {
        this.modalService.open(this.modalWeatherLight);
    }

    public openModalWeatherBig(): void {
        this.modalService.open(this.modalWeatherBig);
    }

    public openModalWeatherDay(): void {
        this.modalService.open(this.modalWeatherDay);
    }

    public openModalSoundcloud(): void {
        this.modalService.open(this.modalSoundcloud);
    }

    public openModalSoundcloudProfile(): void {
        this.modalService.open(this.modalSoundcloudProfile);
    }

    public openModalSoundcloudDiscover(): void {
        this.modalService.open(this.modalSoundcloudDiscover);
    }

    public openModalSoundcloudTop(): void {
        this.modalService.open(this.modalSoundcloudTop);
    }

    public openModalNews(): void {
        this.modalService.open(this.modalNews);
    }

    public openModalNewsSubject(): void {
        this.modalService.open(this.modalNewsSubject);
    }

    public openModalNewsRegion(): void {
        this.modalService.open(this.modalNewsRegion);
    }

    public openModalNewsMedia(): void {
        this.modalService.open(this.modalNewsMedia);
    }

    // Creator of widgets


    async createWidgetWeatherLight() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-weather-light',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.weatherPlaceLight
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 1, rows: 1, y: 0, x: 0, type: 'widget-weather-light', city: this.inputLocal.weatherPlaceLight,
                        time: this.inputLocal.refreshTime, idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    async createWidgetWeatherBig() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-weather-big',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.weatherPlaceBig
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 1, rows: 1, y: 0, x: 0, type: 'widget-weather-big', city: this.inputLocal.weatherPlaceBig,
                        time: this.inputLocal.refreshTime, idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    async createWidgetWeatherDay() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-weather-day',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.weatherPlaceDay
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 1, rows: 1, y: 0, x: 0, type: 'widget-weather-day', city: this.inputLocal.weatherPlaceDay,
                        time: this.inputLocal.refreshTime, idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    async createWidgetSoundcloudProfile() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-soundcloud-profile',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.soundcloudUsername
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 1, rows: 2, y: 0, x: 0, type: 'widget-soundcloud-profile', username: this.inputLocal.soundcloudUsername,
                        time: this.inputLocal.refreshTime, idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    async createWidgetSoundcloudDiscover() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-soundcloud-discover',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.soundCloudCountry,
                this.inputLocal.soundCloudGenre
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 2, rows: 2, y: 0, x: 0, type: 'widget-soundcloud-discover', country: this.inputLocal.soundCloudCountry,
                        music_genre: this.inputLocal.soundCloudGenre, time: this.inputLocal.refreshTime,
                        idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    async createWidgetSoundcloudTop() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-soundcloud-top',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.soundcloudArtist
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 1, rows: 1, y: 0, x: 0, type: 'widget-soundcloud-top', city: this.inputLocal.soundcloudArtist,
                        time: this.inputLocal.refreshTime, idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    async createWidgetNewsSubject() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-news-subject',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.newsSubject
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 1, rows: 3, y: 0, x: 0, type: 'widget-news-subject', city: this.inputLocal.newsSubject,
                        time: this.inputLocal.refreshTime, idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    async createWidgetNewsRegion() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-news-region',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.newsRegion,
                this.inputLocal.newsRegionCat
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 1, rows: 3, y: 0, x: 0, type: 'widget-news-region', city: this.inputLocal.newsRegion,
                        cat: this.inputLocal.newsRegionCat, time: this.inputLocal.refreshTime, idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    async createWidgetNewsMedia() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            type: 'widget-news-media',
            refresh_time: this.inputLocal.refreshTime,
            params: [
                this.inputLocal.newsMedia
            ],
            position: {
                x: 0,
                y: 0
            }
        };
        await this.http.post(this.requestWidget, body, httpOptions)
            .subscribe(success => {
                    this.ref.markForCheck();
                    console.log(success.body as any);
                    // @ts-ignore
                    console.log(success.body.data.id);
                    // @ts-ignore
                    this.receiveFromPost.idWidget = success.body.data.id;
                    this.dashboard.push({
                        cols: 1, rows: 3, y: 0, x: 0, type: 'widget-news-media', city: this.inputLocal.newsMedia,
                        time: this.inputLocal.refreshTime, idWidget: this.receiveFromPost.idWidget
                    });
                },
                error => {
                    console.log(error);
                }
            );
    }

    public clearStorage(): void {
        this.store.clearLocal();
    }

    /*public itemChange(item: GridsterItem): void {
        const requestPositions = this.baseUrl + '/widgets/positions';
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const body = {
            x: item.x,
            y: item.y,
            widget_id: item.id
        };
        this.http.post(requestPositions, body, httpOptions)
            .subscribe(success => {
                    console.log(success.body as any);
                    console.log(item.id);
                },
                error => {
                    console.log(error);
                }
            );
        console.log(item);
    }*/


    async ngOnInit() {

        // Init widgets of the user //

        const requestGETallWidgetsOfTheUser = this.baseUrl + '/users/' + this.store.getData('id') + '/widgets';

        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };

        await this.http.get(requestGETallWidgetsOfTheUser, httpOptions)
            .subscribe(success => {
                    console.log(success.body as any);
                    this.ref.markForCheck();
                    // @ts-ignore
                    this.data = success.body.data;
                    this.loadWidgets();
                }, error => {
                    console.log(error);
                }
            );

        // Options gridster //

        this.options = {
            gridType: GridType.VerticalFixed,
            displayGrid: DisplayGrid.None,
            draggable: {
                enabled: true,
            },
            resizable: {
                enabled: false,
            },
            scrollToNewItems: false,
            disableWarnings: false,
            ignoreMarginInRow: false,
            disableWindowResize: false,
            //itemChangeCallback: this.itemChange.bind(this),
            pushItems: true,
            minCols: 5,
            maxCols: 5,
            minRows: 5,
            fixedRowHeight: 164,
            itemResizeCallback: (item) => {
                this.resizeEvent.emit(item);
            }
        };
        this.dashboard = [];
    }

    loadWidgets() {
        for (const each of this.data) {
            console.log(each);
            console.log(each.params[0]);
            if (each.type === 'widget-weather-light') {
                this.dashboard.push({cols: 1, rows: 1, y: 0, x: 0, type: 'widget-weather-light', city: each.params[0],
                    time: 12, idWidget: each.id});
            } else if (each.type === 'widget-weather-big') {
                this.dashboard.push({cols: 1, rows: 1, y: 0, x: 0, type: 'widget-weather-big', city: each.params[0],
                    time: 12, idWidget: each.id});
            } else if (each.type === 'widget-weather-day') {
                this.dashboard.push({cols: 1, rows: 1, y: 0, x: 0, type: 'widget-weather-day', city: each.params[0],
                    time: 12, idWidget: each.id});
            } else if (each.type === 'widget-soundcloud-profile') {
                this.dashboard.push({cols: 1, rows: 2, y: 0, x: 0, type: 'widget-soundcloud-profile', user: each.params[0],
                    time: 12, idWidget: each.id});
            } else if (each.type === 'widget-soundcloud-discover') {
                this.dashboard.push({cols: 2, rows: 2, y: 0, x: 0, type: 'widget-soundcloud-discover',
                    country: each.params[0], music_genre: each.params[1], time: 12, idWidget: each.id});
            } else if (each.type === 'widget-soundcloud-top') {
                this.dashboard.push({cols: 1, rows: 1, y: 0, x: 0, type: 'widget-soundcloud-top', user: each.params[0],
                    time: 12, idWidget: each.id});
            } else if (each.type === 'widget-news-subject') {
                this.dashboard.push({cols: 1, rows: 3, y: 0, x: 0, type: 'widget-news-subject', subject: each.params[0],
                    time: 12, idWidget: each.id});
            } else if (each.type === 'widget-news-region') {
                this.dashboard.push({cols: 1, rows: 3, y: 0, x: 0, type: 'widget-news-region', region: each.params[0], cat: each.params[1],
                    time: 12, idWidget: each.id});
            } else if (each.type === 'widget-news-media') {
                this.dashboard.push({cols: 1, rows: 3, y: 0, x: 0, type: 'widget-news-media', media: each.params[0],
                    time: 12, idWidget: each.id});
            }
        }
    }

    removeItem($event, item) {
        $event.preventDefault();
        $event.stopPropagation();
        this.dashboard.splice(this.dashboard.indexOf(item), 1);

        const requestDELETEWidget = this.baseUrl + '/users/' + this.store.getData('id') + '/widgets/' + item.idWidget;

        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };

        this.http.delete(requestDELETEWidget, httpOptions)
            .subscribe(success => {
                console.log(success.body as any);
        }, error => {
                console.log(error);
            }
        );
    }

    editItem($event, item) {
        $event.preventDefault();
        $event.stopPropagation();
        this.dashboard.splice(this.dashboard.indexOf(item), 1);

        const request = this.baseUrl + '/users/' + this.store.getData('id') + '/widgets/' + item.idWidget;

        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };

        this.http.get(request, httpOptions)
            .subscribe(success => {
                console.log(success.body as any);
                this.ref.markForCheck();
                // @ts-ignore
                this.infoWidget = success.body.data;
                if (this.infoWidget.type === 'widget-weather-light') {
                    this.openModalWeatherLight();
                } else if (this.infoWidget.type === 'widget-weather-big') {
                    this.openModalWeatherBig();
                } else if (this.infoWidget.type === 'widget-weather-day') {
                    this.openModalWeatherDay();
                } else if (this.infoWidget.type === 'widget-soundcloud-profile') {
                    this.openModalSoundcloudProfile();
                } else if (this.infoWidget.type === 'widget-soundcloud-discover') {
                    this.openModalSoundcloudDiscover();
                } else if (this.infoWidget.type === 'widget-soundcloud-top') {
                    this.openModalSoundcloudTop();
                } else if (this.infoWidget.type === 'widget-news-subject') {
                    this.openModalNewsSubject();
                } else if (this.infoWidget.type === 'widget-news-region') {
                    this.openModalNewsRegion();
                } else if (this.infoWidget.type === 'widget-news-media') {
                    this.openModalNewsMedia();
                }
            }, error => {
                console.log(error);
            });

        this.http.delete(request, httpOptions)
            .subscribe(success => {
                    console.log(success.body as any);
                }, error => {
                    console.log(error);
                }
            );
    }
}
