import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {HttpClient} from "@angular/common/http";
import {environment} from "../../../../environments/environment";
import {IIngredient} from "../../../interfaces/ingredient";

@Injectable({
  providedIn: 'root'
})
export class IngredientService {
  constructor(private httpClient: HttpClient) {
  }

  getIngredients(): Observable<IIngredient[]> {
    return this.httpClient.get<IIngredient[]>(`${environment.apiUrl}/ingredients`);
  }
}
