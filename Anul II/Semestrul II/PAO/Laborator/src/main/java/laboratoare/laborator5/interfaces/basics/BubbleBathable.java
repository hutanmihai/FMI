package main.java.laboratoare.laborator5.interfaces.basics;

/**
 * @author cvoinea
 *
 * interfaces allow us to model multiple inheritance
 *          Washable
 *           ^  ^
 *          |    \
 *         |      \
 *    Soakable   Scrubbable
 *       ^        ^
 *        \      /
 *         \    /
 *      BubbleBathable
 */
public interface BubbleBathable extends Soakable, Scrubbable {

    void takeBubbleBath();
}
