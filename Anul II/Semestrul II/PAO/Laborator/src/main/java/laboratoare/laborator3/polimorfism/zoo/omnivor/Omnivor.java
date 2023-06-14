package main.java.laboratoare.laborator3.polimorfism.zoo.omnivor;

import main.java.laboratoare.laborator3.polimorfism.zoo.Animal;

/**
 * @author cvoinea
 */
public abstract class Omnivor extends Animal {

    public Omnivor(String nume, int varsta) {
        super(nume, varsta);
        this.tipHrana = "carne si vegetatie";
    }

    @Override
    public void seHraneste() {
        System.out.println(this + " se hraneste cu " + this.tipHrana);
    }
}
