export interface Product {
  id: string;
  name: string;
  calories: number;
  fat: number;
  carbs: number;
  protein: number;
  upvotes: number;
  downvotes: number;
}

export interface ProductVote {
  id: string;
  vote: number;
}
