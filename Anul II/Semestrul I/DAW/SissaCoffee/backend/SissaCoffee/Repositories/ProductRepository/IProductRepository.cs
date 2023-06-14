using SissaCoffee.Models;
using SissaCoffee.Models.DTOs.Product;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.ProductRepository;

public interface IProductRepository: IGenericRepository<Product>
{
    public Task<List<Product>> GetAllProductsAsync();

    public Task<Product?> GetProductByIdAsync(Guid id);

    public Task<ProductResponseDTO?> GetProductById2Async(Guid id);
}