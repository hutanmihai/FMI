package main.java.laboratoare.laborator2.arrays_util;

import java.util.Arrays;
import java.util.Comparator;

/**
 * @author cvoinea
 *
 * use of methods sort(), binarySearch()
 */
public class Ex3 {

    public static void main(String[] args) {

        System.out.println("Sorting and searching int[]: ");
        int[] ints = {2, 6, 1, 8, 3, 9, 0, -7, 4};
        // sort()
        System.out.println(Arrays.binarySearch(ints, 0));
        Arrays.sort(ints);
        System.out.println(Arrays.toString(ints));
        // binarySearch() only works with sorted arrays
        System.out.println(Arrays.binarySearch(ints, 0)); // when key is found, it's index is returned
        // when key not found, value returned is ((-insertionPoint) -1)
        System.out.println(Arrays.binarySearch(ints, 5));

        System.out.println("Sorting and searching char[]: ");
        char[] chars = {'f', '3', 'z', '+', 'j', 'a', 'A', 'f', 'F'};
        // sort() from [index to index)
        Arrays.sort(chars, 5, 9);
        System.out.println(String.valueOf(chars));
        System.out.println(Arrays.binarySearch(chars, 'j'));
        System.out.println(Arrays.binarySearch(chars, '+'));
        Arrays.sort(chars);
        System.out.println(Arrays.binarySearch(chars, '+'));

        System.out.println("Sorting and searching String[]: ");
        String[] names = {"Jon", "Danielle", "Marie", "Paul", "Jo"};
        System.out.println(Arrays.binarySearch(names, "Jo"));
        // natural sorting (alphabetically for Strings)
        Arrays.sort(names);
        System.out.println(Arrays.deepToString(names));
        System.out.println(Arrays.binarySearch(names, "Jo"));
        // sort the array ascending by String elements length
        Arrays.sort(names, Comparator.comparingInt(String::length));
        System.out.println(Arrays.deepToString(names));
        System.out.println(Arrays.binarySearch(names, "Jo"));

    }
}
