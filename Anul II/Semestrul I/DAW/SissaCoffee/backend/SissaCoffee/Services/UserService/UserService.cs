using AutoMapper;
using Microsoft.AspNetCore.Identity;
using SissaCoffee.Models;
using SissaCoffee.Models.DTOs.User;
using SissaCoffee.Repositories.RoleRepository;
using SissaCoffee.Repositories.UserRepository;
using SissaCoffee.Helpers.JwtUtils;

namespace SissaCoffee.Services.UserService;

public class UserService: IUserService
{
    private readonly UserManager<ApplicationUser> _userManager;
    private readonly IUserRepository _userRepository;
    private readonly IRoleRepository _roleRepository;
    private readonly IJwtUtils _jwtUtils;
    private readonly IMapper _mapper;

    public UserService(UserManager<ApplicationUser> userManager, IUserRepository userRepository, IRoleRepository roleRepository, IJwtUtils jwtUtils, IMapper mapper)
    {
        _userManager = userManager;
        _userRepository = userRepository;
        _roleRepository = roleRepository;
        _jwtUtils = jwtUtils;
        _mapper = mapper;
    }

    public async Task<IdentityResult> RegisterUserAsync(RegisterUserDTO dto)
    {
        var customerRole = await _roleRepository.GetRoleByNameAsync("Customer");
        if (customerRole is null)
        {
            throw new Exception("Customer role not found.");
        }
        
        var user = new ApplicationUser
        {
            Email = dto.Email,
            UserName = dto.Email,
            FirstName = dto.FirstName,
            LastName = dto.LastName
        };

        var res = await _userManager.CreateAsync(user, dto.Password);

        if (res.Succeeded)
        {
            var secondRes = await _userManager.AddToRoleAsync(user, customerRole.Name);
            if (!secondRes.Succeeded)
            {
                throw new Exception("Failed to add user to role.");
            }
        }

        return res;
    }

    public async Task<string?> LoginUserAsync(LoginUserDTO dto)
    {
        var user = await _userManager.FindByEmailAsync(dto.Email);

        if (user is null) return null;

        if (!await _userManager.CheckPasswordAsync(user, dto.Password)) return null;

        return _jwtUtils.GenerateJwtToken(user);
    }
    
    public async Task<ApplicationUser?> GetUserByEmailAsync(string email)
    {
        return await _userManager.FindByEmailAsync(email);
    }

    public async Task<IEnumerable<UserDTO>?> GetAllUsersDtoAsync()
    {
        var users = await _userRepository.GetUsersWithRolesAsync();
        if (!users.Any()) return null;
        return _mapper.Map<IEnumerable<UserDTO>>(users);
    }

    public async Task<UserDTO?> GetUserDtoByIdAsync(Guid id)
    {
        var user = await _userRepository.GetUserByIdWithRolesAsync(id);
        if (user is null) return null;
        return _mapper.Map<UserDTO>(user);
    }
    
    public async Task<ApplicationUser?> CreateUserAsync(UserDTO userDto)
    {
        var userFound = await _userManager.FindByEmailAsync(userDto.Email);
        if (userFound is not null) throw new Exception("User already exists.");
        var userDtoRoles = new List<ApplicationRole>();
        foreach (var userDtoRole in userDto.Roles)
        {
            var role = await _roleRepository.GetRoleByNameAsync(userDtoRole);
            if (role is null) throw new Exception("Role not found.");
            userDtoRoles.Add(role);
        }
        var user = new ApplicationUser
        {
            Email = userDto.Email,
            UserName = userDto.Email,
            FirstName = userDto.FirstName,
            LastName = userDto.LastName,
            Roles = userDtoRoles
        };
        var res = await _userManager.CreateAsync(user);
        if (!res.Succeeded) throw new Exception(res.Errors.First().Description);
        return user;
    }
    
    public async Task UpdateUserAsync(Guid id, UserDTO userDto)
    {
        if (id != userDto.Id) throw new Exception("Id mismatch.");
        
        var user = await _userManager.FindByIdAsync(id.ToString());
        if (user is null) throw new Exception("User not found.");
        
        var userDtoRoles = new List<ApplicationRole>();
        foreach (var userDtoRole in userDto.Roles)
        {
            var role = await _roleRepository.GetRoleByNameAsync(userDtoRole);
            if (role is null) throw new Exception("Role not found.");
            userDtoRoles.Add(role);
        }
        
        user.FirstName = userDto.FirstName;
        user.LastName = userDto.LastName;
        user.Email = userDto.Email;
        user.UserName = userDto.Email;
        foreach (var userDtoRole in userDtoRoles)
        {
            if (!await _userManager.IsInRoleAsync(user, userDtoRole.Name))
            {
                await _userManager.AddToRoleAsync(user, userDtoRole.Name);
            }
        }
        try
        {
            await _userManager.UpdateAsync(user);
        }
        catch (Exception e)
        {
            throw new Exception(e.Message);
        }
    }

    public async Task DeleteUserAsync(Guid id)
    {
        try
        {
            var userFound = await _userManager.FindByIdAsync(id.ToString());
            if (userFound is null) throw new Exception("User not found.");
            await _userManager.DeleteAsync(userFound);
        }
        catch (Exception e)
        {
            throw new Exception(e.Message);
        }
    }
}