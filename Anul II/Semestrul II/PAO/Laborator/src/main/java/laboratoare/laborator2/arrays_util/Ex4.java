package main.java.laboratoare.laborator2.arrays_util;

import java.util.Arrays;
import java.util.List;

/**
 * @author cvoinea
 *
 * use of method asList()
 */
public class Ex4 {

    public static void main(String[] args) {

        // create List of Integers from an array
        List<Integer> intList = Arrays.asList(4, 7, 8, 10);
        System.out.println(intList);

        List<Character> charList = Arrays.asList('j', 'a', 'v', 'a', '8');
        System.out.println(charList);
        // the next line throws an exception: we cannot modify the list because it is backed by the original array
        charList.add('A');
        System.out.println(charList);

    }
}
