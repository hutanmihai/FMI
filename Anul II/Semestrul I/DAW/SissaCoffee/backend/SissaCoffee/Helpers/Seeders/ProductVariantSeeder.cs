using SissaCoffee.Models;
using SissaCoffee.Repositories.ProductVariantRepository;

namespace SissaCoffee.Helpers.Seeders;

public class ProductVariantSeeder
{
    private readonly IProductVariantRepository _productVariantRepository;
    
    public ProductVariantSeeder(IProductVariantRepository productVariantRepository)
    {
        _productVariantRepository = productVariantRepository;
    }

    public void SeedProductVariants()
    {
        var productVariants = new List<ProductVariant>()
        {
            new()
            {
                Name = "Small",
                Size = 30,
                Unit = "ml",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Tall",
                Size = 250,
                Unit = "ml",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Grande",
                Size = 330,
                Unit = "ml",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Venti",
                Size = 400,
                Unit = "ml",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
        };

        foreach (var productVariant in productVariants)
        {
            if (_productVariantRepository.FindByName(productVariant.Name) is null)
            {
                _productVariantRepository.Create(productVariant);
            }
        }
    }
}