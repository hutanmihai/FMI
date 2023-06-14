import { Component, OnInit } from '@angular/core';
import { IProduct } from "../../../../interfaces/product";
import { ProductService } from "../../services/product.service";
import { AuthService } from "../../../auth/services/auth.service";
import { UserRole } from "../../../../models/user";

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
  products: IProduct[] = [];

  constructor(
    private authService: AuthService,
    private productService: ProductService,
  ) { }

  ngOnInit(): void {
    this.productService.getProducts().subscribe((res: IProduct[]) => {
      this.products = res;
    });
  }

  deleteProduct(productId: string): void {
    this.productService.deleteProductById(productId).subscribe((_) =>{
      {
        this.products = this.products.filter((prod: IProduct) => prod.id !== productId);
      }
    });
  }

  userCanEdit(): boolean {
    return this.authService.checkRole(UserRole.Admin);
  }
}
