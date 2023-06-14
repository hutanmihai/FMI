package src.main.java.laboratoare.laborator11.streams.streamsource;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Random;
import java.util.Set;
import java.util.stream.DoubleStream;
import java.util.stream.IntStream;
import java.util.stream.LongStream;
import java.util.stream.Stream;

/**
 * @author cvoinea
 * ways to create streams
 */
public class Ex2 {

    public static void main(String[] args) {

        // using factory method of(T.. values) - stream on an array
        // Arrays.stream(values) is called, in fact
        Stream<String> streamOnArray = Stream.of("aa", "aaaa", "aaabb", "aabc", "abc");
        streamOnArray.forEach(System.out::println);

        // of(T t)
        int[] i1 = {1, 3, 5, 6, 8, 9, 2};
        Stream.of(i1).forEach(System.out::println); // Stream<int[]>
        Stream<int[]> s2 = Stream.of(i1);
        Set<Integer> setOfIntegers = new HashSet<>(Arrays.asList(33, 44, 55, 77, 33, 44)); // duplicates are removed
        Stream<Set<Integer>> stream = Stream.of(setOfIntegers); // order of elements in stream is not guaranteed since the source is a hashset
        stream.forEach(System.out::println); // only one object in stream -- a hashset
        // vs
        IntStream s3 = Arrays.stream(i1); // can also have streams on primitives like DoubleStream, LongStream;
        IntStream s4 = Arrays.stream(i1, 1, 4); // stream consisting of elements with index in interval [1, 4)
        s4.forEach(System.out::println); // 3 5 6

        IntStream i5 = IntStream.range(1, 5);
        i5.forEach(System.out::println); // [1,5)
        LongStream ls1 = LongStream.rangeClosed(1, 5);
        ls1.forEach(System.out::println); // [1,5]

        Random random = new Random();
        DoubleStream d1 = random.doubles().limit(5); // infinite stream source if limit(long limitValue) is not used
        d1.forEach(System.out::println);
        DoubleStream d2 = random.doubles(5, 5,6); // generate 5 random doubles in [5, 6] interval
        d2.forEach(System.out::println);

        // generate()
        // infinite stream source if limit(long limitValue) is not used
        Stream<String> generatedStream = Stream.generate(() -> "item").limit(5);

        // iterate() --> takes a seed and an UnaryOperator
        // infinite stream source if limit(long limitValue) is not used
        Stream<Integer> intStream = Stream.iterate(0, i -> i + 5).limit(10);

    }
}
