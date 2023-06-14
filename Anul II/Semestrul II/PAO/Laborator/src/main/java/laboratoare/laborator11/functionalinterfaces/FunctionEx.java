package src.main.java.laboratoare.laborator11.functionalinterfaces;

import java.util.function.BiFunction;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.UnaryOperator;

/**
 * @author cvoinea
 *
 * Function<T, R> --> R apply(T t)
 * BiFunction<T, U, R> --> R apply(T t, U u)
 * UnaryOperator<T> --> T apply(T t)
 * BinaryOperator<T> --> T apply(T t, T t)
 */
public class FunctionEx {
    public static void main(String[] args) {

        Function<String, Integer> f1 = x -> x.length();
        Function<String, Integer> f2 = String::length;
        System.out.println(f1.apply("clock"));  // 5
        System.out.println(f2.apply("click"));  // 5

        BiFunction<String, String, String> bf1 = (initialString, toAdd) -> initialString.concat(toAdd);
        BiFunction<String, String, String> bf2 = String::concat;
        System.out.println(bf1.apply("bi ", "function"));
        System.out.println(bf2.apply("method ", "reference"));

        UnaryOperator<String> u1 = x -> x.toUpperCase();
        UnaryOperator<String> u2 = String::toUpperCase;
        System.out.println(u1.apply("AbbA"));
        System.out.println(u2.apply("eXe"));

        BinaryOperator<String> b1 = (initialString, toAdd) -> initialString.concat(toAdd);
        BinaryOperator<String> b2 = String::concat;
        System.out.println(b1.apply("binary ", "operator"));
        System.out.println(b2.apply("functional ", "Interfaces"));
    }
}
