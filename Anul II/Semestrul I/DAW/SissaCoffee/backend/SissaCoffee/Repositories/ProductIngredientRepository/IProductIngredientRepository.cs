using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.ProductIngredientRepository;

public interface IProductIngredientRepository: IGenericRepository<ProductIngredient>
{
    public Task<List<ProductIngredient>> GetAllByProductIdAsync(Guid id);
}