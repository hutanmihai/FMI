using SissaCoffee.Models;
using SissaCoffee.Repositories.IngredientRepository;

namespace SissaCoffee.Helpers.Seeders;

public class IngredientSeeder
{
    private readonly IIngredientRepository _ingredientRepository;
    
    public IngredientSeeder(IIngredientRepository ingredientRepository)
    {
        _ingredientRepository = ingredientRepository;
    }

    public void SeedIngredients()
    {
        var ingredients = new List<Ingredient>()
        {
            new()
            {
                Name = "Milk",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Sugar",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Coffee",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Water",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Chocolate IceCream",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Whipped Cream",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Instant Coffee",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            }
        };

        foreach (var ingredient in ingredients)
        {
            if (_ingredientRepository.FindByName(ingredient.Name) is null)
            {
                _ingredientRepository.Create(ingredient);
            }
        }
    }
}