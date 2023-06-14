package src.main.java.laboratoare.laborator11.lambda.ex1;

/**
 * @author cvoinea
 */
public class Main {

    public static void main(String[] args) {

        // interface reference, concrete implementation
        Instrument guitar = new Guitar();
        guitar.play();
        System.out.println("guitar object: " + guitar);

        // anonymous class
        Instrument piano = new Instrument() { // here starts the body of an anonymous class which implements Instrument interface
            // implement the abstract method inherited
            @Override
            public void play() {
                System.out.println("playing piano " + this);
            }
        };
        piano.play();

        // use lambda expression
        Instrument i1 = () -> System.out.println("new instrument playing"); // declare the implementation, but nothing is executed here yet
        i1.play(); // actual call to the above implementation

        Instrument i2 = () -> System.out.println("stop playing");
        i2.play();
    }
}
