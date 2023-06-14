import { Product } from './product';

export interface MealProductBody {
  product_id: string;
  quantity_grams: number;
}

export interface MealProduct extends Product {
  quantity_grams: number;
}

export interface Meal {
  id: string;
  name: string;
  total_calories: number;
  total_fat: number;
  total_carbs: number;
  total_protein: number;
  products: MealProduct[];
}
