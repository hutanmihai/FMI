package main.java.laboratoare.laborator7.enums;

/**
 * @author cvoinea
 */
public class Order {

    private final Product product;
    private final Status status;

    public Order(Product product, Status status) {
        this.product = product;
        this.status = status;
    }

    public Product getProduct() {
        return product;
    }

    public Status getStatus() {
        return status;
    }

    @Override
    public String toString() {
        return "Order{" +
                "product=" + product +
                ", status=" + status +
                '}';
    }
}
