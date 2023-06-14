using Microsoft.AspNetCore.Mvc;
using SissaCoffee.Helpers.Attributes;
using SissaCoffee.Models;
using SissaCoffee.Services.ProductVariantService;

namespace SissaCoffee.Controllers;

[Route("api/variants")]
[ApiController]
public class ProductVariantController : ControllerBase
{
    private readonly IProductVariantService _productVariantService;
    public ProductVariantController(IProductVariantService productVariantService)
    {
        _productVariantService = productVariantService;
    }

    [HttpGet]
    [Authorization("Admin")]
    public async Task<ActionResult<IEnumerable<ProductVariant>>> GetIngredients()
    {
        return await _productVariantService.GetAllVariantsAsync();
    }
}