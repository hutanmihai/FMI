using SissaCoffee.Models;
using SissaCoffee.Repositories.TagRepository;

namespace SissaCoffee.Services.TagService;

public class TagService: ITagService
{
    private readonly ITagRepository _tagRepository;
    public TagService(ITagRepository tagRepository)
    {
        _tagRepository = tagRepository;
    }
    
    public async Task<List<Tag>> GetAllTagsAsync()
    {
        return await _tagRepository.GetAllAsync();
    }
}