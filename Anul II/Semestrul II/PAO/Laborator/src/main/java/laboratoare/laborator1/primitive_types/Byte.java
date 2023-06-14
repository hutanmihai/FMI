package main.java.laboratoare.laborator1.primitive_types;

/**
 * @author cvoinea
 *
 *  Java is statically-typed --> all variables must first be declared (type and name) before they can be used
 *  kind of variables: instance var (non-static fields), class var (static fields), local vars, params
 *
 *  primitive data type vs. non-primitive/ reference data type
 *  variable's data type determines: values it may contain and operations that may be performed on it
 *
 *  Primitive data types: predefined by the language and named by a reserved keyword
 *  They directly hold a value in memory (number or character)
 *  They are not objects or references to objects
 *  Primitive values don't share state with other primitive values
 *  The values stored in primitives are called literals (source code representation of a fixed value e.g. 232)
 *
 */
public class Byte {

    static byte defaultValue;

    public static void main(String[] args) {

        // byte --> 8-bit integer values
        byte b1 = -128;  // local variables must be initialized before use
        System.out.println(b1);

        byte b2 = 127;
        System.out.println(b2);
        b2++;

        System.out.println(b2++);
        System.out.println(++b2);

//        byte b3 = 12345;  // doesn't compile, assigned value is an int, by default

        System.out.println(defaultValue);
    }
}
