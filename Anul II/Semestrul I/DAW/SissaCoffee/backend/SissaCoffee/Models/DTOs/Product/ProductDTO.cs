namespace SissaCoffee.Models.DTOs.Product;

public class ProductDTO
{
    public Guid Id { get; set; } = Guid.Empty;
    public string Name { get; set; } = String.Empty;
    public string? Tag { get; set; }
    public ProductVariantDTO Variant { get; set; } = new ProductVariantDTO();
    public List<string> Ingredients { get; set; } = new List<string>();
}