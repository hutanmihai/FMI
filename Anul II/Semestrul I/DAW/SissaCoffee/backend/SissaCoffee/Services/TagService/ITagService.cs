using SissaCoffee.Models;

namespace SissaCoffee.Services.TagService;

public interface ITagService
{
    public Task<List<Tag>> GetAllTagsAsync();
}