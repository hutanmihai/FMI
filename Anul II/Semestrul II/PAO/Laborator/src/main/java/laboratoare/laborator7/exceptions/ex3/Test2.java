package main.java.laboratoare.laborator7.exceptions.ex3;

import java.io.File;
import java.io.IOException;
import java.util.NoSuchElementException;
import java.util.Scanner;

/**
 * @author cvoinea
 */
public class Test2 {

    public static void main(String[] args) {

        int a, b;
        try {
            createFile();
            Scanner scanner = new Scanner(new File("./course6/src/exceptions/ex3/test.txt"));
            a = scanner.nextInt();
            b = scanner.nextInt();
            double result = a / b;
            System.out.println(result);
            scanner.close();
            // when using multi-catch, exceptions must be disjoint (not part of the same exception hierarchy)
        } catch (IOException | NoSuchElementException | ArithmeticException e) {
            System.out.println(e);
            // cannot reassign a value to variable in multi-catch -> it is effectively final
//            e = new NoSuchElementException();
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            System.out.println("finally");
            b = 0;
        }
    }

    static void createFile() throws IOException {
        File file = new File("test.txt");
        if (file.createNewFile()) {
            System.out.println("file created");
        } else {
            System.out.println("file already exists");
        }
//        throw new IOException("io exception while creating file");
    }


}
