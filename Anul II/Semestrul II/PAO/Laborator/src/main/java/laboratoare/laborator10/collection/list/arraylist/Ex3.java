package src.main.java.laboratoare.laborator10.collection.list.arraylist;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

/**
 * @author cvoinea
 */
public class Ex3 {

    public static void main(String[] args) {

        // convert an array to a list
        List<String> list = Arrays.asList("def", "ade", "a", "f", "ef", "e5");

        //toArray without array param returns an Object[]
        Object[] array = list.toArray();

        String[] strings = new String[10];
        // toArray with array param puts the values in that array and returns it
        System.out.println(Arrays.toString(list.toArray(strings)));

        // use static methods from Collections class to perform different ops on collections
        Collections.sort(list);
        System.out.println(list);

        Collections.shuffle(list);
        System.out.println(list);

        System.out.println(Collections.binarySearch(list, "f"));
        System.out.println(Collections.binarySearch(list, "ff")); // if not found => -(insertionPoint + 1)
    }
}
