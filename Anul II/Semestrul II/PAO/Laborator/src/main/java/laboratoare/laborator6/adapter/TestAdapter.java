package main.java.laboratoare.laborator6.adapter;


import main.java.laboratoare.laborator6.adapter.library.ABritishCar;
import main.java.laboratoare.laborator6.adapter.library.Movable;
import main.java.laboratoare.laborator6.adapter.own_app.MovableAdapter;
import main.java.laboratoare.laborator6.adapter.own_app.MovableAdapterImpl;

/**
 * @author cvoinea
 */
public class TestAdapter {

    public static void main(String[] args) {

        Movable car1 = new ABritishCar(100);

        System.out.printf("Car speed in MPH: %s", car1.getSpeed());
        System.out.println();

        // after adapting
        MovableAdapter adaptedCar = new MovableAdapterImpl(car1);
        System.out.printf("Car speed adapted to KMPH: %s", adaptedCar.getSpeed());
    }
}
