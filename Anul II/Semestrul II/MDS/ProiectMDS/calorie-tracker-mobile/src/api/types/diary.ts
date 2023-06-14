import { Product } from './product';

export interface DiaryProductBody {
  product_id: string;
  quantity_grams: number;
  is_from_meal?: boolean;
}

export interface DiaryProduct extends Product {
  quantity_grams: number;
}

export interface Diary {
  id: string;
  date: string;
  total_calories: number;
  total_fat: number;
  total_carbs: number;
  total_protein: number;
  products: DiaryProduct[];
}
