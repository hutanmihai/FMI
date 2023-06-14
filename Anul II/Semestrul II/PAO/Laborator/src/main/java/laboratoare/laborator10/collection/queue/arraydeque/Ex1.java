package src.main.java.laboratoare.laborator10.collection.queue.arraydeque;

import java.util.ArrayDeque;

/**
 * @author cvoinea
 *
 * same methods as a Linkedlist, but on an array
 */
public class Ex1 {

    public static void main(String[] args) {

        ArrayDeque<String> arrayDeque = new ArrayDeque<>();
        arrayDeque.add("a");
        arrayDeque.addFirst("ff");
        arrayDeque.addLast("rr");

        arrayDeque.offer("55");
        arrayDeque.push("uuu");
        System.out.println(arrayDeque);

        System.out.println(arrayDeque.poll());
        System.out.println(arrayDeque);
    }
}
