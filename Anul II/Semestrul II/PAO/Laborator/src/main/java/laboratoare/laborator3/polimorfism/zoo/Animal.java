package main.java.laboratoare.laborator3.polimorfism.zoo;

/**
 * @author cvoinea
 */
public abstract class Animal {

    private int nrIdentificare;
    private String nume;
    private int varsta;
    protected String tipHrana;
    protected String sunetSpecific;

    public Animal(String nume, int varsta) {
        nrIdentificare = hashCode();
        this.nume = nume;
        this.varsta = varsta;
    }

    public abstract void seHraneste();

    public abstract void scoateSunet();

    public void afiseazaDetalii() {
        System.out.println("Acesta este " + this);
    }

    @Override
    public String toString() {
        return "Animal din categoria " + this.getClass().getSuperclass().getSimpleName() +
                ", din specia " + this.getClass().getSimpleName() + "{" +
                "nume='" + nume + '\'' +
                ", varsta=" + varsta +
                ",nrIdentificare=" + nrIdentificare +
                '}';
    }

    public String getNume() {
        return nume;
    }
}
