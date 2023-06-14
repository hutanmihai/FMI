package models;

import java.util.Objects;

public class Soda extends Product {

    private String brand;
    private String flavor;
    private Double volume;

    public Soda() {
    }

    public Soda(String name, String description, Integer quantity, Double price, String brand, String flavor, Double volume) {
        super(name, description, quantity, price);
        this.brand = brand;
        this.flavor = flavor;
        this.volume = volume;
    }

    public Soda(Integer id, String name, String description, Integer quantity, Double price, String brand, String flavor, Double volume) {
        super(id, name, description, quantity, price);
        this.brand = brand;
        this.flavor = flavor;
        this.volume = volume;
    }

    public String getBrand() {
        return brand;
    }

    public void setBrand(String brand) {
        this.brand = brand;
    }

    public String getFlavor() {
        return flavor;
    }

    public void setFlavor(String flavor) {
        this.flavor = flavor;
    }

    public Double getVolume() {
        return volume;
    }

    public void setVolume(Double volume) {
        this.volume = volume;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Soda soda)) return false;
        if (!super.equals(o)) return false;
        return getBrand().equals(soda.getBrand()) && getFlavor().equals(soda.getFlavor()) && getVolume().equals(soda.getVolume());
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), getBrand(), getFlavor(), getVolume());
    }

    @Override
    public String toString() {
        return
                "Name: " + this.getName() + "\n" +
                        "Description: " + this.getDescription() + "\n" +
                        "Quantity: " + this.getQuantity() + "\n" +
                        "Price: " + this.getPrice() + "\n" +
                        "Brand: " + this.getBrand() + "\n" +
                        "Flavor: " + this.getFlavor() + "\n" +
                        "Volume: " + this.getVolume() + "\n";
    }
}
