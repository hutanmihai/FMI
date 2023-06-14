using SissaCoffee.Models.Base;

namespace SissaCoffee.Models;

public class Tag: BaseEntity
{
    public string Name { get; set; } = String.Empty;
    
    public Product? Product { get; set; }
}