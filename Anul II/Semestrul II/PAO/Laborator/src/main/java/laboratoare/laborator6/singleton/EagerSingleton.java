package main.java.laboratoare.laborator6.singleton;

/**
 * @author cvoinea
 *
 * private static instance
 * private constructor
 * public static utility method to get the actual instance
 */
public class EagerSingleton {

    private static final EagerSingleton INSTANCE = new EagerSingleton();

    // instantiation can also happen in static block
//    static {
//        INSTANCE = new EagerSingleton();
//    }

    private EagerSingleton() {
    }

    public static EagerSingleton getInstance() {
        return INSTANCE;
    }
}
