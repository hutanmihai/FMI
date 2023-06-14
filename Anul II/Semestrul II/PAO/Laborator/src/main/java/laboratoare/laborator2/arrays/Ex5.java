package main.java.laboratoare.laborator2.arrays;

/**
 * @author cvoinea
 * <p>
 * copy and clone operations on arrays
 */
public class Ex5 {

    public static void main(String[] args) {

        // copy elements of an array using arrayCopy() method in System class
        char[] source = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'};
        char[] destination = new char[5];

        System.arraycopy(source, 3, destination, 0, 4);
        System.out.println(String.valueOf(destination));

        // on single-dimensional arrays, clone() method copies the values as expected
        int[] ints = {22, 33, 44, 55, 66};
        int[] clone = ints.clone();
        for (int i : clone) {
            System.out.print(i + " ");
        }

        System.out.println();
        System.out.println(ints);
        System.out.println(clone);
        System.out.println(ints == clone);


        byte[][] bytes = new byte[3][];
        bytes[0] = new byte[]{1, 0};
        bytes[1] = new byte[]{};
        bytes[2] = new byte[]{1, 1, 1, 1, 1, 1};

        // cloning multidimensional arrays only copies the references of array elements (shallow copy)
        byte[][] cloneOfBytes = bytes.clone();
        // this will print true since we compare two byte values
        System.out.println(bytes[0][0] == cloneOfBytes[0][0]);

        // will print true since both values are references to the same array in memory
        System.out.println(bytes[0] == cloneOfBytes[0]);
        // same address in memory
        System.out.println(bytes[0]);
        System.out.println(cloneOfBytes[0]);
    }
}
