package main.java.laboratoare.laborator3.polimorfism.zoo.ierbivor;

/**
 * @author cvoinea
 */
public class Cal extends Ierbivor {

    public Cal(String nume, int varsta) {
        super(nume, varsta);
        this.sunetSpecific = "necheaza";
    }

    @Override
    public void scoateSunet() {
        System.out.println("calul " + this.sunetSpecific);
    }
}
