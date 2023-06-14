package main.java.laboratoare.laborator4.asociere;

import java.util.Arrays;

/**
 * @author cvoinea
 */
public class Universitate { //has-to-have-a

    private String nume;
    private Departament[] departamente; // compozitie

    public Universitate(String nume, Departament[] departamente) {
        this.nume = nume;
        this.departamente = Arrays.copyOf(departamente, departamente.length); // copie a obiectului referentiat in parametru
    }

    @Override
    public String toString() {
        return "Universitate{" +
                "nume='" + nume + '\'' +
                ", departamente=" + Arrays.toString(departamente) +
                '}';
    }
}
