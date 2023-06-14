package src.main.java.laboratoare.laborator10.collection.set.treeset;


import src.main.java.laboratoare.laborator10.collection.set.Person;
import src.main.java.laboratoare.laborator10.collection.set.PersonNameComparator;

import java.util.Arrays;
import java.util.TreeSet;

/**
 * @author cvoinea
 * <p>
 * red-black binary tree that keeps elements sorted
 * add, remove, contains --> O(log2n) complexity
 * good to use when storing many objects sorted by a criteria, they can be returned fast
 */
public class Ex1 {

    public static void main(String[] args) {

        TreeSet<Integer> set1 = new TreeSet<>(Arrays.asList(55, 33, 1, 766, 8, 99));
        System.out.println(set1); // prints elements in natural order

        TreeSet<Person> set2 = new TreeSet<>(new PersonNameComparator());
        set2.add(new Person("Mircea M", 33));
        set2.add(new Person("Adrian S", 30));
        set2.add(new Person("Maria B", 28));
        System.out.println(set2);
    }
}
