using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.ProductVariantRepository;

public interface IProductVariantRepository: IGenericRepository<ProductVariant>
{
    public ProductVariant? FindByName(string name);
}