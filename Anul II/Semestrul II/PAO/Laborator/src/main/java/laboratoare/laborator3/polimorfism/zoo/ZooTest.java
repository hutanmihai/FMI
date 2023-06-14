package main.java.laboratoare.laborator3.polimorfism.zoo;

import main.java.laboratoare.laborator3.polimorfism.zoo.carnivor.Leu;
import main.java.laboratoare.laborator3.polimorfism.zoo.carnivor.Pisica;
import main.java.laboratoare.laborator3.polimorfism.zoo.ierbivor.Cal;
import main.java.laboratoare.laborator3.polimorfism.zoo.ierbivor.Elefant;
import main.java.laboratoare.laborator3.polimorfism.zoo.omnivor.Caine;
import main.java.laboratoare.laborator3.polimorfism.zoo.omnivor.Urs;

import java.util.Scanner;

/**
 * @author cvoinea
 * <p>
 * java.lang - importat default
 */
public class ZooTest {

    public static void main(String[] args) {

        // mod alternativ de citire valoare ca argument pentru main
//        int nrAnimaleZoo = Integer.parseInt(args[0]);
//        System.out.println(nrAnimaleZoo);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Precizati nr max de animale ce pot fi gazduite la zoo: ");
        int nrAnimaleZoo = scanner.nextInt();
        scanner.close();

        Zoo zooBucuresti = new Zoo(nrAnimaleZoo);
        adaugaAnimaleLaZoo(zooBucuresti);
        for (int i = 0; (i < zooBucuresti.animaleZoo.length) && (zooBucuresti.animaleZoo[i] != null); i++) {
            Animal animal = zooBucuresti.animaleZoo[i];
            animal.afiseazaDetalii();
            animal.seHraneste();
            animal.scoateSunet();
        }

        // demo folosire equals
        Pisica pisica = new Pisica("Tom", 2);
        Pisica pisica1 = new Pisica("Tom", 2);
        System.out.println(pisica == pisica1);
        System.out.println(pisica.equals(pisica1));
    }

    public static void adaugaAnimaleLaZoo(Zoo zoo) {
        Leu leu = new Leu("Simba", 7);
        zoo.adaugaAnimal(leu);
        Elefant elefant = new Elefant("Eli", 10);
        zoo.adaugaAnimal(elefant);
        Urs urs = new Urs("Fram", 4);
        zoo.adaugaAnimal(urs);
        Pisica pisica = new Pisica("Tom", 2);
        zoo.adaugaAnimal(pisica);
        Caine caine = new Caine("Toto", 3);
        zoo.adaugaAnimal(caine);
        Cal cal = new Cal("Thunder", 3);
        zoo.adaugaAnimal(cal);
    }

}
