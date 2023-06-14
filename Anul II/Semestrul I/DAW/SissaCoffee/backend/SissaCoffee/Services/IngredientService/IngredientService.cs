using SissaCoffee.Models;
using SissaCoffee.Repositories.IngredientRepository;

namespace SissaCoffee.Services.IngredientService;

public class IngredientService: IIngredientService
{
    private readonly IIngredientRepository _ingredientRepository;
    public IngredientService(IIngredientRepository ingredientRepository)
    {
        _ingredientRepository = ingredientRepository;
    }
    
    public async Task<List<Ingredient>> GetAllIngredientsAsync()
    {
        return await _ingredientRepository.GetAllAsync();
    }
}