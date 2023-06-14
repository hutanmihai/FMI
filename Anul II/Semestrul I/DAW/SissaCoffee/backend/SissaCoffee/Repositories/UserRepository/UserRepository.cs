using SissaCoffee.Data;
using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;
using Microsoft.EntityFrameworkCore;

namespace SissaCoffee.Repositories.UserRepository;

public class UserRepository : GenericRepository<ApplicationUser>, IUserRepository
{
    public UserRepository(AppDbContext context) : base(context)
    {
    }
    
    public async Task<ApplicationUser?> GetUserByIdWithRolesAsync(Guid id)
    {
        return await _table
            .Include(u => u.Roles)
            .FirstOrDefaultAsync(u => u.Id == id);
    }

    public async Task<List<ApplicationUser>> GetUsersWithRolesAsync()
    {
        return await _table
            .Include(u => u.Roles)
            .ToListAsync();
    }
}
