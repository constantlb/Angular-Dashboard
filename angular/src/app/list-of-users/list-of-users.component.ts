import {
    ChangeDetectionStrategy,
    ChangeDetectorRef,
    Component,
    EventEmitter,
    Input,
    OnInit,
    ViewChild,
    ViewEncapsulation
} from '@angular/core';
import {StorageService} from '../storage.service';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Component({
    selector: 'app-list-of-users',
    templateUrl: './list-of-users.component.html',
    styleUrls: ['./list-of-users.component.css'],
    encapsulation: ViewEncapsulation.None,
    changeDetection: ChangeDetectionStrategy.OnPush
})

export class ListOfUsersComponent implements OnInit {

    @Input() widget;
    @Input() resizeEvent: EventEmitter<any>;
    data;
    baseUrl = 'http://localhost:5000';
    id;

    bookList = [
        {
            name: 'eXtreme Programming Explained'
        },
        {
            name: 'Clean Code'
        }
    ];

    constructor(private store: StorageService, private http: HttpClient, private ref: ChangeDetectorRef) {
        this.id = this.store.getData('id');
    }

    ngOnInit() {
        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };

        const requestGET = this.baseUrl + '/users';

        this.http.get(requestGET, httpOptions)
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

    removeUser($event, id) {
        $event.preventDefault();
        $event.stopPropagation();

        const request = this.baseUrl + '/users/' + id;
        console.log(id);

        const httpOptions = {
            headers: new HttpHeaders({Authorization: this.id}),
            observe: 'response' as 'response'
        };

        this.http.delete(request, httpOptions)
            .subscribe(success => {
                    console.log(success.body as any);
                    window.location.reload();
                }, error => {
                    console.log(error);
                }
            );
    }

}
