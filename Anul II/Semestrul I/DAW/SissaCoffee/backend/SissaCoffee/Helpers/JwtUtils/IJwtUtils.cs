using SissaCoffee.Models;

namespace SissaCoffee.Helpers.JwtUtils
{
    public interface IJwtUtils
    {
        public string GenerateJwtToken(ApplicationUser user);
        public Guid ValidateJwtToken(string? token);
    }
}
