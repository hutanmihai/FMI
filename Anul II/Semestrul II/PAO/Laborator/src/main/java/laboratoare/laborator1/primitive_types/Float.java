package main.java.laboratoare.laborator1.primitive_types;

/**
 * @author cvoinea
 *
 * single-precision 32-bit IEEE 754 floating point
 *
 */
public class Float {

    static float defaultFloat;

    public static void main(String[] args) {

        float f1 = 12345; // can assign an int to a float
        System.out.println(f1);

//        float f2 = 123.45; // cannot use floating point value without F or f suffix (literal value defaults to double)

        float f3 = 12345.67f;
        System.out.println(f3);

        System.out.println(defaultFloat);
    }
}
