package main.java.laboratoare.laborator1.basics;

/**
 * @author cvoinea
 * <p>
 * expression - a construct made up of variables, operators, and method invocations
 *            - constructed according to the syntax of the language
 *            - evaluates to a single value
 * use parentheses when writing compound expressions
 * <p>
 * statement - roughly equivalent to a sentence in natural language
 *           - forms a complete unit of execution
 */
public class  ExpressionsStatementsBlocks {

    public static void main(String[] args) { // begin block main method

        //int age = 20 // this expression returns an int (the assignment operator returns a value of the same type as left operand)

        // Expression statements (expressions ending with a semicolon ; )
        ;

        // assignment statement
        double d = 123.45;

        // increment statement
        d++;

        // method invocation statement
        System.out.println("Hello World!");

        // object creation statement
        Object name = new Object();

        int age = 20; // declaration statement

        if (true) { // begin block
            System.out.println("true");
        } // end block
        else { // begin block
            System.out.println("false");
        } // end block

    } // end block main method
}
