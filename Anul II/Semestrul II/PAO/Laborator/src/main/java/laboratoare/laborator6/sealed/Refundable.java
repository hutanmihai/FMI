package main.java.laboratoare.laborator6.sealed;

/**
 * @author cvoinea
 */
public sealed interface Refundable extends Taxable permits VatRefundable{
}
