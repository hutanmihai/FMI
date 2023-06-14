package main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model;

/**
 * @author cvoinea
 */
public class Cup extends WashableObject {

    private double volume;
    private String color;

    @Override
    public void wash() {
        System.out.println("washing a cup");
    }

    public double getVolume() {
        return volume;
    }

    public void setVolume(double volume) {
        this.volume = volume;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
}
