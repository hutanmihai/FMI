package main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces;


import main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model.CoffeeCup;
import main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model.Cup;
import main.java.laboratoare.laborator5.interfaces.benefits.withoutinterfaces.model.TeaCup;

/**
 * @author cvoinea
 *
 * inheritance and polymorphism can be enough to model a small inheritance hierarchy
 * however, this wash() behaviour doesn't seem to belong to these classes, it is rather a capability ("can do" behaviour)
 *
 * What if we want other unrelated objects to exhibit this behaviour?  We could try to use an Object reference type --> see Cleaner.java
 */
public class VirtualCoffee {

    public static void prepareCup(Cup cup) {
        cup.wash();
    }

    public static void main(String[] args) {

        Cup cup = new Cup();
        prepareCup(cup);

        // dynamic polymorphism
        Cup coffeeCup = new CoffeeCup();
        prepareCup(coffeeCup);

        // dynamic polymorphism
        Cup teaCup = new TeaCup();
        prepareCup(teaCup);
    }


}
