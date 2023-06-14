package src.main.java.laboratoare.laborator9.serializable;

import java.io.Serializable;

/**
 * @author cvoinea
 */
public class Address implements Serializable {

    private String streetName;
    private int number;


    public Address(String streetName, int number) {
        this.streetName = streetName;
        this.number = number;
    }

    public String getStreetName() {
        return streetName;
    }

    public void setStreetName(String streetName) {
        this.streetName = streetName;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    @Override
    public String toString() {
        return "Address{" +
                "streetName='" + streetName + '\'' +
                ", number=" + number +
                '}';
    }
}
