using SissaCoffee.Models.Base;

namespace SissaCoffee.Models;

public class Ingredient: BaseEntity
{
    public string Name { get; set; } = String.Empty;
    
    public ICollection<ProductIngredient> Products { get; set; } = new List<ProductIngredient>();
}