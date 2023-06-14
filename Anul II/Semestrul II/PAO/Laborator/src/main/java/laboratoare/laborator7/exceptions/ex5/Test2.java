package main.java.laboratoare.laborator7.exceptions.ex5;

/**
 * @author cvoinea
 *
 * same example as in Test1, but much more concise using try-with-resources
 */
public class Test2 {

    public static void main(String[] args) {

        // try without catch or finally
        try (R1 r1 = new R1("r1")) {
//			r1 = new R1();  // implicitly final, cannot reassign !!!
            //some logic here
        }
    }
}