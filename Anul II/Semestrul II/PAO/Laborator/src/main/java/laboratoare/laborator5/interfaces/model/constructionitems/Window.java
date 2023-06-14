package main.java.laboratoare.laborator5.interfaces.model.constructionitems;


import main.java.laboratoare.laborator5.interfaces.basics.Washable;

/**
 * @author cvoinea
 */
public class Window implements Washable {

    @Override
    public void wash() {
        System.out.println("washing a window");
    }
}
