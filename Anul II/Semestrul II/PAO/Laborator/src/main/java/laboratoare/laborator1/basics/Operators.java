package main.java.laboratoare.laborator1.basics;

/**
 * @author cvoinea
 */
public class Operators {

    public static void main(String[] args) {

        boolean b1 = true;
        boolean b2 = false;

        boolean b3 = b1 || (b2 = 'A' == 65); // short-circuiting OR
        System.out.println(b3);
        System.out.println(b2);

        int number;
        number = b2 ? 1 : 0; // ternary operator, shorthand for if-then-else
        System.out.println(number);

        b2 = args instanceof Object; // instanceof operator
        System.out.println(b2);

        b3 = null instanceof Object; // null literal is not an instance of anything
        System.out.println(b3);
    }
}
