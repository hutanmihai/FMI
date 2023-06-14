package main.java.laboratoare.laborator3.exercitiu;

/**
 * @author cvoinea
 */
public class TestCandyBox {

    public static void main(String[] args) {

        CandyBox cb1 = new CandyBox();
        System.out.println(cb1.toString()); // apel explicit toString()

        CandyBox cb2 = new CandyBox("strawberry", "swiss");
        System.out.println(cb2); // apel implicit toString()

        CandyBox cb3 = cb2;

        CandyBox cb4 = new CandyBox("strawberry", "swiss");


        System.out.println("equals: " + cb1.equals(cb2)); // false
        System.out.println("equals: " + cb3.equals(cb2)); // true
        System.out.println("equals: " + cb4.equals(cb2)); // true


    }
}
