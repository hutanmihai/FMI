using Microsoft.IdentityModel.Tokens;
using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using SissaCoffee.Models;

namespace SissaCoffee.Helpers.JwtUtils
{
    public class JwtUtils: IJwtUtils
    {

        private readonly IConfiguration _configuration;
        
        public JwtUtils(IConfiguration configuration)
        {
            _configuration = configuration;
        }

        public string GenerateJwtToken(ApplicationUser user)
        {
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Subject = new ClaimsIdentity(new []
                {
                    new Claim("UserId", user.Id.ToString())
                }),
                Expires = DateTime.UtcNow.AddDays(10),
                SigningCredentials = new SigningCredentials(new SymmetricSecurityKey(Encoding.UTF8
                        .GetBytes(_configuration["Jwt:Secret"] ?? "SecretKey")),
                    SecurityAlgorithms.HmacSha256Signature)
            };

            var tokenHandler = new JwtSecurityTokenHandler();
            var securityToken = tokenHandler.CreateToken(tokenDescriptor);
            return tokenHandler.WriteToken(securityToken);
        }

        public Guid ValidateJwtToken(string? token)
        {
            if(token == null)
            {
                 return Guid.Empty;
            }

            var tokenHandler = new JwtSecurityTokenHandler();
            var appPrivateKey = Encoding.UTF8.GetBytes(_configuration["Jwt:Secret"] ?? "SecretKey");

            var tokenValidationParameters = new TokenValidationParameters
            { 
                ValidateIssuerSigningKey = true, 
                IssuerSigningKey = new SymmetricSecurityKey(appPrivateKey), 
                ValidateIssuer = false, 
                ValidateAudience = false, 
                ClockSkew = TimeSpan.Zero,
            };

            try
            { 
                tokenHandler.ValidateToken(token, tokenValidationParameters, out SecurityToken validatedToken);
               
                var jwtToken = (JwtSecurityToken)validatedToken; 
                var userId = new Guid(jwtToken.Claims.FirstOrDefault(x => x.Type == "UserId")?.Value ?? Guid.Empty.ToString());

                if (userId == Guid.Empty)
                {
                    return Guid.Empty;
                }
               
                return userId;
            }
            catch
            { 
                return Guid.Empty;
            }
        }
    }
}
