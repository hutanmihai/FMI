package main.java.laboratoare.laborator3.polimorfism.zoo;

/**
 * @author cvoinea
 */
public class Zoo {

    private final int nrMaxAnimale;
    Animal[] animaleZoo;
    private int indexCurent;

    public Zoo(int nrMaxAnimale) {
        if (nrMaxAnimale > 0) {
            this.nrMaxAnimale = nrMaxAnimale;
            this.animaleZoo = new Animal[nrMaxAnimale];
        } else {
            throw new RuntimeException("Nu ati introdus un nr intreg pozitiv");
        }
    }

    public void adaugaAnimal(Animal animal) {
        if (indexCurent < animaleZoo.length) {
            animaleZoo[indexCurent] = animal;
            System.out.println("Adaugat animal " + animal.getClass().getSimpleName() + " la pozitia " + indexCurent++);
        }
    }


}
