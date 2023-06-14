package main.java.laboratoare.laborator3.exercitiu;

/**
 * @author cvoinea
 */
public class TestLindt {

    public static void main(String[] args) {

        CandyBox lindt1 = new Lindt();
        lindt1.flavor = "abc";
        lindt1.origin = "cde";
        System.out.println(lindt1);
        System.out.println(lindt1.getVolume());
        System.out.println(lindt1.flavor);
        System.out.println(lindt1.origin);

        CandyBox lindt2 = new Lindt("fff", "ggg", 4, 3, 2);
        System.out.println(lindt2);
        System.out.println(lindt2.flavor);
        System.out.println(lindt2.origin);
        System.out.println(lindt2.getVolume());
    }
}
