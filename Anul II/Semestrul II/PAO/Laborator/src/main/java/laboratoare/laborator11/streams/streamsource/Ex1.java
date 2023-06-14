package src.main.java.laboratoare.laborator11.streams.streamsource;

import java.util.Arrays;
import java.util.Comparator;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Stream;

/**
 * @author cvoinea
 * Stream interface in package java.multiuserchat.util.stream
 * ways to create streams
 */
public class Ex1 {

    public static void main(String[] args) {

        List<Integer> intList = Arrays.asList(1, 4, 6, 7, 8, 9, 33, 22);
        // process elements using iteration
//        for (int i : ints) {
//            if (i % 2 == 0) {
//                System.out.println(i);
//            }
//        }

        // using stream() method on a collection
        Stream<Integer> streamOnCollection = intList.stream();
        streamOnCollection
                .filter(i -> i % 2 == 0)
                .forEach(i -> System.out.println(i)); // System.out::println

        // empty() -- see streamOf() method below
        long count = streamOf(new HashSet<>()).count(); //!! count() returns a long value
        System.out.println(count);

        // builder() - type should be specified, otherwise Stream<Object> is created
        Stream<String> streamWithBuilder = Stream.<String>builder().add("aa").add("aab").add("aabbc").build();
        streamWithBuilder
                .filter(s -> s.startsWith("aa"))
                .peek(System.out::println)
                .max(Comparator.comparing(String::length))
                .ifPresent(System.out::println);
    }

    // empty() ---> avoid returning null, but a stream with no elements instead
    public static Stream<String> streamOf(Set<String> set) {
        return set == null || set.isEmpty() ? Stream.empty() : set.stream();
    }
}
