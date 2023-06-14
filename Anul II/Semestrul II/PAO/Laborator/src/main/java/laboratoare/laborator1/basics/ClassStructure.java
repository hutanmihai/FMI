/*
 * This must be the first executable line in a Java file. It represents the location of this file.
 * Not present in classes that are not part of any package. However, this is considered a bad project design.
 */
package main.java.laboratoare.laborator1.basics;

/*
 * This is also a multi-line comment. Comments are not executable code.
 *
 * This line imports the Scanner class so that it can be used without specifying its whole fully-qualified name every time.
 * If the class does not use any classes from other packages, this "imports" section can be missing all together.
 */

import java.util.Scanner;

import static java.lang.Math.pow;

/**
 * This is a Javadoc comment
 *
 * @author cvoinea
 * <p>
 * This is the class declaration section. If this class is public, the file must be named exactly the same.
 */
public class ClassStructure { // curly brace pairs {} define Java blocks of code

    /**
     * This is a non-static class member. Each instance of the class can have its own values for these fields.
     * To access a non-static field we need an instance of the class (an object) on which we can access it.
     */
    private int instanceField; // this is an in-line comment

    /**
     * This is a static field, it belongs to the class. Thus, no matter how many objects we create of this class,
     * there will only exist one field located in the class, and the value of that field is the same, no matter from which object it is accessed.
     */
    private static int staticField;

    /**
     * A Java field can be declared final. A final field cannot have its value changed, once assigned (it is a constant).
     */
    private final int MIN_VALUE = -128;

    /**
     * This is an instance initialization block. It is run at the creation of each object, for that specific object.
     * A class can have multiple such blocks and they will be executed in the order that they appear in the class.
     */ {
        instanceField = 22;
    }

    /**
     * This a class initialization block. It is run the first time the class is referenced somewhere. It can only access
     * static fields and methods in the class.
     */
    static {
        staticField = 3;
    }

    /**
     * This is a class method member.
     *      private -> the access modifier. Can be "private", "protected", "public" or it can be left out, meaning it's "default" or "package private".
     *      double -> the return type of the method. If the method does not return anything, the return type is "void".
     *      doSomething -> the method name - can be any valid identifier in the Java language
     *      long, String -> types for the corresponding parameters
     *      firstParam, secondParam -> names of the parameters
     */
    private double doSomething(long firstParam, String secondParam) {
        return pow(10, 2); // any non-void function must return a value. If the method is void, the "return;" instruction can be used,
        // signaling that it should end its execution at that point.
    }

    /**
     * This is the main entry point in a Java class. If a class should be run, this is the signature that the Java Runtime Environment
     * will look for. If any argument was supplied when running the class, it is passed in the array.
     */
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        //use the scanner resource, then close it
        scanner.close();
    }

}

/**
 * A .java file can have multi class definitions in it. However, only one can be public.
 */
class NonPublicClass {

    /**
     * class field
     */
    private int a;

    /**
     * class method
     */
    public void doSomethingElse() {
    }
}