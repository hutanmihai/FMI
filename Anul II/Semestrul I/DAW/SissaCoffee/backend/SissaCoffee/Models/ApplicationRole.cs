using Microsoft.AspNetCore.Identity;

namespace SissaCoffee.Models;

public class ApplicationRole : IdentityRole<Guid>
{ 
    public ICollection<ApplicationUser> Users { get; set; } = new List<ApplicationUser>();
}