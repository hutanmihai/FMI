using Microsoft.AspNetCore.Identity;
using SissaCoffee.Models;

namespace SissaCoffee.Helpers.Seeders;

public class RoleSeeder
{
    private readonly IConfiguration _configuration;
    private readonly RoleManager<ApplicationRole> _roleManager;

    public RoleSeeder(IConfiguration configuration, RoleManager<ApplicationRole> roleManager)
    {
        _configuration = configuration;
        _roleManager = roleManager;
    }

    public void SeedRoles()
    {
        if (_roleManager is null)
        {
            throw new Exception("Role manager not configured.");
        }
        
        var roles = _configuration.GetSection("Identity:DefaultRoles").Get<List<string>>();
        foreach (var role in roles)
        {
            if (_roleManager.RoleExistsAsync(role).Result) continue;
                         
            var result = _roleManager.CreateAsync(new ApplicationRole { Name = role }).Result;
            if (!result.Succeeded)
            {
                 throw new Exception(string.Join('\n', result.Errors));
            }
        }
    }
}