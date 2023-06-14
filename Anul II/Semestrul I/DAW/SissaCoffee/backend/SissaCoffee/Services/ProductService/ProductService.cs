using AutoMapper;
using SissaCoffee.Models;
using SissaCoffee.Models.DTOs.Product;
using SissaCoffee.Repositories.IngredientRepository;
using SissaCoffee.Repositories.ProductIngredientRepository;
using SissaCoffee.Repositories.ProductRepository;
using SissaCoffee.Repositories.ProductVariantRepository;
using SissaCoffee.Repositories.TagRepository;

namespace SissaCoffee.Services.ProductService;

public class ProductService: IProductService
{
    private readonly IProductRepository _productRepository;
    private readonly IProductVariantRepository _productVariantRepository;
    private readonly IIngredientRepository _ingredientRepository;
    private readonly ITagRepository _tagRepository;
    private readonly IProductIngredientRepository _productIngredientRepository;
    private readonly IMapper _mapper;

    public ProductService(IProductRepository productRepository, IProductVariantRepository productVariantRepository, IIngredientRepository ingredientRepository, ITagRepository tagRepository, IProductIngredientRepository productIngredientRepository, IMapper mapper)
    {
        _productRepository = productRepository;
        _productVariantRepository = productVariantRepository;
        _ingredientRepository = ingredientRepository;
        _tagRepository = tagRepository;
        _productIngredientRepository = productIngredientRepository;
        _mapper = mapper;
    }

    public async Task<List<ProductDTO>> GetAllProductsAsync()
    {
        var products = await _productRepository.GetAllProductsAsync();
        return _mapper.Map<List<ProductDTO>>(products);
    }

    public async Task UpdateProductAsync(Guid id, ProductUpdateDTO dto)
    {
        var product = await _productRepository.GetProductByIdAsync(id);
        if (product is null)
        {
            throw new Exception("Product not found");
        }
        
        var variant = await _productVariantRepository.FindByIdAsync(dto.Variant);
        if (variant is null)
        {
            throw new Exception("Variant not found");
        }
        
        var tag = await _tagRepository.GetByIdAsync(dto.Tag);
        var currentlyUsedTags = await _productRepository.GetAllProductsAsync();
        foreach (var products in currentlyUsedTags)
        {
            if (products.Tag == tag)
            {
                throw new Exception("Tag already used");
            }
        }
        
        product.Name = dto.Name;
        product.Variant = variant;
        product.Tag = tag;
        product.UpdatedAt = DateTime.UtcNow;
        
        var currentIngredients = await _productIngredientRepository.GetAllByProductIdAsync(product.Id);
        
        foreach (var currentIngredient in currentIngredients)
        {
            if (!dto.Ingredients.Contains(currentIngredient.IngredientId))
            {
                product.Ingredients.Remove(currentIngredient);
                await _productIngredientRepository.DeleteAsync(currentIngredient);
            }
        }

        foreach (var ingredientId in dto.Ingredients)
        {
            var existingIngredient = currentIngredients.FirstOrDefault(i => i.IngredientId == ingredientId);
            if (existingIngredient == null)
            {
                var ingredient = await _ingredientRepository.FindByIdAsync(ingredientId);
                if (ingredient is null)
                {
                    throw new Exception("Ingredient not found");
                }
                var productIngredient = new ProductIngredient
                {
                    Id = Guid.NewGuid(),
                    Product = product,
                    Ingredient = ingredient,
                    CreatedAt = DateTime.UtcNow,
                    UpdatedAt = DateTime.UtcNow
                };
                await _productIngredientRepository.CreateAsync(productIngredient);
                product.Ingredients.Add(productIngredient);
            }
        }
        await _productRepository.UpdateAsync(product);
    }

    public async Task<ProductDTO> CreateProductAsync(ProductCreateDTO dto)
    {
        var variant = await _productVariantRepository.FindByIdAsync(dto.Variant);
        if (variant is null)
        {
            throw new Exception("Variant not found");
        }
        
        var tag = await _tagRepository.GetByIdAsync(dto.Tag);
        
        var currentlyUsedTags = await _productRepository.GetAllProductsAsync();
        foreach (var products in currentlyUsedTags)
        {
            if (products.Tag == tag && tag != null)
            {
                throw new Exception("Tag already used");
            }
        }
        
        var product = new Product
        {
            Id = Guid.NewGuid(),
            Name = dto.Name,
            Variant = variant,
            Tag = tag,
            CreatedAt = DateTime.UtcNow,
            UpdatedAt = DateTime.UtcNow
        };
        
        foreach (var ingredientId in dto.Ingredients)
        { 
            var ingredient = await _ingredientRepository.FindByIdAsync(ingredientId);
            if (ingredient is null)
            { 
                throw new Exception("Ingredient not found");
            } 
            var productIngredient = new ProductIngredient 
            { 
                Id = Guid.NewGuid(), 
                Product = product, 
                ProductId = product.Id,
                Ingredient = ingredient, 
                IngredientId = ingredient.Id,
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            };
            product.Ingredients.Add(productIngredient);
        }
        await _productRepository.CreateAsync(product);
        await _productRepository.SaveAsync();
        var createdProduct = await _productRepository.GetProductByIdAsync(product.Id);
        return _mapper.Map<ProductDTO>(createdProduct);
    }
    
    public async Task DeleteProductAsync(Guid id)
    {
        var product = await _productRepository.GetProductByIdAsync(id);
        if (product is null)
        {
            throw new Exception("Product not found");
        }
        await _productRepository.DeleteAsync(product);
    }

    public async Task<ProductResponseDTO> GetProductByIdAsync(Guid id)
    {
        var product = await _productRepository.GetProductById2Async(id);
        if (product is null)
        {
            throw new Exception("Product not found");
        }
        return product;
    }
}