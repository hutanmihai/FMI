package main.java.laboratoare.laborator2.arrays_util;

import java.util.Arrays;

/**
 * @author cvoinea
 *
 * use of methods fill(), toString(), deepToString(), equals(), deepEquals(), hashCode(), deepHashCode()
 */
public class Ex2 {

    public static void main(String[] args) {

        // use Arrays.fill() method to initialize array elements
        int[][] array = new int[5][5];
        for (int[] row : array) {
            Arrays.fill(row, 3);
            System.out.println(Arrays.toString(row));
        }

        // compare a multidimensional array with its copy
        int[][] copyArray = array.clone();
        // equals and deepEquals
        System.out.println(Arrays.equals(array, copyArray));
        System.out.println(Arrays.deepEquals(array, copyArray)); //deepEquals works only with Object[] as args

        // pretty-print multidimensional arrays
        System.out.println(Arrays.toString(copyArray));
        // use Arrays.deepToString() to print String representation of embedded objects
        System.out.println(Arrays.deepToString(copyArray));

        // hashcode and deepHashCode
        System.out.println(Arrays.hashCode(copyArray));
        System.out.println(Arrays.deepHashCode(copyArray));

    }
}
