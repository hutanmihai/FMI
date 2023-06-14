using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.Filters;

namespace SissaCoffee.Helpers.Attributes
{
    public class AuthorizationAttribute : Attribute, IAuthorizationFilter
    {
        private readonly IList<string> _roles;

        public AuthorizationAttribute(params string[] roles)
        {
            _roles = roles;
        }

        public void OnAuthorization(AuthorizationFilterContext context)
        {
            var unauthorizedStatusObject = new JsonResult(new { Message = "Unauthorized" })
                { StatusCode = StatusCodes.Status401Unauthorized };

            if (_roles.Count == 0)
            {
                context.Result = unauthorizedStatusObject;
                return;
            }

            if (!context.HttpContext.Items.TryGetValue("Roles", out var actualRoles) || !(actualRoles is IList<string> actualRolesList))
            {
                context.Result = new JsonResult(new { Message = "Unauthorized"})
                    { StatusCode = StatusCodes.Status401Unauthorized };
                return;
            }

            int count = 0;
            foreach (var role in _roles)
            {
                if (actualRolesList.Contains(role))
                {
                    count++;
                }
            }

            if (count == 0)
            {
                context.Result = unauthorizedStatusObject;
            }
        }
    }
}
