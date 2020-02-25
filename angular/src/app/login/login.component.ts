import {Component, OnInit} from '@angular/core';
import * as $ from 'jquery';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Router} from '@angular/router';
import {StorageService} from '../storage.service';

@Component({
    selector: 'app-login',
    templateUrl: './login.component.html',
    styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
    loginV = {
        email: '',
        password: ''
    };
    register = {
        name: '',
        password: '',
        password_conf: '',
        email: ''
    };
    baseUrl = 'http://localhost:5000';
    id;

    constructor(private http: HttpClient, private router: Router, private store: StorageService) {
        this.id = store.getData('id');
    }

    public Register(): void {
        const url = this.baseUrl + '/users/';
        const httpOptions = {
            headers: new HttpHeaders({'Content-Type': 'application/json'}),
            observe: 'response' as 'response'
        };
        if (this.register.password === this.register.password_conf) {
            const body = {
                username: this.register.name,
                password: this.register.password,
                email: this.register.email
            };
            this.http.post(url, body, httpOptions)
                .subscribe(success => {
                    // @ts-ignore
                    this.store.saveData('account', success.body.data);
                    // @ts-ignore
                    this.store.saveData('id', success.body.data.id);
                    this.router.navigateByUrl('/dashboard');
                }, error => {
                    console.log(error);
                });
            console.log(this.register);
        } else {
            console.log('BAD PASSWORD');
        }
    }

    public SendLogin(): void {
        const url = this.baseUrl + '/users/login';
        const httpOptions = {
            headers: new HttpHeaders({'Content-Type': 'application/json'}),
            observe: 'response' as 'response'
        };
        const body = {
            email: this.loginV.email,
            password: this.loginV.password,
        };
        this.http.post(url, body, httpOptions)
            .subscribe(success => {
                // @ts-ignore
                this.store.saveData('account', success.body.data);
                // @ts-ignore
                this.store.saveData('id', success.body.data.id);
                this.router.navigateByUrl('/dashboard');
                console.log(success.body as any);
            }, error => {
                console.log(error);
            });
        console.log(this.loginV);
    }

    ngOnInit() {
        $(document).ready(function() {
            var panelOne = $('.form-panel.two').height(),
                panelTwo = $('.form-panel.two')[0].scrollHeight;

            $('.form-panel.two').not('.form-panel.two.active').on('click', function(e) {
                e.preventDefault();

                $('.form-toggle').addClass('visible');
                $('.form-panel.one').addClass('hidden');
                $('.form-panel.two').addClass('active');
                $('.form').animate({
                    'height': panelTwo
                }, 200);
            });

            $('.form-toggle').on('click', function(e) {
                e.preventDefault();
                $(this).removeClass('visible');
                $('.form-panel.one').removeClass('hidden');
                $('.form-panel.two').removeClass('active');
                $('.form').animate({
                    'height': panelOne
                }, 200);
            });
        });

    }

}
