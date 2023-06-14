using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.IngredientRepository;

public interface IIngredientRepository: IGenericRepository<Ingredient>
{
    public Ingredient? FindByName(string name);
}