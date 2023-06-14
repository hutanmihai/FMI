using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.TagRepository;

public interface ITagRepository: IGenericRepository<Tag>
{
    public Tag? FindByName(string name);
    public Task<Tag?> GetByIdAsync(Guid? id);
}