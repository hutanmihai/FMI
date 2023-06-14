import {Injectable} from '@angular/core';
import {environment} from "../../../../environments/environment";
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {IProduct, IProductCreate} from "../../../interfaces/product";

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  constructor(private httpClient: HttpClient) {
  }

  getProducts(): Observable<IProduct[]> {
    return this.httpClient.get<IProduct[]>(`${environment.apiUrl}/products`);
  }

  addProduct(product: IProductCreate): Observable<IProduct> {
    return this.httpClient.post<IProduct>(`${environment.apiUrl}/products`, product);
  }

  deleteProductById(productId: string): Observable<any> {
    return this.httpClient.delete(`${environment.apiUrl}/products/` + productId);
  }
}
