package main.java.laboratoare.laborator6.sealed;

/**
 * @author cvoinea
 *
 * sealed, non-sealed -> restricting inheritance
 *
 *                                  taxable
 *                                   ^  ^
 *                                  /    \
 *                           payment     refundable
 *                         ^       ^           ^
 *                        /         \           \
 *                       /           \           \
 *                    card           cash     vat-refundable
 *                    ^  ^
 *                  /     \
 *                /        \
 *         creditCard      debitCard
 *             ^
 *             |
 *             |
 *          amexCard
 */
public class Ex1 {

    public static void main(String[] args) {

    }
}
