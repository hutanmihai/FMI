package main.java.laboratoare.laborator1.primitive_types;

/**
 * @author cvoinea
 *
 * long --> 64-bit integer value
 *
 */
public class Long {

    public static void main(String[] args) {

        long l1 = 1223343534;
        long l2 = 1223343534;  // if the literal ends with "L" or "l", it's a long, otherwise int
        System.out.println("l1 = " + l1);
        System.out.println("l2 = " + l2);
        long l3, l4;
        System.out.println(l3 = l4 = -0b1010101101010L);

    }
}
