import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../../../environments/environment";
import {ITag} from "../../../interfaces/tag";

@Injectable({
  providedIn: 'root'
})
export class TagService {
  constructor(private httpClient: HttpClient) {
  }

  getTags(): Observable<ITag[]> {
    return this.httpClient.get<ITag[]>(`${environment.apiUrl}/tags`);
  }
}
