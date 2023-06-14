import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {ProductsComponent} from './components/products/products.component';
import {AuthGuard} from "../auth/guards/auth.guard";
import {ProductAddComponent} from "./components/product-add/product-add.component";

const routes: Routes = [
  {
    path: 'list',
    component: ProductsComponent,
    canActivate: [AuthGuard],
  },
  {
    path: 'new',
    component: ProductAddComponent,
    canActivate: [AuthGuard],
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProductsRoutingModule {
}
