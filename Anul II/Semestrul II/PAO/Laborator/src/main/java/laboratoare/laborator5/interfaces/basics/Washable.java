package main.java.laboratoare.laborator5.interfaces.basics;

/**
 * @author cvoinea
 *
 * interfaces allow us to model multiple inheritance
 *            Washable
 *             ^  ^
 *            |    \
 *           |      \
 *      Soakable   Scrubbable
 *         ^        ^
 *          \      /
 *           \    /
 *        BubbleBathable
 */
public interface Washable {

    // IMPERVIOUS
    int IMPERVIOUS = 0;
    int RESISTANT = 1;
    int FRAGILE = 2;
    int EXPLOSIVE = 3;

    void wash();

    default boolean needsWashing() {
        System.out.println("by default, wash everything");
        return true;
    }
}
