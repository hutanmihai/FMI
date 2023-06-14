package main.java.laboratoare.laborator7.exceptions.ex5;

/**
 * @author cvoinea
 */
public class R1 implements AutoCloseable {

    private String name;

    public R1(String name) {
        this.name = name;
    }

    @Override
    public void close() {
        System.out.println("closing " + name);
    }
}
