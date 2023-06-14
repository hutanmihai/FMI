using SissaCoffee.Models;

namespace SissaCoffee.Services.RoleService;

public interface IRoleService
{
    public Task<List<ApplicationRole>> GetAllRolesAsync();
    
    public Task<ApplicationRole?> GetRoleByNameAsync(string name);
}