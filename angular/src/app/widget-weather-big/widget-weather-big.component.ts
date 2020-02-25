import {
    ChangeDetectionStrategy,
    ChangeDetectorRef,
    Component,
    EventEmitter,
    Input,
    OnDestroy,
    OnInit,
    ViewEncapsulation
} from '@angular/core';
import {Subscription} from 'rxjs';
import {StorageService} from '../storage.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Component({
    selector: 'app-widget-weather-big',
    templateUrl: './widget-weather-big.component.html',
    styleUrls: ['./widget-weather-big.component.css'],
    changeDetection: ChangeDetectionStrategy.OnPush,
    encapsulation: ViewEncapsulation.None
})

export class WidgetWeatherBigComponent implements OnInit, OnDestroy {

    @Input() widget;
    @Input() resizeEvent: EventEmitter<any>;
    data;
    resizeSub: Subscription;
    baseUrl = 'http://localhost:5000';
    id;

    constructor(private store: StorageService, private http: HttpClient, private ref: ChangeDetectorRef) {
        this.id = this.store.getData('id');
    }

    ngOnInit() {
        console.log('wesh on vas faire la requette');
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };
        const requestGETWidgetWeatherBig = this.baseUrl + '/users/' + this.store.getData('id') + '/widgets/' +
            this.widget.idWidget + '/data';

        this.http.get(requestGETWidgetWeatherBig, httpOptions)
            .subscribe(success => {
                    console.log(success.body as any);
                    this.ref.markForCheck();
                    // @ts-ignore
                    this.data = success.body.data;
                },
                error => {
                    console.log(error);
                }
            );
    }

    ngOnDestroy() {
        this.resizeSub.unsubscribe();
    }

}
