using Microsoft.EntityFrameworkCore;
using SissaCoffee.Data;
using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.RoleRepository;

public class RoleRepository: GenericRepository<ApplicationRole>, IRoleRepository
{
    public RoleRepository(AppDbContext context) : base(context)
    {
    }

    public async Task<ApplicationRole?> GetRoleByNameAsync(string name)
    {
        return await _context.ApplicationRoles.FirstOrDefaultAsync(r => r.Name == name);
    }
}