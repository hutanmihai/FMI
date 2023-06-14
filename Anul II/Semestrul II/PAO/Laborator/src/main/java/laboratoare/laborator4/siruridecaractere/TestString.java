package main.java.laboratoare.laborator4.siruridecaractere;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * @author cvoinea
 */
public class TestString {

    private static String defaultString; // default null pt tipuri referinta
    private int numar = 989887; // literal

    public static void main(String[] args) {

        System.out.println("default String value: " + defaultString); // null
        String s1 = ""; // empty String

        String s2 = "abc"; // String pool
        System.out.println("s2: " + s2); // abc

        s2.toUpperCase(); // imutabilitate, valoarea referentiata de s2 nu se modifica
        System.out.println("s2: " + s2); // abc

        s2 = s2.toUpperCase(); // "ABC" - se creeaza un nou obiect String in String pool, referentiat de s2
        System.out.println("s2: " + s2); // ABC

        String s3 = "cde";
        String s4 = new String("cde"); // alocare explicita de memorie pe heap
        String s5 = "cde"; // referinta catre acelasi obiect "cde" din String pool
        System.out.println("comparare referinte s3 == s4: " + (s3 == s4)); //false , referinte diferite catre obiecte diferite
        System.out.println("comparare referinte s4 == s5: " + (s4 == s5)); //false
        System.out.println("comparare referinte s3 == s5: " + (s3 == s5)); // true
        System.out.println("comparare s3.equals(s4): " + s3.equals(s4)); // true -> comparare continut

        s4 = s4.intern(); // trecere explicita in String pool
        System.out.println("comparare referinte s3 == s4: " + (s3 == s4)); //true
        System.out.println("comparare referinte s3 == s5: " + (s3 == s5)); // true

        String s6 = "efg";
        System.out.println(s6.toUpperCase() == s6.toUpperCase()); // false!!

        String nrTelefon = "0777121212";
        System.out.println("matches(): " + nrTelefon.matches("(076|077)[0-9]{7}"));// true
        // java.util.regex
        Pattern pattern = Pattern.compile("(076|077)[0-9]{7}");
        Matcher matcher = pattern.matcher("0777121212");
        System.out.println("matcher: " + matcher.find());// true
    }
}
