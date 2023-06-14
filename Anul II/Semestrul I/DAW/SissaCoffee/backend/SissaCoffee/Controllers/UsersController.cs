using Microsoft.AspNetCore.Mvc;
using SissaCoffee.Helpers.Attributes;
using SissaCoffee.Models;
using SissaCoffee.Models.DTOs.User;
using SissaCoffee.Services.UserService;

namespace SissaCoffee.Controllers;


[Route("api/users/")]
[ApiController]
public class UsersController: ControllerBase
{
    private readonly IUserService _userService;

    public UsersController(IUserService userService)
    {
        _userService = userService;
    }
    
    [HttpGet("me")]
    [Authorization("Customer")]
    public async Task<ActionResult<UserDTO>> GetMe()
    {
        var userId = HttpContext.Items["UserId"]?.ToString();
        if (userId is null)
        {
            return NotFound();
        }

        var user = await _userService.GetUserDtoByIdAsync(new Guid(userId));
        if (user is null)
        {
            return NotFound();
        }

        return Ok(user);
    }

    [HttpGet]
    [Authorization("Admin")]
    public async Task<ActionResult<IEnumerable<UserDTO>>> GetUsers()
    {
        var users = await _userService.GetAllUsersDtoAsync();
        if (users is null)
        {
            return NotFound();
        }

        return Ok(users);
    }

    [HttpGet("{id}")]
    [Authorization("Admin")]
    public async Task<ActionResult<UserDTO>> GetUser(Guid id)
    {
        var user = await _userService.GetUserDtoByIdAsync(id);
        if (user is null)
        {
            return NotFound();
        }

        return Ok(user);
    }

    [HttpPost]
    [Authorization("Admin")]
    public async Task<ActionResult<ApplicationUser>> PostUser([FromBody] UserDTO dto)
    {
        try
        {
            return await _userService.CreateUserAsync(dto);
        }
        catch (Exception e)
        {
            return BadRequest(e.Message);
        }
    }

    [HttpPut("{id}")]
    [Authorization("Admin")]
    public async Task<IActionResult> PutUser(Guid id, UserDTO user)
    {
        try
        {
            await _userService.UpdateUserAsync(id, user);
        }
        catch (Exception e)
        {
            return BadRequest(e.Message);
        }
    
        return NoContent();
    }

    [HttpDelete("{id}")]
    [Authorization("Admin")]
    public async Task<IActionResult> DeleteUser(Guid id)
    {
        try{
            await _userService.DeleteUserAsync(id);
            return Accepted();
        }
        catch (Exception e)
        {
            return BadRequest(e.Message);
        }
    }
}