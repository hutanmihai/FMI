using SissaCoffee.Models;

namespace SissaCoffee.Services.ProductVariantService;

public interface IProductVariantService
{
    public Task<List<ProductVariant>> GetAllVariantsAsync();
}