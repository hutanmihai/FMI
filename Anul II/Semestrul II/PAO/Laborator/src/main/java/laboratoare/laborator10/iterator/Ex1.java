package src.main.java.laboratoare.laborator10.iterator;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * @author cvoinea
 */
public class Ex1 {

    public static void main(String[] args) {

        List<String> list = new ArrayList<>();
        list.add("abc");
        list.add("cd");
        list.add("cde");
        list.add("ee");

        for (String s : list) {
            System.out.println(s);
        }

        Iterator<String> iterator = list.iterator();
        while (iterator.hasNext()) {
            System.out.println(iterator.next());
        }

//        for (String s : list) {
//            if (s.length() % 2 == 0) {
//                list.remove(s); // ConcurrentModificationException
//            }
//        }

//        Iterator<String> iterator2 = list.iterator();
//        while (iterator2.hasNext()) {
//            String element = iterator2.next(); // throws ConcurrentModificationException
//			if (element.length() % 2 == 1) {
//                list.remove(element);  // cannot call remove on list
//            }
//        }

        System.out.println(list);
        Iterator<String> iterator3 = list.iterator();
        while (iterator3.hasNext()){
            String element = iterator3.next();
            if (element.length() % 2 == 0) {
                iterator3.remove();// can call remove on iterator
            }
        }
        System.out.println(list);

    }
}
