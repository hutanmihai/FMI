package src.main.java.laboratoare.laborator11.streams.intermediateops;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.Random;
import java.util.stream.DoubleStream;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * @author cvoinea
 * a stream pipeline consists of elements: a source, intermediate operations and terminal operation
 * intermediate ops. are optional for the stream to be consumed (can have only source and terminal operation)
 * intermediate ops transform the stream into another stream
 * intermediate ops: limit, skip, distinct, sorted, filter, peek, map, flatMap
 */
public class Ex1 {

    public static void main(String[] args) {

        Stream<String> s1 = Stream.of("aa", "aaab", "aabbcc", "abc")
                .filter(s -> s.startsWith("aa")); //
        Optional<String> anyElement = s1.findAny(); // functional style of declaring operations
        System.out.println(anyElement);

        /* a stream instance is accessible as long as only intermediate ops were called
         * executing a terminal operation makes that stream instance inaccessible (it's already consumed)
         * IllegalStateException if trying to reuse a stream instance after a terminal operation has been called */
//        Optional<String> firstElement = s1.findFirst();

        List<Integer> ints = Arrays.asList(1, 1, 9, 9, 2, 2, 2, 8, 8, 4, 5, 5);

        // limit()
        DoubleStream ds1 = new Random().doubles().limit(3);
        // skip
        IntStream is1 = IntStream.rangeClosed(1, 10).skip(5);
        is1.forEach(System.out::println); // 6 7 8 9 10
        // distinct and sorted
        Stream<Integer> is2 = ints.stream();
        is2.distinct()
                .sorted()
                .forEach(System.out::println); // 1 2 4 5 8 9
        // filter
        long count = ints.stream()
                .filter(i -> i % 2 == 1)
                .count();
        // peek - designed for debugging; do not use to modify the stream
        System.out.println("peek method");
        ints.stream() // initial values: 1, 1, 9, 9, 2, 2, 2, 8, 8, 4, 5, 5
                .distinct() // 1, 9, 2, 8, 4, 5
                .peek(i -> System.out.println("distinct value " + i + " "))
                .sorted() // 1, 2, 4, 5, 8, 9
                .peek(i -> System.out.println("sorted value " + i + " "))
                .filter(i -> i % 2 == 0) // 2, 4, 8
                .forEach(System.out::println);
    }
}
