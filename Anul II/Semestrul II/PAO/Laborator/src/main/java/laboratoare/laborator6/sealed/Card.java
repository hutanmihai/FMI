package main.java.laboratoare.laborator6.sealed;

/**
 * @author cvoinea
 */
public sealed class Card extends Payment permits CreditCard, DebitCard {
}
