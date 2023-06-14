package src.main.java.laboratoare.laborator11.streams.terminalops;

import java.util.Arrays;
import java.util.List;

/**
 * @author cvoinea
 * terminal operations: forEach, count, min, max, anyMatch, allMatch, noneMatch, findAny, findFirst, reduce, collect, toArray
 */
public class Ex1 {

    public static void main(String[] args) {

        List<String> strings = Arrays.asList("aaa", "aabb", "aaabbc", "aaabbccd", "abc", "def");
        long count = strings.stream()
                .map(s -> s.substring(2)) // a, bb, abbc,
                .filter(s -> s.length() >= 3)
                .count();
        System.out.println(count); // 2

        boolean b1 = strings.stream()
                .anyMatch(s -> s.startsWith("a"));
        System.out.println(b1); //true
        boolean b2 = strings.stream()
                .allMatch(s -> s.startsWith("a"));
        System.out.println(b2); //false
        boolean b3 = strings.stream()
                .noneMatch(s -> s.startsWith("a"));
        System.out.println(b3); // false

        strings.stream()
                .findFirst()
                .ifPresent(System.out::println); // aaa
        strings.stream()
                .findAny()
                .ifPresent(System.out::println); // aaa


    }
}
