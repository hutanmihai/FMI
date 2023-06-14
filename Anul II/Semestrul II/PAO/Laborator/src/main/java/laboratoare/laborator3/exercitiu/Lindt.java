package main.java.laboratoare.laborator3.exercitiu;

/**
 * @author cvoinea
 */
public class Lindt extends CandyBox {

    private float lungime;
    private float latime;
    private float inaltime;

    public Lindt() {
    }

    public Lindt(String flavor, String origin, float lungime, float latime, float inaltime) {
        super(flavor, origin);
        this.lungime = lungime;
        this.latime = latime;
        this.inaltime = inaltime;
    }

    @Override
    public float getVolume() {
        return lungime * latime * inaltime;
    }

    @Override
    public String toString() {
        //return "The " + origin + " " + flavor + "  has volume " + getVolume();
        return super.toString() + " has volume: " + getVolume();
    }
}
