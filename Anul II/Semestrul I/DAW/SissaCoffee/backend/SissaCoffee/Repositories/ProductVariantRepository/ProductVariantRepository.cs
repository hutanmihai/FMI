using Microsoft.EntityFrameworkCore;
using SissaCoffee.Data;
using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.ProductVariantRepository;

public class ProductVariantRepository: GenericRepository<ProductVariant>, IProductVariantRepository
{
    public ProductVariantRepository(AppDbContext context) : base(context)
    {
    }
    
    public ProductVariant? FindByName(string name)
    {
        return _table.FirstOrDefault(e => e.Name == name);
    }
}