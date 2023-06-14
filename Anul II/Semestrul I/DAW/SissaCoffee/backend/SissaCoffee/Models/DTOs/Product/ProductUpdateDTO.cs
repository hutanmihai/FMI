namespace SissaCoffee.Models.DTOs.Product
{
    public class ProductUpdateDTO
    {
        public string Name { get; set; }
        public List<Guid> Ingredients { get; set; }
        public Guid Variant { get; set; }
        public Guid? Tag { get; set; }
    }
}