using Microsoft.AspNetCore.Mvc;
using SissaCoffee.Helpers.Attributes;
using SissaCoffee.Models;
using SissaCoffee.Models.DTOs.Product;
using SissaCoffee.Services.ProductService;

namespace SissaCoffee.Controllers;

[ApiController]
[Route("/api/products")]
public class ProductController : ControllerBase
{
    private readonly IProductService _productService;

    public ProductController(IProductService productService)
    {
        _productService = productService;
    }

    [HttpGet]
    [Authorization("Customer")]
    public async Task<IActionResult> GetProducts()
    {
        var products = await _productService.GetAllProductsAsync();
        return Ok(products);
    }
    
    [HttpGet("{id}")]
    [Authorization("Admin")]
    public async Task<IActionResult> GetProduct(Guid id)
    {
        try
        {
            var product = await _productService.GetProductByIdAsync(id);
            return Ok(product);
        }
        catch
        {
            return NotFound();
        }
    }
    
    [HttpPut("{id}")]
    [Authorization("Admin")]
        public async Task<IActionResult> PutProduct(Guid id, [FromBody] ProductUpdateDTO dto)
        {
            try
            {
                await _productService.UpdateProductAsync(id, dto);
                return Ok();
            }
            catch (Exception e)
            {
                return BadRequest(e.Message);
            }
        }

        [HttpPost]
        [Authorization("Admin")]
        public async Task<ActionResult<ProductDTO>> PostProduct([FromBody] ProductCreateDTO dto)
        {
            try
            {
                return await _productService.CreateProductAsync(dto);
            }
            catch (Exception e)
            {
                return BadRequest(e.Message);
            }
        }
        
        [HttpDelete("{id}")]
        [Authorization("Admin")]
        public async Task<IActionResult> DeleteProduct(Guid id)
        {
            try
            {
                await _productService.DeleteProductAsync(id);
                return Accepted();
            }
            catch (Exception e)
            {
                return BadRequest(e.Message);
            }
        }
}