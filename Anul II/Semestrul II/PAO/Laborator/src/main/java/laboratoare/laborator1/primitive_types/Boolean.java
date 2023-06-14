package main.java.laboratoare.laborator1.primitive_types;

/**
 * @author cvoinea
 *
 * data type for simple flags that track true/ false conditions
 * represents one bit of information, but its "size" is not precisely defined (VM dependant)
 * at VM level, a boolean occupies the same amount of space as an int, meaning one stack cell:
 *                  at least 4 bytes, typically 4 bytes on 32-bit Java and 8 bytes on 64-bit.
 *
 */
public class Boolean {

    static boolean defaultBoolean;

    public static void main(String[] args) {

        boolean b1 = true;
        System.out.println(b1);

        boolean b2 = false;
        System.out.println(b2);

        boolean b3 = 'A' == 65;
        System.out.println(b3);

        System.out.println(defaultBoolean);
    }


}
