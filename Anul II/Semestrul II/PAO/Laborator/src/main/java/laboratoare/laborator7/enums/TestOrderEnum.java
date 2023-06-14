package main.java.laboratoare.laborator7.enums;

import static main.java.laboratoare.laborator7.enums.StatusEnum.RECEIVED;

/**
 * @author cvoinea
 */
public class TestOrderEnum {

    public static void main(String[] args) {

        Product p1 = new Product("p1", 1);
        OrderWithEnum o1 = new OrderWithEnum(p1, RECEIVED);

        System.out.println(o1.getStatus().name());
        System.out.println(o1.getStatus().ordinal());

        System.out.println(o1);
        System.out.println(o1.getStatus().estimateDeliveryTime());

        // values()
        for (StatusEnum status : StatusEnum.values()) {
            System.out.println(status);
        }

        System.out.println(StatusEnum.fromValue("abc")); // null
        System.out.println(StatusEnum.fromValue("  ProceSSing  ")); // PROCESSING

    }
}
