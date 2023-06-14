package src.main.java.laboratoare.laborator10.collection.list.arraylist;

import java.util.ArrayList;
import java.util.List;

/**
 * @author cvoinea
 */
public class Ex2 {

    public static void main(String[] args) {

        //constructor with initial capacity of underlying array
        ArrayList<Integer> ints = new ArrayList<>(20); // implicit is 10
        ints.add(1);
        ints.add(3);
        ints.add(5);
        ints.add(7);

        //replaces value at index, returns value
        ints.set(2, 10);

        // returns element by index
        System.out.println(ints.get(0));
        System.out.println(ints);
        ints.addAll(ints);
        System.out.println(ints);

        //first occurrence
        System.out.println(ints.indexOf(3));

        // last occurrence
        System.out.println(ints.lastIndexOf(3));

        // get a sublist between [2, 4), backed by the initial list
        List<Integer> sublist = ints.subList(2, 4);
        System.out.println("sublist: " + sublist);
        // box the int value to wrapper class in order to use the method with this signature: boolean remove(Object o)
        ints.remove(Integer.valueOf(10));
        System.out.println(ints);
        //throws java.util.ConcurrentModificationException
//        System.out.println(sublist); // cannot use sublist after modifying initial list
    }
}
