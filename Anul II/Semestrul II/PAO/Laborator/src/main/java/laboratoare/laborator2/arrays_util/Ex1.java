package main.java.laboratoare.laborator2.arrays_util;

import java.util.Arrays;

/**
 * @author cvoinea
 *
 * https://docs.oracle.com/javase/7/docs/api/java/util/Arrays.html
 *
 */
public class Ex1 {

    public static void main(String[] args) {

        // copy elements of an array using arrayCopy() method in System class
        char[] source = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'};
        char[] destination = new char[5];

        System.arraycopy(source, 3, destination, 0, 4);
        System.out.println(String.valueOf(destination));

        // perform copy using Arrays.copyOf()
        char[] anotherCopy = Arrays.copyOf(source, 4);
        // using Arrays.toString() method to print the array
        System.out.println(Arrays.toString(anotherCopy));

        // using Arrays.copyOfRange() method
        int[] ints = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}; // 10 elements
        // pay attention that 'to' index specified as 3rd argument is exclusive: [from, to-1 ] or [from, to)
        System.out.println(Arrays.toString(Arrays.copyOfRange(ints, 0, 10))); // actual interval is [0, 9] or [0, 10)
        System.out.println(Arrays.toString(Arrays.copyOfRange(ints, 4, 4)));
        // next line will throw an exception since 'from' index must be <= 'to' index
        System.out.println(Arrays.toString(Arrays.copyOfRange(ints, 4, 3)));

    }
}
