package main.java.laboratoare.laborator5.comparableandcomparator;

import java.util.Comparator;

/**
 * @author cvoinea
 */
public class MovieRatingComparator implements Comparator<Movie> {

    @Override
    public int compare(Movie o1, Movie o2) {
        // ascending by rating
        return Double.compare(o1.getRating(), o2.getRating());
    }
}
