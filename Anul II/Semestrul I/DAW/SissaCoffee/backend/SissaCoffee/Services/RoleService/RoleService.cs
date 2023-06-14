using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using SissaCoffee.Models;
using SissaCoffee.Repositories.RoleRepository;

namespace SissaCoffee.Services.RoleService;

public class RoleService : IRoleService
{
    private readonly RoleManager<ApplicationRole> _roleManager;
    private readonly IRoleRepository _roleRepository;
    
    public RoleService(RoleManager<ApplicationRole> roleManager, IRoleRepository roleRepository)
    {
        _roleManager = roleManager;
        _roleRepository = roleRepository;
    }

    public async Task<List<ApplicationRole>> GetAllRolesAsync()
    {
        return await _roleManager.Roles.ToListAsync();
    }

    public async Task<ApplicationRole?> GetRoleByNameAsync(string name)
    {
        return await _roleRepository.GetRoleByNameAsync(name);
    }
}