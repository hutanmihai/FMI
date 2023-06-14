using Microsoft.AspNetCore.Mvc;
using SissaCoffee.Helpers.Attributes;
using SissaCoffee.Models;
using SissaCoffee.Services.IngredientService;

namespace SissaCoffee.Controllers;

    [Route("api/ingredients")]
    [ApiController]
    [Authorization("Admin")]
    public class IngredientController : ControllerBase
    {
        private readonly IIngredientService _ingredientService;
        public IngredientController(IIngredientService ingredientService)
        {
            _ingredientService = ingredientService;
        }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Ingredient>>> GetIngredients()
        {
            return await _ingredientService.GetAllIngredientsAsync();
        }
    }
