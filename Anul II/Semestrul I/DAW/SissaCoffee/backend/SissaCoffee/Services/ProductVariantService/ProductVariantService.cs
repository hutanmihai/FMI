using SissaCoffee.Models;
using SissaCoffee.Repositories.ProductVariantRepository;

namespace SissaCoffee.Services.ProductVariantService;

public class ProductVariantService: IProductVariantService
{
    private readonly IProductVariantRepository _productVariantRepository;
    public ProductVariantService(IProductVariantRepository productVariantRepository)
    {
        _productVariantRepository = productVariantRepository;
    }
    
    public async Task<List<ProductVariant>> GetAllVariantsAsync()
    {
        return await _productVariantRepository.GetAllAsync();
    }
}