package main.java.laboratoare.laborator7.exceptions.ex3;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.NoSuchElementException;
import java.util.Scanner;

/**
 * @author cvoinea
 */
public class Test1 {

    private static final String CURRENT_DIR = "./src/main/java/laboratoare/laborator7/exceptions/ex3/";

    public static void main(String[] args) {

        int a, b;
        try {
            createFile();
            Scanner scanner = new Scanner(new File(CURRENT_DIR, "test.txt"));
            a = scanner.nextInt();
            b = scanner.nextInt();
            int result = a / b;
            System.out.println(result);
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.out.println("could not find specified file");
        } catch (NoSuchElementException e) {
            System.out.println("no elements to read in file");
        } catch (NumberFormatException nfe) {
            System.out.println("Wrong number format");
        } catch (ArithmeticException ae) {
            System.out.println("division by 0");
        } catch (IOException e) {
            System.out.println("cannot open the file");
        } finally {
            System.out.println("in finally");
        }
    }

    static void createFile() throws IOException {
        File file = new File(CURRENT_DIR, "test.txt");
        if (file.createNewFile()) {
            System.out.println("file created");
        } else {
            System.out.println("file already exists");
        }
    }


}