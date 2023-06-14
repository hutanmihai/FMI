package src.main.java.laboratoare.laborator10.collection.list.arraylist;

import java.util.ArrayList;
import java.util.List;

/**
 * @author cvoinea
 *
 *  ArrayList = list implementation using a dynamically resizeable, uni-dimensional array
 *  it is ordered, but unsorted (can be sorted)
 *  can contain duplicate values
 *  use it for read-intensive ops ( O(1) complexity, elements are referred by exact index)
 *  O(n) complexity for finding, deleting, adding (at specified position) an element (and even adding at the end if current capacity is exceeded)
 *
 */
public class Ex1 {

    public static void main(String[] args) {

        int[] ints = new int[3]; // when using arrays, the size is predefined and cannot change
        ints[0] = 1;
        ints[1] = 2;
        ints[2] = 3;

        // without generics -> not a recommended use
        List bulkList = new ArrayList();
        bulkList.add(1);
        bulkList.add("another element");
        bulkList.add(new Object());
        System.out.println(bulkList);

        // no-argument constructor
        List<String> list1 = new ArrayList<>(); // implicit size is 10
        System.out.println(list1.isEmpty()); // true
        list1.add("1"); // add value "1" at the end
        list1.add("2");
        System.out.println(list1); // "1" "2"
        // add an element to a particular index
        list1.add(0, "3"); // "3" "1" "2"
        System.out.printf("list size is: %d", list1.size()); // 3
        // specified index must be <= list.size()
//        list1.add(4, "4"); // this throws IndexOutOfBoundsException
        list1.add(3, "5");

        if (list1.contains("2")) {
            // pay attention to overloaded method
            System.out.println(list1.remove(1)); // removes and returns the element at specified index
            System.out.println(list1.remove("2")); // removes specified element if present and returns boolean
            // throws exception
//			System.out.println(list1.remove(1));
        }
        System.out.println("list1: " + list1); // overrides toString

        //constructor accepting another collection as argument
        List<String> list2 = new ArrayList<>(list1);
        System.out.println("list2: " + list2);

        // add the content of another collection at the end
        list2.addAll(list1);
        System.out.println("after adding list1 elements at the end of list 2: " + list2);

        // add the content of another collection starting at a specific index
        list2.addAll(1, list1);
        list2.add("aaa");
        System.out.println(list2);

        // removes from list2 all the values also found in list1
        list2.removeAll(list1);
        System.out.println("list2 after removeAll: " + list2);

        // clears all the content, returns void
        list1.clear();
        System.out.println("list1 after clear: " + list1);
    }
}
