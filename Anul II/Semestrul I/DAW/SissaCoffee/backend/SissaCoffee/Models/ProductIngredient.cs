using SissaCoffee.Models.Base;

namespace SissaCoffee.Models;

public class ProductIngredient: BaseEntity
{
    public Product Product { get; set; } = new();
    public Ingredient Ingredient { get; set; } = new();

    public Guid ProductId { get; set; } = Guid.Empty;
    public Guid IngredientId { get; set; } = Guid.Empty;
}