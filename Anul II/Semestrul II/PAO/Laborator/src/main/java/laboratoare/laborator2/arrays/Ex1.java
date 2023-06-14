package main.java.laboratoare.laborator2.arrays;

/**
 * @author cvoinea
 * <p>
 * an array is a container object
 * it holds a fixed number of values of a single type
 * its length is established at creation time (cannot be modified afterwards)
 * index-based, index starts at 0
 * array data can be retrieved and sorted efficiently
 * size limit is a disadvantage: it's length cannot grow at runtime (collection framework is used to solve this issue)
 * https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html
 */
public class Ex1 {

    public static void main(String[] args) {

        /*
         * declare an array of integer values
         * the declaration doesn't actually create an array object
         * it simply tells the compiler that intArray variable will hold an array of integer values
         */
        int[] intArray;

        // instantiate the array using new operator (allocate memory for 5 integers)
        intArray = new int[5];
        // initialize some elements
        intArray[0] = 123;
        intArray[2] = 11;
        intArray[4] = 0;
        // trying to access an out-of-bounds index will result in a runtime exception
//         intArray[5] = 55; // this line will compile, but will throw an exception at runtime

        // display all the values
        for (int i = 0; i < intArray.length; i++) { // length is a built-in property of arrays
            System.out.println("Element at index " + i + ": " + intArray[i]);
        }

        // can also put the brackets after the name, but language convention discourages this form
        int anotherIntArray[] = new int[10];

        // can declare an array of any other primitive or reference type
        byte[] byteArray;
        short[] shortArray;
        long[] longArray;
        float[] floatArray;
        double[] doubleArray;
        char[] charArray;
        boolean[] booleanArray;
        String[] stringArray = args;
        Object[] objectArray;

    }

}
