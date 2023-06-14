package main.java.laboratoare.laborator7.enums;

/**
 * @author cvoinea
 */
public class TestOrder {

    private static final String PROCESSING_STATUS = "processing";
    private static final String COMPLETE_STATUS = "complete";
    private static final String RECEIVED_STATUS = "received";

    public static void main(String[] args) {

        Product p1 = new Product("p1", 1);
        Status s1 = new Status("processing");
        Order o1 = new Order(p1, s1);

        System.out.printf("Estimated delivery time for order %s: \n %s ",
                o1, estimateDeliveryTime(o1.getStatus().getOrderStatus()));

    }

    public static int estimateDeliveryTime(String currentStatus) {
        if (currentStatus.equalsIgnoreCase(RECEIVED_STATUS)) {
            return 3;
        } else if (currentStatus.equalsIgnoreCase(PROCESSING_STATUS)) {
            return 1;
        } else if (currentStatus.equalsIgnoreCase(COMPLETE_STATUS)) {
            return 0;
        } else {
            return -1;
        }
    }
}
