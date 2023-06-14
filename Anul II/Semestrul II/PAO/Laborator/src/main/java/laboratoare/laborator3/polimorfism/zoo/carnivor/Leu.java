package main.java.laboratoare.laborator3.polimorfism.zoo.carnivor;

/**
 * @author cvoinea
 */
public class Leu extends Carnivor {

    public Leu(String nume, int varsta) {
        super(nume, varsta);
        this.sunetSpecific = "rage";
    }

    @Override
    public void scoateSunet() {
        System.out.println("leul " + this.sunetSpecific);
    }
}
