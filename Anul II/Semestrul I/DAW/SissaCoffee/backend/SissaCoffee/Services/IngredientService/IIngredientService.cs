using SissaCoffee.Models;

namespace SissaCoffee.Services.IngredientService;

public interface IIngredientService
{
    public Task<List<Ingredient>> GetAllIngredientsAsync();
}