using Microsoft.EntityFrameworkCore;
using SissaCoffee.Data;
using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.ProductIngredientRepository;

public class ProductIngredientRepository: GenericRepository<ProductIngredient>, IProductIngredientRepository
{
    public ProductIngredientRepository(AppDbContext context) : base(context)
    { }

    public async Task<List<ProductIngredient>> GetAllByProductIdAsync(Guid id)
    {
        return await _table
            .Include(pi => pi.Ingredient)
            .Include(pi => pi.Product)
            .Where(pi => pi.ProductId == id).ToListAsync();
    }
}