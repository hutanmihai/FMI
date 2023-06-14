using Microsoft.OpenApi.Models;
using SissaCoffee.Helpers.Attributes;
using Swashbuckle.AspNetCore.SwaggerGen;

namespace SissaCoffee.Helpers.SwaggerConfig;

public class AuthorizationOperationFilter : IOperationFilter
{
    public void Apply(OpenApiOperation operation, OperationFilterContext context)
    {
        var hasAuthorize = context.MethodInfo.DeclaringType != null && (context.MethodInfo.DeclaringType.GetCustomAttributes(true).OfType<AuthorizationAttribute>().Any() || 
                                                                        context.MethodInfo.GetCustomAttributes(true).OfType<AuthorizationAttribute>().Any());
        if (hasAuthorize)
        {
            operation.Security = new List<OpenApiSecurityRequirement>
            {
                new OpenApiSecurityRequirement
                {
                    {
                        new OpenApiSecurityScheme
                        {
                            Reference = new OpenApiReference
                            {
                                Type = ReferenceType.SecurityScheme,
                                Id = "Authorization"
                            },
                            Scheme = "oauth2",
                            Name = "Authorization",
                            In = ParameterLocation.Header,
                        },
                        new List<string>()
                    }
                }
            };
        }
    }
}
