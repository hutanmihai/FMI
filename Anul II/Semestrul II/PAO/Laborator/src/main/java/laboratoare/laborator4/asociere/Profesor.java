package main.java.laboratoare.laborator4.asociere;

/**
 * @author cvoinea
 */
public class Profesor {

    private int id;
    private String nume;

    public Profesor(int id, String nume) {
        this.id = id;
        this.nume = nume;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNume() {
        return nume;
    }

    public void setNume(String nume) {
        this.nume = nume;
    }

    @Override
    public String toString() {
        return "Profesor{" +
                "id=" + id +
                ", nume='" + nume + '\'' +
                '}';
    }
}
