package main.java.laboratoare.laborator4.imutabilitate;

import java.util.Objects;

/**
 * @author cvoinea
 */
public final class Client {

    private Adresa adresa;

    public Client(Adresa adresa) {
        this.adresa = new Adresa(adresa);
    }

    public Adresa getAdresa() {
        return adresa;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Client client = (Client) o;
        return Objects.equals(adresa, client.adresa);
    }

    @Override
    public int hashCode() {
        return Objects.hash(adresa);
    }

    @Override
    public String toString() {
        return "Client{" +
                "adresa=" + adresa +
                '}';
    }
}
