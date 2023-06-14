using SissaCoffee.Models;
using SissaCoffee.Repositories.TagRepository;

namespace SissaCoffee.Helpers.Seeders;

public class TagSeeder
{
    private readonly ITagRepository _tagRepository;
    
    public TagSeeder(ITagRepository tagRepository)
    {
        _tagRepository = tagRepository;
    }

    public void SeedTags()
    {
        var tags = new List<Tag>()
        {
            new()
            {
                Name = "BestSeller",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "New",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Recommendation",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            },
            new()
            {
                Name = "Favorite",
                CreatedAt = DateTime.UtcNow,
                UpdatedAt = DateTime.UtcNow
            }
        };

        foreach (var tag in tags)
        {
            if (_tagRepository.FindByName(tag.Name) is null)
            {
                _tagRepository.Create(tag);
            }
        }
    }
}