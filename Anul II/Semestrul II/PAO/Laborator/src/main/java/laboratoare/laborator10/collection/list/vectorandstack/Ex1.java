package src.main.java.laboratoare.laborator10.collection.list.vectorandstack;

import java.util.Stack;
import java.util.Vector;

/**
 * @author cvoinea
 *
 * Vector is thread-safe
 * Stack is a subclass of Vector
 */
public class Ex1 {

    public static void main(String[] args) {

        Vector<String> vector = new Vector<>();
        vector.add("aaa");
        vector.add("bbb");

        // own methods
        vector.addElement("ccc");
        System.out.println(vector.capacity()); // 10 = implicit
        System.out.println(vector.elementAt(1));
        System.out.println(vector.firstElement());


        // push, pop, peek, search
        Stack<String> stack = new Stack<>();
        stack.add("abc");
        stack.add("cde");
        stack.push("fff"); // calls addElement
        System.out.println(stack.peek()); //returns top element, calls elementAt, throws exception if empty stack
        System.out.println(stack.pop()); // removes top element and returns it
        System.out.println(stack);
        System.out.println(stack.search("cde"));
        System.out.println(stack.search("ccc")); // -1 if not found
    }
}
