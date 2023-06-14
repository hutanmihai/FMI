package main.java.laboratoare.laborator1.primitive_types;

/**
 * @author cvoinea
 *
 * double-precision 64-bit IEEE 754 floating point
 *
 */
public class Double {

    static double defaultDouble;

    public static void main(String[] args) {

        double d1 = 555; // int literal
        System.out.println(d1);

        double d2 = 123_456_789_000L; // long literal
        System.out.println(d2);

        double d3 = 123.4f; // float literal
        System.out.println(d3);

        double d4 = 12345.6d; // double literal, D or d is optional
        System.out.println(d4);

        double d5 = 1.23456e4D; // same value as d4, in scientific notation
        System.out.println(d5);

        System.out.println(defaultDouble);
    }

}
