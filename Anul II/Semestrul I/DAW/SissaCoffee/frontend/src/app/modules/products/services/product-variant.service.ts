import {Injectable} from '@angular/core';
import {Observable} from "rxjs";
import {IProductVariant} from "../../../interfaces/product-variant";
import {environment} from "../../../../environments/environment";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class ProductVariantService {
  constructor(private httpClient: HttpClient) {
  }

  getVariants(): Observable<IProductVariant[]> {
    return this.httpClient.get<IProductVariant[]>(`${environment.apiUrl}/variants/`);
  }
}
