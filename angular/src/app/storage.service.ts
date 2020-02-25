import {Injectable} from '@angular/core';
import {LocalStorageService} from 'ngx-store';

@Injectable({
    providedIn: 'root'
})
export class StorageService {

    constructor(public localstorage: LocalStorageService) {
    }

    public saveData(string, value: any) {
        this.localstorage.set(string, value);
    }

    public getData(str) {
        return (this.localstorage.get(str));
    }

    public clearLocal() {
        this.localstorage.clear();
    }
}
