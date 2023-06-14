package main.java.laboratoare.laborator4.asociere;

import java.util.Arrays;

/**
 * @author cvoinea
 */
public class Departament { // has-a

    private String nume;
    private Profesor[] profesori; // agregare

    public Departament(String nume, Profesor[] profesori) {
        this.nume = nume;
        this.profesori = profesori;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    public Profesor[] getProfesori() {
        return profesori;
    }

    public void setProfesori(Profesor[] profesori) {
        this.profesori = profesori;
    }

    @Override
    public String toString() {
        return "Departament{" +
                "nume='" + nume + '\'' +
                ", profesori=" + Arrays.toString(profesori) +
                '}';
    }
}
