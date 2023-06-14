package main.java.laboratoare.laborator1.primitive_types;

/**
 * @author cvoinea
 *
 * int --> 32-bit integer value
 */
public class Int {

    static int defaultInt;

    public static void main(String[] args) {

        int i1 = 68_709_809; // underscore chars in numeric literals available since Java 7
        System.out.println("i1 = " + i1);

        System.out.println("min value for int: " + Integer.MIN_VALUE);
        System.out.println("max value for int: " + Integer.MAX_VALUE);

        int i2 = 0b0101_0_101_010101010; //binary
        System.out.println("i2 = " + i2);

        int i4, i3 = 0_167;
        System.out.println("i3 = " + i3); // octal
        System.out.println("i4 = " + (i4 = 0x57_FAE)); // hexadecimal

        System.out.println(defaultInt);
    }
}
