package main.java.laboratoare.laborator6.sealed;

/**
 * @author cvoinea
 */
public sealed abstract class Payment implements Taxable permits Card, Cash {


}
