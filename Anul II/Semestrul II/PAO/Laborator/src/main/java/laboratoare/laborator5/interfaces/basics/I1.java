package main.java.laboratoare.laborator5.interfaces.basics;

/**
 * @author cvoinea
 *
 * all fields are public static final:
 *      - public => accessible from anywhere in the code (before Java 9 <-- modules)
 *      - final => they are constants
 *      - static => they are not owned by an instance (interfaces are abstract types)
 *
 * before Java 8 -> only abstract methods (so all methods were implicitly public abstract)
 * starting Java 8, concrete methods were introduced -> public non-static/instance methods = public default methods: they are inherited
 *                                                   -> public static methods
 *                  -> they were introduced to extend the existing language functionality while also maintaining backwards compatibility
 *
 * before Java 9, all interface members were public
 * starting Java 9, private static and non-static/instance methods were introduced -> achieve code reuse in interfaces while not exposing it outside
 *
 */
@FunctionalInterface //interfaces that define exactly one abstract method
public interface I1 {

    // public static final
    public static final int FIELD1 = 1;
    static int FIELD2 = 2;
    public int FIELD3 = 3;
    final int FIELD4 = 4;

    // public abstract
    public abstract void m1();

    // public, default methods since java 8
    public default void m2() {
        m5();
        System.out.println("default m1");
    }

    public default void m4() {
        m5();
        m6();
        System.out.println("default m4");
    }

    public static void m3() {
        m6();
        System.out.println("static method m3");
    }

    // since Java 9
    private void m5() {
        System.out.println("-----inteface I1-----");
    }

    private static void m6(){
        System.out.println("-----inteface I1-----");
    }


}
/*
 * marker interface -> has no methods or constants
 *                  -> provides runtime type information about objects
 *                  -> can be replaced by using annotations
 * JDK examples of marker interfaces: Cloneable, Serializable, Remote
 */
interface I2{}

// classes allowed to implement multiple interfaces
// C1 is-a I1
// C1 is-a I2
class C1 implements I1, I2 {

    @Override
    public void m1() {
        System.out.println("m1 in class C1");
    }

    @Override
    public void m4() {
        System.out.println("override inherited default method m4");
        // can call the inherited method using: [InterfaceName].super.[methodName]
        I1.super.m4();

        // calling m4() this way is bad => java.lang.StackOverflowError exception (infinite recursive call)
        //m4();
    }

    void m7(){
        System.out.println("m7");
    }
}