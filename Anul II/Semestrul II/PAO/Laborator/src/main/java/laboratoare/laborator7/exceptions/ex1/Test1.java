package main.java.laboratoare.laborator7.exceptions.ex1;

/**
 * @author cvoinea
 * exceptions can be thrown:
 * 	- by the programmer
 * 	- by the code imported from other packages, libraries etc.
 * 	- by the runtime environment
 *
 * Throwable in java.lang
 *    Error  -> unchecked exceptions
 *       StackOverflowError
 *
 *    Exception -> checked exception (compile-time) - checkedby the compiler, if not treated, code will not compile
 *  		IOException (java.io), SQLException (java.sql)
 *          RuntimeException -> unchecked exception (runtime)
 *           		NPE, IndexOutOfBoundsException, ArithmeticException, IllegalArgumentException (NumberFormatException), ClassCastException *
 *
 *   usually defined in the same package with the classes that generate them (especially the checked exceptions)
 *
 *
 *  Exception -> checked-exceptions - compile-time (Exception and subclasses, excluding RuntimeException and its subclasses)
 *            -> unchecked exceptions - runtime (RuntimeException and subclasses)
 *
 *  try {
 *      // code that throws/susceptible to throw exception(s)
 *  } catch(Exception e) {
 *      // catch the exception and implement specific logic (the app continues to run)
 *  } finally {
 *      // always executes (*), ussually closing resources here
 *  }
 */
public class Test1 {

    public static void main(String[] args) {
        try {
//			System.out.println("exiting before catch and finally");
//			System.exit(0);  //
            m1();
            Object obj = new Object();
            // ClassCastException
            String s = (String) obj;
            System.out.println(s);
        } catch (StackOverflowError exc){ // can use same variable name because the scope is different for each
            System.out.println(exc);
//			obj = "";  // cannot use here this reference because it is out of scope (its scope is delimited by the try block)
//			System.exit(0); // if uncommented, finally doesn't execute anymore
            return;
        } catch (ClassCastException exc){
            System.out.println(exc);
        } finally {
            // executes even if 'return' statement is user in try or catch
            // does not execute when calling System.exit(0) or possibly when getting OutOfMemoryException
            System.out.println("in finally");
        }
    }
    // throws StackOverflowError
    public static void m1(){
        m1();
    }
}
