using Microsoft.AspNetCore.Mvc;
using SissaCoffee.Helpers.Attributes;
using SissaCoffee.Models;
using SissaCoffee.Services.TagService;

namespace SissaCoffee.Controllers;

    [Route("api/tags")]
    [ApiController]
    public class TagController : ControllerBase
    {
        private readonly ITagService _tagService;
        public TagController(ITagService tagService)
        {
            _tagService = tagService;
        }

        [HttpGet]
        [Authorization("Admin")]
        public async Task<ActionResult<IEnumerable<Tag>>> GetIngredients()
        {
            return await _tagService.GetAllTagsAsync();
        }
    }
