package main.java.laboratoare.laborator1.primitive_types;

/**
 * @author cvoinea
 *
 * single 16-bit Unicode character
 *
 */
public class Char {

    static char defaultChar;

    public static void main(String[] args) {

        System.out.println(Character.MIN_VALUE + 0); // '\u0000' in Unicode, not printable
        System.out.println(Character.MAX_VALUE + 0); // '\uffff' in Unicode
        System.out.println((int)defaultChar); // '\u0000' in Unicode

    }

}
