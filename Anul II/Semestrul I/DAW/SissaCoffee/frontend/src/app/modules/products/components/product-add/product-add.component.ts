import {Component, OnInit} from "@angular/core";
import {FormArray, FormControl, FormGroup, Validators} from "@angular/forms";
import {ProductService} from "../../services/product.service";
import {Router} from "@angular/router";
import {IIngredient} from "../../../../interfaces/ingredient";
import {IngredientService} from "../../services/ingredient.service";
import {IProduct, IProductCreate} from "../../../../interfaces/product";
import {ITag} from "../../../../interfaces/tag";
import {IProductVariant} from "../../../../interfaces/product-variant";
import {TagService} from "../../services/tag.service";
import {ProductVariantService} from "../../services/product-variant.service";

@Component({
  selector: "app-product-add",
  templateUrl: "./product-add.component.html",
  styleUrls: ["./product-add.component.css"],
})
export class ProductAddComponent implements OnInit {
  formGroup: FormGroup = new FormGroup({
    name: new FormControl("", Validators.required),
    ingredients: new FormArray([]),
    tag: new FormControl(null),
    variant: new FormControl(null),
  });

  products!: IProduct[];
  ingredients!: IIngredient[];
  tags!: ITag[];
  variants!: IProductVariant[];


  constructor(
    private productService: ProductService,
    private router: Router,
    private ingredientService: IngredientService,
    private tagService: TagService,
    private variantService: ProductVariantService
  ) {
  }

  ngOnInit(): void {
    this.ingredientService.getIngredients().subscribe((res: IIngredient[]) => {
      this.ingredients = res;
      this.ingredients.forEach((_) => (this.formGroup.get("ingredients") as FormArray).push(new FormControl(false)));
    });
    this.tagService.getTags().subscribe((res: ITag[]) => {
      this.tags = res;
    });
    this.variantService.getVariants().subscribe((res: IProductVariant[]) => {
      this.variants = res;
    });
    this.productService.getProducts().subscribe((res: IProduct[]) => (this.products = res));
  }

  goToPage(pageName: string): void {
    this.router.navigate([`${pageName}`]);
  }

  addProd(): void {
    const arrayControl = (this.formGroup.get("ingredients") as FormArray);
    const ingredients = this.ingredients.filter((_, index) => arrayControl.at(index).value);
    const product: IProductCreate = {
      ingredients: ingredients.map((x: IIngredient) => x.id),
      name: this.formGroup.get("name")!.value,
      // @ts-ignore
      tag: this.formGroup.get("tag").value,
      variant: this.formGroup.get("variant")!.value,
    };


    this.productService.addProduct(product).subscribe({
      next: (_) => {
        this.goToPage(`/products/list`);
      },
    });
  }
}
