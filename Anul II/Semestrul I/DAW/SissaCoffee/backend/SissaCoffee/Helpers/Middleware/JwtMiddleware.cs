using Microsoft.AspNetCore.Identity;
using SissaCoffee.Helpers.JwtUtils;
using SissaCoffee.Models;

namespace SissaCoffee.Helpers.Middleware
{
    public class JwtMiddleware
    {
        private readonly RequestDelegate _next;

        public JwtMiddleware(RequestDelegate next)
        {
            _next = next;
        }

        public async Task Invoke(HttpContext httpContext, IJwtUtils jwtUtils, UserManager<ApplicationUser> userManager)
        {
            string authHeader = httpContext.Request.Headers["Authorization"].ToString();
            var token = authHeader.Split(" ").Last();
            
            var userId = jwtUtils.ValidateJwtToken(token);

            httpContext.Items["UserId"] = userId.ToString();

            if(userId != Guid.Empty)
            {
                var user = await userManager.FindByIdAsync(userId.ToString());
                if (user != null)
                {
                    var roles = await userManager.GetRolesAsync(user);
                    httpContext.Items["Roles"] = roles;
                }
            }

            await _next(httpContext);
        }
    }
}
