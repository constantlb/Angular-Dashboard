import { Injectable } from '@angular/core';
import {StorageService} from './storage.service';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(public store: StorageService) { }

  logged() {
    return !!this.store.getData('id');
  }
}
