package main.java.laboratoare.laborator5.comparableandcomparator;

import java.util.Comparator;

/**
 * @author cvoinea
 */
public class MovieNameLengthComparator implements Comparator<Movie> {

    @Override
    public int compare(Movie o1, Movie o2) {
        // descending by name length
        return o2.getName().length() - o1.getName().length();
    }
}
