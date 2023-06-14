using Microsoft.EntityFrameworkCore;
using SissaCoffee.Data;
using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.IngredientRepository;

public class IngredientRepository: GenericRepository<Ingredient>, IIngredientRepository
{
    public IngredientRepository(AppDbContext context) : base(context)
    {
    }
    
    public Ingredient? FindByName(string name)
    {
        return _table.FirstOrDefault(e => e.Name == name);
    }
}
