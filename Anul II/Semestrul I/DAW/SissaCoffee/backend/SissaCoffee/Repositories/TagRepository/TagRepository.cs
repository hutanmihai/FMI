using Microsoft.EntityFrameworkCore;
using SissaCoffee.Data;
using SissaCoffee.Models;
using SissaCoffee.Repositories.GenericRepository;

namespace SissaCoffee.Repositories.TagRepository;

public class TagRepository: GenericRepository<Tag>, ITagRepository
{
    public TagRepository(AppDbContext context) : base(context)
    {
    }
    
    public Tag? FindByName(string name)
    {
        return _table.FirstOrDefault(e => e.Name == name);
    }
    
    public async Task<Tag?> GetByIdAsync(Guid? id)
    {
        if (id == null)
        {
            return null;
        }
        var tag = await _table.FirstOrDefaultAsync(e => e.Id == id);
        if (tag == null)
        {
            throw new Exception("Tag not found");
        }

        return tag;
    }
}