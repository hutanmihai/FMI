package main.java.laboratoare.laborator7.exceptions.ex5;

import java.util.Arrays;

/**
 * @author cvoinea
 */
public class Test4 {

    public static void main(String[] args) {

        try (R2 r1 = new R2("r1");
             R2 r2 = new R2("r2")) {
            // this exception is caught and it suppresses other exceptions (thrown in close() method, for example)
            throw new Exception("exception in try block");
        } catch (Exception e) {
            System.out.println(e);
            // suppressed exceptions
           Throwable[] suppressedExceptions = e.getSuppressed();
            System.out.println(Arrays.toString(suppressedExceptions));
        } finally {
            System.out.println("finally");
        }
    }
}
