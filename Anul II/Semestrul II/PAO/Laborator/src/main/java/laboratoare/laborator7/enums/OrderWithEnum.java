package main.java.laboratoare.laborator7.enums;

/**
 * @author cvoinea
 */
public class OrderWithEnum {

    private final Product product;
    private final StatusEnum status;

    public OrderWithEnum(Product product, StatusEnum status) {
        this.product = product;
        this.status = status;
    }

    public Product getProduct() {
        return product;
    }

    public StatusEnum getStatus() {
        return status;
    }

    @Override
    public String toString() {
        return "OrderWithEnum{" +
                "product=" + product +
                ", status=" + status +
                '}';
    }
}
