package main.java.laboratoare.laborator6.singleton;

/**
 * @author cvoinea
 */
public class TestSingleton {

    public static void main(String[] args) {

        EagerSingleton e1 = EagerSingleton.getInstance();
        EagerSingleton e2 = EagerSingleton.getInstance();
        System.out.println(e1 == e2); // true

        LazySingleton l1 = LazySingleton.getInstance();
        LazySingleton l2 = LazySingleton.getInstance();
        System.out.println(l1 == l2); // true

        LazySingletonWithHolder lh1 = LazySingletonWithHolder.getInstance();
        LazySingletonWithHolder lh2 = LazySingletonWithHolder.getInstance();
        System.out.println(lh1 == lh2); // true
    }
}
