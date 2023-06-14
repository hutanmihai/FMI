using SissaCoffee.Models.Base;

namespace SissaCoffee.Models;

public class ProductVariant: BaseEntity
{
    public string Name { get; set; } = String.Empty;
    public int Size { get; set; } = 0;
    public string Unit { get; set; } = String.Empty;
    
    public ICollection<Product> Products { get; set; } = new List<Product>();
}