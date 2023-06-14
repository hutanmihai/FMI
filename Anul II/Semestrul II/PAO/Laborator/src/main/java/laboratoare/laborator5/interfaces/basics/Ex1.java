package main.java.laboratoare.laborator5.interfaces.basics;

/**
 * @author cvoinea
 */
public class Ex1 {

    public static void main(String[] args) {

        // type polymorphism
        C1 c1 = new C1();
        I1 c11 = new C1();
        I2 c111 = new C1();


        // Using C1 reference type:
        // can call the inherited and overridden abstract method from interface (will use the implementation in C1)
        c1.m1();
        // can call the inherited default method
        c1.m2();
        // can call the inherited and overridden default method from interface (runtime polymorphism -> m4() in C1 gets called at runtime)
        c1.m4();
        // obviously can call own behaviour
        c1.m7();
        // cannot access public static method from interface (it is not inherited, can access it only with an Interface reference)
        //c1.m3();
        // cannot access private instance method from outside the interface
        //c1.m5();
        // cannot access private static method from outside the interface
        //c1.m6();

        // Using I1 reference type
        c11.m1();
        c11.m2();
        c11.m4();
        // cannot access this behaviour because it is not available with the specified reference type (I1)
        //c11.m7();
        // can be solved with an explicit type cast
        ((C1) c11).m7();

        // can access static methods
        I1.m3();

        // access constants using the declared interface reference type
        System.out.println(I1.FIELD1);
    }
}
