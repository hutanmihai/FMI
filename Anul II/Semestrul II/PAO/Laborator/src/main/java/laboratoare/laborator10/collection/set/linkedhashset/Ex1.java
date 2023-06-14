package src.main.java.laboratoare.laborator10.collection.set.linkedhashset;

import java.util.Arrays;
import java.util.HashSet;
import java.util.LinkedHashSet;

/**
 * @author cvoinea
 *
 * similar to HashSet, but it preserves order of insertion
 */
public class Ex1 {

    public static void main(String[] args) {

        LinkedHashSet<Integer> ints = new LinkedHashSet<>(Arrays.asList(1, 3, 5, 6, 8, 9, 323, 12, 434 , 667));
        HashSet<Integer> hashSet = new HashSet<>(ints);

        System.out.println(hashSet);// doesn't preserve order

        for (int i : ints){
            System.out.print(i + " ");
        }
    }
}
