using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using SissaCoffee.Models.DTOs.User;
using SissaCoffee.Services.UserService;

namespace SissaCoffee.Controllers
{
    [Route("api/auth/")]
    [ApiController]
    public class AccountsController : ControllerBase
    {
        private readonly IUserService _userService;

        public AccountsController(IUserService userService)
        {
            _userService = userService;
        }

        [HttpPost("register")]
        [AllowAnonymous]
        public async Task<IActionResult> Register([FromBody] RegisterUserDTO dto)
        {
            var user = await _userService.GetUserByEmailAsync(dto.Email);

            if (user is not null)
            {
                return BadRequest("The user already exists!");
            }

            var result = await _userService.RegisterUserAsync(dto);

            if (result.Succeeded)
            {
                return Ok(result);
            }

            return BadRequest(result.Errors.ToList());
        }

        [HttpPost("login")]
        [AllowAnonymous]
        public async Task<IActionResult> Login([FromBody] LoginUserDTO dto)
        {
            var token = await _userService.LoginUserAsync(dto);

            if (token is null)
            {
                return Unauthorized();
            }

            return Ok(token);
        }
    }
}