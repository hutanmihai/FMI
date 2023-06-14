package main.java.laboratoare.laborator5.interfaces.model.cup;


import main.java.laboratoare.laborator5.interfaces.basics.Washable;

/**
 * @author cvoinea
 */
public class Cup implements Washable {

    double volume;
    String color;

    public int getLevelOfFragility() {
        return Washable.FRAGILE;
    }

    public boolean isEmpty() {
        return volume == 0;
    }

    @Override
    public void wash() {
        System.out.println("washing a cup");
    }
}
