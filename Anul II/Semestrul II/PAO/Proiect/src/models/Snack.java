package models;

import java.util.Objects;

public class Snack extends Product {

    private String type;
    private String size;

    public Snack() {
    }

    public Snack(String name, String description, Integer quantity, Double price, String type, String size) {
        super(name, description, quantity, price);
        this.type = type;
        this.size = size;
    }

    public Snack(Integer id, String name, String description, Integer quantity, Double price, String type, String size) {
        super(id, name, description, quantity, price);
        this.type = type;
        this.size = size;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Snack snack)) return false;
        if (!super.equals(o)) return false;
        return getType().equals(snack.getType()) && getSize().equals(snack.getSize());
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), getType(), getSize());
    }

    @Override
    public String toString() {
        return
                "Name: " + this.getName() + "\n" +
                        "Description: " + this.getDescription() + "\n" +
                        "Quantity: " + this.getQuantity() + "\n" +
                        "Price: " + this.getPrice() + "\n" +
                        "Type: " + this.getType() + "\n" +
                        "Size: " + this.getSize() + "\n";
    }
}
