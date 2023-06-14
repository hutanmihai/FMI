package src.main.java.laboratoare.laborator10.collection.set.hashset;


import src.main.java.laboratoare.laborator10.collection.set.Person;

import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * @author cvoinea
 * <p>
 * keeps unique elements
 * can add null (only once)
 * unsorted, unordered
 * initial size = 16, doubles its size when loaded at 75% (load factor)
 */
public class Ex1 {

    public static void main(String[] args) {

        Person p1 = new Person("Ana Ionescu", 22);
        Person p2 = new Person("Ana Ionescu", 22);

        Set<Person> people = new HashSet<>(32, 0.8f); // define initial size and load factor
        System.out.println(people.add(p1));
        System.out.println(people.add(p2)); // false if equals() is overridden correctly
        people.add(null);
        System.out.println(people);

        Person p3 = new Person("Paul Ionescu", 22);
        people.add(p3);
        for (Person p : people) { // iterate with enhanced for
            if (p != null) {
                System.out.println(p.getName());
            }
        }

        List<String> strings = Arrays.asList("aaa", "aaa", "aaa", "b", "c");
        Set<String> set = new HashSet<>(strings); // can be built upon other collection
        System.out.println(set);

    }
}
