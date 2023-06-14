package main.java.laboratoare.laborator3.polimorfism.zoo.omnivor;

/**
 * @author cvoinea
 */
public class Urs extends Omnivor {

    public Urs(String nume, int varsta) {
        super(nume, varsta);
        this.sunetSpecific = "mormaie";
    }

    @Override
    public void scoateSunet() {
        System.out.println("ursul " + this.sunetSpecific);
    }
}
