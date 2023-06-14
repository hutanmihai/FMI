package main.java.laboratoare.laborator7.exceptions.ex4;

/**
 * @author cvoinea
 * <p>
 * custom unchecked exception
 */
public class MyRuntimeException extends RuntimeException {

    public MyRuntimeException(String message) {
        super(message);
    }
}
