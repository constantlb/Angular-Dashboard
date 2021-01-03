import {ChangeDetectorRef, Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {map} from 'rxjs/operators';
import {Observable} from 'rxjs';
import {HttpClient, HttpHeaders} from '@angular/common/http';

@Component({
    selector: 'app-login-callback',
    templateUrl: './login-callback.component.html',
    styleUrls: ['./login-callback.component.css']
})
export class LoginCallbackComponent implements OnInit {
    code;
    accessToken;

    constructor(private currentRoute: ActivatedRoute, private router: Router, private http: HttpClient) {
    }

    ngOnInit() {
        this.currentRoute.queryParams.subscribe(params => {
          this.code = params.code;
        });

        if (!this.code) {
            console.log('no code');
            this.router.navigateByUrl('/login');
        }

        this.postGithub();
    }

    public postGithub(): void {
        const url = 'https://github.com/login/oauth/access_token?client_id=48c9fbba490367c3bf7d&client_secret=85e3384b41d1cd670a7851605bae578e83633fa9&code=' + this.code;
        const httpOptions = {
            headers: new HttpHeaders({
              'Access-Control-Allow-Origin': '*'
            }),
            observe: 'response' as 'response'
        };
        this.http.post(url, {}, httpOptions)
            .subscribe(success => {
              console.log(success);
              this.accessToken = success.body as any;
            }, error => {
                console.log(error);
            });
    }
}
