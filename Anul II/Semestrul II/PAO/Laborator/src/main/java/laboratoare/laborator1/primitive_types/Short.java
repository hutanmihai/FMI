package main.java.laboratoare.laborator1.primitive_types;

/**
 * @author cvoinea
 *
 * short --> 16-bit integer values
 */
public class Short {

    static short defaultShort;

    public static void main(String[] args) {

        short s1 = -32_768;
        System.out.println(s1);

        short s2 = 32_767;
        System.out.println(++s2);

        System.out.println(defaultShort);

    }
}
