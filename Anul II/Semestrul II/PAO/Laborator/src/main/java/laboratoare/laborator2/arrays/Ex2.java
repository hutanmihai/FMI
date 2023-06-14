package main.java.laboratoare.laborator2.arrays;

import java.util.Arrays;

/**
 * @author cvoinea
 * <p>
 * shortcut syntax to create an array
 */
public class Ex2 {

    public static void main(String[] args) {

        // shortcut syntax to instantiate and initialize an array
        char[] chars = {'j', 'a', 'v', 'a'}; // length is determined by the no of values provided between braces - here: 4
        // use for-each loop to cycle through elements
        for (char c : chars) {
            System.out.println(c);
        }
        System.out.println(new String(chars));

        // can also use this syntax
        byte[] bytes = new byte[]{0, 4, 6, -128};
        System.out.println(bytes); // will print something like [B@hash_code since arrays don't implement toString()
        System.out.println(int[].class);
        System.out.println(Arrays.toString(bytes)); // utility class Arrays contains various methods for manipulating arrays

        // array length here will be 0 (cannot be changed after creation)
        int[] intArray = {};
        // exception at runtime while trying to access an out-of-bounds element
        intArray[0] = 0;
        System.out.println(intArray[0]);

    }
}
