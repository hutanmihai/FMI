package src.main.java.laboratoare.laborator10.map.treemap;


import src.main.java.laboratoare.laborator10.map.hashmap.Ex2;

import java.util.Map;
import java.util.TreeMap;

/**
 * @author cvoinea
 *
 * implementation which uses a red-black binary tree to sort the keys
 *
 * solve the same exercise to display the words used in a given text, together with their number of appearances,
 * but also sort the words ascending
 */
public class Ex1 {

    public static void main(String[] args) {

        Map<String, Integer> hashMap = Ex2.createMap();
        TreeMap<String, Integer> treeMap = new TreeMap<>(hashMap);
        System.out.println(treeMap);


        System.out.println(new TreeMap<>(Ex2.createMap()));

    }
}
