using Microsoft.AspNetCore.Identity;

namespace SissaCoffee.Models;

public class ApplicationUser: IdentityUser<Guid>
{
    public string FirstName { get; set; } = String.Empty;
    public string LastName { get; set; } = String.Empty;

    public ICollection<ApplicationRole> Roles { get; set; } = new List<ApplicationRole>();
}