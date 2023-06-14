using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.UserRepository;

public interface IUserRepository: IGenericRepository<ApplicationUser>
{
    public Task<ApplicationUser?> GetUserByIdWithRolesAsync(Guid id);
    
    public Task<List<ApplicationUser>> GetUsersWithRolesAsync();
}