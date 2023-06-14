package main.java.laboratoare.laborator7.enums;

/**
 * @author cvoinea
 */
public class Status {

    private String orderStatus;

    public Status(String orderStatus) {
        this.orderStatus = orderStatus;
    }

    public String getOrderStatus() {
        return orderStatus;
    }

    public void setOrderStatus(String orderStatus) {
        this.orderStatus = orderStatus;
    }

    @Override
    public String toString() {
        return "Status{" +
                "orderStatus='" + orderStatus + '\'' +
                '}';
    }
}
