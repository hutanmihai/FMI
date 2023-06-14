package src.main.java.laboratoare.laborator11.streams.terminalops;

import java.util.Arrays;
import java.util.Comparator;
import java.util.IntSummaryStatistics;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * @author cvoinea
 */
public class Ex2 {

    public static void main(String[] args) {

        // min, max
        List<String> strings = Arrays.asList("aaa", "aaa", "aabb", "aaabbc", "aaaabbccd", "abc", "def", "def");
        strings.stream()
                .min(Comparator.comparingInt(String::length))
                .ifPresent(System.out::println);
        strings.stream()
                .max(Comparator.comparingInt(String::length))
                .ifPresent(System.out::println);

        //reduce
        strings.stream()
                .reduce(String::concat) // returns an optional; (a, b) -> a.concat(b)
                .ifPresent(System.out::println);
        String concat = strings.stream()
                .reduce("prefix: ", String::concat); // always returns the value provided as identity
        System.out.println(concat);

        System.out.println(Stream.of(1, 3, 5, 7, 8, 9, 33, 44)
                .reduce(0, Integer::sum)); //(x, y) -> x + y
        // sum performed with int stream
        IntStream i1 = IntStream.rangeClosed(1, 100);
        System.out.println(i1.reduce(0, Integer::sum));
        // same thing, but using sum() terminal method on primitive streams
        IntStream i2 = IntStream.rangeClosed(1, 100);
        System.out.println(i2.sum());
        // a summary statistics object has multiple useful methods
        IntStream i3 = IntStream.rangeClosed(1, 100);
        IntSummaryStatistics iss = i3.summaryStatistics();
        System.out.println(iss.getSum());
        System.out.println(iss.getAverage());
    }
}
