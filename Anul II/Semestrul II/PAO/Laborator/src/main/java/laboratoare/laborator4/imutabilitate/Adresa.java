package main.java.laboratoare.laborator4.imutabilitate;

/**
 * @author cvoinea
 */
public class Adresa {

    private String strada;
    private int numar;

    public Adresa(String strada, int numar) {
        this.strada = strada;
        this.numar = numar;
    }

    public Adresa(Adresa adresa) {
        this.strada = adresa.getStrada();
        this.numar = adresa.getNumar();
    }

    public String getStrada() {
        return strada;
    }

    public void setStrada(String strada) {
        this.strada = strada;
    }

    public int getNumar() {
        return numar;
    }

    public void setNumar(int numar) {
        this.numar = numar;
    }

    @Override
    public String toString() {
        return "Adresa{" +
                "strada='" + strada + '\'' +
                ", numar=" + numar +
                '}';
    }
}
