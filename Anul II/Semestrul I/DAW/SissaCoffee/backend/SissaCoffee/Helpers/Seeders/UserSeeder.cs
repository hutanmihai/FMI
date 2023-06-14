using Microsoft.AspNetCore.Identity;
using SissaCoffee.Models;

namespace SissaCoffee.Helpers.Seeders;

public class UserSeeder
{
    private readonly UserManager<ApplicationUser> _userManager;

    public UserSeeder(UserManager<ApplicationUser> userManager)
    {
        _userManager = userManager;
    }

    public void SeedUsers()
    {
        if (_userManager is null)
        {
            throw new Exception("User manager not configured.");
        }

        var admins = new List<ApplicationUser>
        {
            new()
            {
                FirstName = "Mihai",
                LastName = "Hutan",
                Email = "hutanmihai29@gmail.com",
                UserName = "hutanmihai29@gmail.com"
            },
            new()
            {
                FirstName = "Cristian",
                LastName = "David",
                Email = "davidcristian@gmail.com",
                UserName = "davidcristian@gmail.com"
            },
        };

        foreach (var admin in admins){
            if (_userManager.FindByEmailAsync(admin.Email).Result == null)
            {
                var result = _userManager.CreateAsync(admin, "admin").Result;
                if (result.Succeeded)
                {
                    _userManager.AddToRoleAsync(admin, "Admin").Wait();
                    _userManager.AddToRoleAsync(admin, "Customer").Wait();
                }
            }
        }
        
        var customers = new List<ApplicationUser>
        {
            new()
            {
                FirstName = "Andrei",
                LastName = "Popescu",
                Email = "andreipopescu@gmail.com",
                UserName = "andreipopescu@gmail.com"
            },
            new()
            {
                FirstName = "Mihai",
                LastName = "Militaru",
                Email = "mihaimilitaru@gmail.com",
                UserName = "mihaimilitaru@gmail.com"
            },
        };
        foreach (var customer in customers){
            if (_userManager.FindByEmailAsync(customer.Email).Result == null)
            {
                var result = _userManager.CreateAsync(customer, "customer").Result;
                if (result.Succeeded)
                {
                    _userManager.AddToRoleAsync(customer, "Customer").Wait();
                }
            }
        }
    }
}