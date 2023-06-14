package main.java.laboratoare.laborator3.exercitiu;

import java.util.Objects;

/**
 * @author cvoinea
 *
 * Creati o clasa CandyBox, care va conține câmpurile private flavor (String)
 * și origin (String). Clasa va avea, de asemenea:
 * - un constructor fără parametri;
 * - un constructor ce va inițializa toate campurile;
 * - o metoda de tip float getVolume(), care va intoarce valoarea 0.
 * Adaugati o metoda toString(), care va returna flavor-ul si regiunea de proveniență
 * a cutiei de bomboane.
 */
public class CandyBox {
     protected String flavor;
     protected String origin;

    public CandyBox() {
    }

    public CandyBox(String flavor, String origin) {
        this.flavor = flavor;
        this.origin = origin;

    }

    public float getVolume() {
        return 0;
    }

    @Override
    public String toString() {
        return this.getClass().getName() +
                " flavor: " + this.flavor +
                " origin: " + this.origin;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        CandyBox candyBox = (CandyBox) o;
        return Objects.equals(flavor, candyBox.flavor) && Objects.equals(origin, candyBox.origin);
    }

    @Override
    public int hashCode() {
        return Objects.hash(flavor, origin);
    }
}
