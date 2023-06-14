package main.java.laboratoare.laborator1.instructions;

import java.util.Scanner;

/**
 * @author cvoinea
 *
 * do while ()
 */
public class WhileStatement {

    public static void main(String[] args) {

        int inputNo;
        int reversedNo = 0;

        System.out.println("Input an int number: ");
        Scanner scanner = new Scanner(System.in);
        inputNo = scanner.nextInt();
        scanner.close();

        while (inputNo != 0) {
            reversedNo = reversedNo * 10; // 0
            reversedNo = reversedNo + inputNo % 10;// 0 + 9 = 9
            inputNo = inputNo / 10; //12345678
        }

        System.out.println("Reversed no: " + reversedNo);

        int a = 0;
        do {
            a ++;
            // bloc instructiuni
        } while (a != 0);

    }
}
