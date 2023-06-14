package src.main.java.laboratoare.laborator10.collection.list.linkedlist;
import java.util.LinkedList;

/**
 * @author cvoinea
 *
 * LinkedList is a List implementation using double-linked elements
 * every element is a node and it contains 2 references: to previous and next node
 *
 * O(n) complexity to search for an element
 * insertion, addition and removal of elements are faster than with arraylist
 *
 *
 * test Queue behavior of LinkedList
 *
 boolean offer(E var1);
 E poll();
 E element();
 E peek();
 *
 head - - - - tail
 */
public class Ex1 {

	public static void main(String[] args) {

		// creates an empty list
		LinkedList<String> list = new LinkedList<>();
		list.add("a");
		list.add("bb");

		// methods inherited from Queue

		// add element to tail, it calls add() underneath
		list.offer("ccc");
		System.out.println(list);

		// returns head element
		//underneath it calls getFirst from Deque, throws NoSuchElementException if list is empty
		System.out.println(list.element());

		// returns first element (head), null if list is empty
		System.out.println(list.peek());

		// removes first element (the current head)
		System.out.println(list.poll());
		System.out.println(list);

		// safe to use, returns null if list is empty
		System.out.println(new LinkedList<>().poll());


	}
}
