package main.java.laboratoare.laborator1.instructions;

import java.util.Scanner;

/**
 * @author cvoinea
 *
 * program that checks whether the input character is vowel or consonant
 *
 * TO DO: write a program that outputs the number of days of a particular month of a year (input from keyboard)
 */
public class SwitchStatement {

    public static void main(String[] args) {

        boolean isVowel = false;
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a character: ");
        char inputChar = scanner.next().charAt(0);
        scanner.close();

        switch (inputChar) {  // works only with single integer value, enum value or String
            case 'a':  // executed in sequence until break statement is encountered;
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case 'A':
            case 'E':
            case 'I':
            case 'O':
            case 'U': {
                isVowel = true;
                break;  // necessary because otherwise statements fall through
            }
            default: {
                System.out.println(inputChar + " surely is not a vowel");
                break; // not necessary, but recommended - less error-prone for future development
            }

        }

        if (isVowel) {
            System.out.println(inputChar + " is a vowel");
        } else {
            if ((inputChar >= 'a' && inputChar <= 'z') || (inputChar >= 'A' && inputChar <= 'Z'))
                System.out.println(inputChar + " is a consonant");
            else
                System.out.println("Input is not a letter");
        }

    }
}
