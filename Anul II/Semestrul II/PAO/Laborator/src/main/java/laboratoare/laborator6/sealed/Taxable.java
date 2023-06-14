package main.java.laboratoare.laborator6.sealed;

/**
 * @author cvoinea
 */
public sealed interface Taxable permits Payment, Refundable{
}
