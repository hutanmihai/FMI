package models;

import java.util.Objects;

public class Theater extends BaseModel {
    private String name;
    private Integer numberOfSeats;

    public Theater() {
    }

    public Theater(String name, Integer numberOfSeats) {
        this.name = name;
        this.numberOfSeats = numberOfSeats;
    }

    public Theater(Integer id, String name, Integer numberOfSeats) {
        super(id);
        this.name = name;
        this.numberOfSeats = numberOfSeats;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Integer getNumberOfSeats() {
        return numberOfSeats;
    }

    public void setNumberrOfSeats(Integer nrOfSeats) {
        this.numberOfSeats = nrOfSeats;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Theater theater)) return false;
        return getName().equals(theater.getName()) && getNumberOfSeats().equals(theater.getNumberOfSeats());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getName(), getNumberOfSeats());
    }

    @Override
    public String toString() {
        return
                "Name: " + this.getName() + "\n" +
                        "Number of seats: " + this.getNumberOfSeats() + "\n";
    }
}
