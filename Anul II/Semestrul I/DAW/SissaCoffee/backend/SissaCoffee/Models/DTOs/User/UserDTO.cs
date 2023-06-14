namespace SissaCoffee.Models.DTOs.User;

public class UserDTO
    {
        public Guid Id { get; set; } = Guid.Empty;
        public string Email { get; set; } = String.Empty;
        public string FirstName { get; set; } = String.Empty;
        public string LastName { get; set; } = String.Empty;
        public IList<string> Roles { get; set; } = new List<string>();
    }
