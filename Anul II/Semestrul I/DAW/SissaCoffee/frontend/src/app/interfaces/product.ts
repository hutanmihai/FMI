import {IProductVariant} from "./product-variant";

export interface IProduct {
  id?: string;
  name: string;
  tag?: string;
  variant: IProductVariant;
  ingredients?: string[];
}

export interface IProductCreate {
  name: string;
  variant: string;
  ingredients: string[];
  tag?: string;
}
