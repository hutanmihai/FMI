package main.java.laboratoare.laborator6.adapter.own_app;


import main.java.laboratoare.laborator6.adapter.library.Movable;

/**
 * @author cvoinea
 */
public class MovableAdapterImpl implements MovableAdapter{

    private Movable car;

    public MovableAdapterImpl(Movable car) {
        this.car = car;
    }

    @Override
    public double getSpeed() {
        return convertFromMphToKmph(car.getSpeed());
    }

    private double convertFromMphToKmph(double speed) {
        return speed * 1.6;
    }
}
