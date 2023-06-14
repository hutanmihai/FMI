package main.java.laboratoare.laborator6.adapter.library;

/**
 * @author cvoinea
 */
public class ABritishCar implements Movable {

    private double speedInMph;

    public ABritishCar(double speedInMph) {
        this.speedInMph = speedInMph;
    }

    @Override
    public double getSpeed() {
        return speedInMph; // in mph
    }
}
