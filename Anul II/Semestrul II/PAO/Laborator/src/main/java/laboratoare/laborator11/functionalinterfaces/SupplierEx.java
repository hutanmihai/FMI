package src.main.java.laboratoare.laborator11.functionalinterfaces;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.function.Supplier;

/**
 * @author cvoinea
 *
 * T get()
 *
 */
public class SupplierEx {

    public static void main(String[] args) {

        Supplier<LocalDate> s1 = new Supplier<LocalDate>() {
            @Override
            public LocalDate get() {
                return LocalDate.now();
            }
        };
        Supplier<LocalDate> s2 = () -> LocalDate.now();
        Supplier<LocalDate> s3 = LocalDate::now; // reference to a static method

        LocalDate d1 = s1.get();
        LocalDate d2 = s2.get();
        LocalDate d3 = s3.get();
        System.out.println(d1);
        System.out.println(d2);
        System.out.println(d3);

        Supplier<StringBuilder> sb1 = () -> new StringBuilder();
        Supplier<StringBuilder> sb2 = StringBuilder::new; // method reference to a constructor
        System.out.println(sb1.get().append("sb1"));
        System.out.println(sb2.get().append("sb2"));

        Supplier<ArrayList<String>> sb3 = ArrayList::new; // method reference to a constructor
        ArrayList<String> ar1 = sb3.get();
        System.out.println(ar1);

        // the class denoted here exists only in memory, not on FS
        System.out.println(s3);
    }
}
