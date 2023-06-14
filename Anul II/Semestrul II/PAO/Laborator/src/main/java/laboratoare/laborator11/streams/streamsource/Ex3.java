package src.main.java.laboratoare.laborator11.streams.streamsource;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.regex.Pattern;
import java.util.stream.IntStream;
import java.util.stream.Stream;

/**
 * @author cvoinea
 * ways to create streams
 */
public class Ex3 {

    public static void main(String[] args) {

        // there is no CharStream interface in JDK, so use IntStream to represent a stream of chars
        IntStream streamOfChars = "abcabcabc".chars();
        streamOfChars.distinct().forEach(c -> System.out.println((char)c));

        // stream of strings from Pattern class
        Stream<String> streamOfString = Pattern.compile(",").splitAsStream("a,b,c,d,e,f,g,h");
        streamOfString.forEach(System.out::println);

        // stream of strings from Files class
        Path path = Paths.get("course8\\src\\streams\\streamsource\\Ex3.java");
        Stream<String> streamOfLines = Stream.empty();
        try {
            streamOfLines = Files.lines(path);
        } catch (IOException e) {
            System.out.println("cannot read from file!");
        }
        streamOfLines.forEach(System.out::println);

    }
}
