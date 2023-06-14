package main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces;


import main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model.Car;
import main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model.CoffeeCup;
import main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model.Cup;
import main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model.Dog;
import main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model.Window;

/**
 * @author cvoinea
 *
 * make all individual types implement the desired behaviour wash() and pass the references as Object type
 *
 * in this case, the code proves to have multipe problems: reasons to change if adding/removing supported types, inefficient and extensive 'if' logic etc.
 *                                                          => poor design
 */
public class Cleaner {

    // when not using a common supertype
    public static void cleanObject(Object object) {
        if (object instanceof Car) {
            Car car = (Car) object;
            car.wash();
        } else if (object instanceof Window window) {  // pattern variable since Java 14
            window.wash();
        } else if (object instanceof Cup cup) {
            //Cup cup = (Cup) object;
            cup.wash();
        } else if (object instanceof Dog) {
            Dog dog = (Dog) object;
            dog.wash();
        } else {
            System.out.println("unsupported object type"); // must treat all exceptional cases
        }
    }

    public static void main(String[] args) {
        Dog dog = new Dog();
        cleanObject(dog);

        Window window = new Window();
        cleanObject(window);

        Car car = new Car();
        cleanObject(car);

        Cup cup = new CoffeeCup();
        cleanObject(cup);

        String unknownType = "unknown type";
        cleanObject(unknownType);
    }
}
