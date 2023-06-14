using AutoMapper.QueryableExtensions;
using Microsoft.EntityFrameworkCore;
using SissaCoffee.Repositories.GenericRepository;
using SissaCoffee.Data;
using SissaCoffee.Models;
using SissaCoffee.Models.DTOs.Product;

namespace SissaCoffee.Repositories.ProductRepository;

public class ProductRepository: GenericRepository<Product>, IProductRepository
{
    public ProductRepository(AppDbContext context) : base(context)
    {
    }
    
    public async Task<List<Product>> GetAllProductsAsync()
    {
        return await _table
            .Include(p => p.Ingredients)
            .ThenInclude(x => x.Ingredient)
            .Include(p => p.Variant)
            .Include(p => p.Tag)
            .ToListAsync();
    }
    
    public async Task<Product?> GetProductByIdAsync(Guid id)
    {
        var product = await _table
            .Include(p => p.Ingredients)
            .ThenInclude(pi => pi.Ingredient)
            .Include(p => p.Variant)
            .Include(p => p.Tag)
            .FirstOrDefaultAsync(p => p.Id == id);
        return product ?? null;
    }

    public async Task<ProductResponseDTO?> GetProductById2Async(Guid id)
    {
        var product = await _table
            .Where(p => p.Id == id)
            .Select(p => new ProductResponseDTO
            {
                id = p.Id,
                name = p.Name,
                variant = new VariantResponseDTO
                {
                    id = p.Variant.Id,
                    name = p.Variant.Name,
                    size = p.Variant.Size,
                    unit = p.Variant.Unit
                },
                ingredients = p.Ingredients.Select(i => new IngredientResponseDTO
                {
                    id = i.Ingredient.Id,
                    name = i.Ingredient.Name
                }).ToArray(),
                tag = new TagResponseDTO
                {
                    id = p.Tag.Id,
                    name = p.Tag.Name 
                }
            }).FirstOrDefaultAsync();
        return product ?? null;
    }
}