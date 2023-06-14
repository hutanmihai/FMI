package main.java.laboratoare.laborator7.exceptions.ex2;

/**
 * @author cvoinea
 */
public class Test1 {

    public static void main(String[] args) {

        try {
            int x = m1();
            System.out.println(x); // doesn't execute, exception is thrown before this line
        } catch (ArithmeticException e) {
            System.out.println("executing catch");
        } finally {
            System.out.println("code that must execute");
        }
    }

    static int m1() {
        int i = 5 / 0; // ArithmeticException
        System.out.println(i);
        return i;
    }
}
