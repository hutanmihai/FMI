package sample.exceptions;

/**
 * @author cvoinea
 * <p>
 * Use custom exceptions (checked or unchecked):
 * * to implement exceptions that are specific to the business logic and workflow
 * * to catch and provide specific treatment to a subset of existing Java exceptions
 */
public class CustomException extends Exception {

    /**
     * create a custom exception with a relevant error message
     */
    public CustomException(String message) {
        super(message);
    }

    /**
     * Use this overloaded constructor if the exception root cause is important
     */
    public CustomException(String message, Throwable cause) {
        super(message, cause);
    }
}
