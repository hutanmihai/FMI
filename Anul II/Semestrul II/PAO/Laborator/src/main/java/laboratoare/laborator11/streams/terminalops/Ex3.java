package src.main.java.laboratoare.laborator11.streams.terminalops;

import java.util.Arrays;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.Function;
import java.util.stream.Collectors;

/**
 * @author cvoinea
 * collect() terminal operation examples
 */
public class Ex3 {

    public static void main(String[] args) {

        List<String> strings = Arrays.asList("aaa", "aaa", "aabb", "aaabbc", "aaaabbccd", "abc", "def", "def");

        // collect to list
        List<String> list = strings.stream().limit(3).collect(Collectors.toList());
        // collect to set
        Set<String> set = strings.stream().sorted().collect(Collectors.toSet());
        // collect to map
        Map<String, Integer> result = strings.stream()
                .collect(Collectors.toMap(Function.identity(), String::length, (key, duplicateKey) -> key)); // s->s
        System.out.println(result);

        // for strings can use joining()
        String allValues = strings.stream().collect(Collectors.joining(";", "prefix: ", " :suffix"));
        System.out.println(allValues);

        // counting()
        Long count = strings.stream().collect(Collectors.counting());

        // groupingBy()
        Map<Integer, List<String>> groups = strings.stream().collect(Collectors.groupingBy(String::length, Collectors.toList()));
        System.out.println(groups);

        // partitioningBy()
        Map<Boolean, Set<String>> partitions = strings.stream().collect(Collectors.partitioningBy(s -> s.length() > 3, Collectors.toSet()));
        System.out.println(partitions);
    }
}
