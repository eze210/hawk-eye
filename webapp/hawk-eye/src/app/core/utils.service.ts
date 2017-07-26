// src/app/core/utils.service.ts
import { Injectable } from '@angular/core';

@Injectable()
export class UtilsService {

  constructor() { }

  isLoaded(loading: boolean): boolean {
    return loading === false;
  }

}