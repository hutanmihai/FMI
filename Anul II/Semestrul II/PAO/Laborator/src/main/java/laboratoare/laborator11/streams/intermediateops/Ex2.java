package src.main.java.laboratoare.laborator11.streams.intermediateops;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * @author cvoinea
 */
public class Ex2 {

    public static void main(String[] args) {

        List<String> strings = Arrays.asList("abc", "aa", "aba1", "cde", "efe2");
        // map() -- maps an original element to other value or type
        Stream<String> s1 = strings.stream()
                .map(String::toUpperCase); // map to same type, but different value
        IntStream s2 = strings.stream()
                .mapToInt(String::length);

        //flatMap() - returns a new stream (resulted from concatenation of resulted streams) after applying a function on initial stream
        Stream<String> uniqueWords = Stream.empty();
        try {
            uniqueWords = Files.lines(Paths.get("course_9\\src\\intermediateops\\Ex2.java"))
                    .flatMap(line -> Arrays.stream(line.split("[,.;:(){}]+")))
                    .distinct();
        } catch (IOException e) {
            System.out.println("cannot read from file");
        }
        uniqueWords.forEach(System.out::println);

    }
}
