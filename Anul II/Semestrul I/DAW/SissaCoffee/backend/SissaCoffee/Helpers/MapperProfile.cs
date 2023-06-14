using AutoMapper;
using SissaCoffee.Models;
using SissaCoffee.Models.DTOs.Product;
using SissaCoffee.Models.DTOs.User;

namespace SissaCoffee.Helpers
{
    public class MapperProfile: Profile
    {
        public MapperProfile()
        {
            CreateMap<ApplicationUser, LoginUserDTO>();
            CreateMap<ApplicationUser, RegisterUserDTO>();
            CreateMap<ApplicationUser, UserDTO>().ForMember(
                dest => dest.Roles,
                opt => opt.MapFrom(src => src.Roles.Select(x=>x.Name).ToList())
            );
            CreateMap<Product, ProductDTO>().ForMember(
                dest => dest.Ingredients,
                opt => opt.MapFrom(src => src.Ingredients.Select(x=>x.Ingredient.Name).ToList())
            ).ForMember(
                dest => dest.Tag,
                opt => opt.MapFrom(src => src.Tag.Name))
                .ForMember(
                    dest => dest.Variant,
                    opt => opt.MapFrom(src => new ProductVariantDTO(){Name = src.Variant.Name, Size = src.Variant.Size, Unit = src.Variant.Unit}));
        }
    }
}
