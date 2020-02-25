import {Component, OnInit} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Router} from '@angular/router';


@Component({
    selector: 'app-about',
    templateUrl: './about.component.html',
    styleUrls: ['./about.component.css']
})
export class AboutComponent implements OnInit {

    baseUrl = 'http://localhost:5000';
    data;

    constructor(private http: HttpClient, private router: Router) {
    }

    public getJson(): void {
        const url = this.baseUrl + '/about';
        const httpOptions = {
            headers: new HttpHeaders({'Content-Type': 'application/json'}),
            observe: 'response' as 'response'
        };
        this.http.get(url, httpOptions)
            .subscribe(success => {
                this.data = JSON.stringify(success, undefined, 2);
            }, error => {
                console.log(error);
            });
    }


    ngOnInit() {
      this.getJson();
    }

}
