using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.RoleRepository;

public interface IRoleRepository: IGenericRepository<ApplicationRole>
{
    public Task<ApplicationRole?> GetRoleByNameAsync(string name);
}