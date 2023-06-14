package main.java.laboratoare.laborator5.interfaces.model.vehicle;


import main.java.laboratoare.laborator5.interfaces.basics.Washable;

/**
 * @author cvoinea
 */
public class Car implements Washable {

    @Override
    public void wash() {
        System.out.println("washing a car");
    }
}
