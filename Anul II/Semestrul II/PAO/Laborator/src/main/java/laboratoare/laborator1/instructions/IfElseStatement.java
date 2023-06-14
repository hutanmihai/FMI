package main.java.laboratoare.laborator1.instructions;

import java.util.Scanner;

/**
 * @author cvoinea
 *
 * Program to check whether the given number is positive or negative
 *
 * TO DO: write a program to check leap year
 */
public class IfElseStatement {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        scanner.close();

        if (number > 0) {
            System.out.println(number + " is positive");
        } else if (number < 0) {
            System.out.println(number + " is negative");
        } else {
            System.out.println(number + " is neither positive nor negative");
        }
    }
}
