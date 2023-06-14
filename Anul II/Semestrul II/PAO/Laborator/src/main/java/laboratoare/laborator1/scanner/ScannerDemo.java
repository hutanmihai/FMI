package main.java.laboratoare.laborator1.scanner;

import java.util.Scanner;

/**
 * @author cvoinea
 *
 * program to read your name input from keyboard
 *
 */

public class ScannerDemo {

    public static void main(String[] args) {

        // A simple text scanner which can parse primitive types and strings (using regular expressions)
        Scanner scanner = new Scanner(System.in);

        // here using an output stream
        System.out.println("Enter your name: ");

        // here we actually read keyboard input
        String myName = scanner.nextLine();

        // close the resource !!
        scanner.close();

        // display the input to console
        System.out.println("My name is: " + myName);
    }
}
