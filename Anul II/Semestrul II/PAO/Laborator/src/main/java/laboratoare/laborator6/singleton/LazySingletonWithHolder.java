package main.java.laboratoare.laborator6.singleton;

/**
 * @author cvoinea
 */
public class LazySingletonWithHolder {

    private LazySingletonWithHolder() {
    }

    static class SingletonHolder {
        private static final LazySingletonWithHolder INSTANCE = new LazySingletonWithHolder();
    }

    public static LazySingletonWithHolder getInstance() {
        return SingletonHolder.INSTANCE;
    }
}
