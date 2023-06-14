namespace SissaCoffee.Models.DTOs.Product;

public class TagResponseDTO
{
    public Guid id { get; set; }
    public string name { get; set; }
}

public class VariantResponseDTO
{
    public Guid id { get; set; }
    public string name { get; set; }
    public int size { get; set; }
    public string unit { get; set; }
}

public class IngredientResponseDTO
{
    public Guid id { get; set; }
    public string name { get; set; }
}

public class ProductResponseDTO
{
    public Guid id { get; set; }
    public string name { get; set; }
    public VariantResponseDTO variant { get; set; }
    public IngredientResponseDTO[] ingredients { get; set; }
    public TagResponseDTO? tag { get; set; }
}