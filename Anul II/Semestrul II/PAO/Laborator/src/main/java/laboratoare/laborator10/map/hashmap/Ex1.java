package src.main.java.laboratoare.laborator10.map.hashmap;

import java.util.HashMap;
import java.util.Map;

/**
 * @author cvoinea
 *
 * (key, value) pairs
 * part of Collections framework, but doesn't extend Collection interface
 */
public class Ex1 {

    public static void main(String[] args) {

        Map<Integer, Integer> map = new HashMap<>(20); // initial capacity
        for (int i = 1; i <= 10; i++){
            map.put(i, i * i);
        }
        // returns value by key
        System.out.println(map.get(4));
        // removes pair by key and returns value
        System.out.println(map.remove(5));
        // returns boolean for removing the specified pair
        System.out.println(map.remove(2, 2));
        System.out.println(map);

        // returns value and adds pair if key is missing
        System.out.println(map.putIfAbsent(2, 2));
        System.out.println(map);

        // default method
        System.out.println(map.getOrDefault(5, 5555)); // returns default provided if key not found
        System.out.println(map.getOrDefault(9, 999999)); // returns 81 = value for key provided if found
    }
}
