package main.java.laboratoare.laborator5.comparableandcomparator;

import java.util.Arrays;
import java.util.Comparator;

/**
 * @author cvoinea
 */
public class MovieTest {

    public static void main(String[] args) {

        Movie[] movies = {new Movie("Breaking bad", 2014, 9.3),
                new Movie("Die hard", 1990, 8),
                new Movie("Star wars", 1977, 8.8),
                new Movie("Planet of the apes", 1976, 8),
                new Movie("Terminator", 1994, 7.5)
        };

        System.out.println("Before sorting: ");
        System.out.println(Arrays.toString(movies));
        System.out.println("After sorting: ");
        // sort the array using the order provided by implementing Comparable interface
        Arrays.sort(movies);
        System.out.println(Arrays.toString(movies));

        // sort the array by using a movie rating comparator
        System.out.println("Ascending by rating: ");
        Arrays.sort(movies, new MovieRatingComparator());
        System.out.println(Arrays.toString(movies));

        // sort the array by using a movie name length comparator
        System.out.println("Descending by name length: ");
        Arrays.sort(movies, new MovieNameLengthComparator());
        System.out.println(Arrays.toString(movies));

        /*
         * chain comparators: first sort ascending by rating (but reversed -> so descending), then descending by name length
         *
         * it makes a good example here for extending interfaces functionality in Java 8
         */
        Arrays.sort(movies, new MovieRatingComparator().reversed().thenComparing(new MovieNameLengthComparator()));
        System.out.println("Sort by rating desc, then by name length desc: ");
        System.out.println(Arrays.toString(movies));

        // same order as with Comparable implementation, but this time defining a Comparator reference inline
        Comparator<Movie> yearComparator = (Movie movie1, Movie movie2) -> movie1.getYear() - movie2.getYear(); // it actually specifies the abstract method implementation (compare)
        Arrays.sort(movies, yearComparator); // callback mechanism
        System.out.println("Ascending by year using inline comparator");
        System.out.println(Arrays.toString(movies));

        // same thing as above, but directly using an anonymous comparator
        Arrays.sort(movies, (movie1, movie2) -> movie1.getYear() - movie2.getYear()); // callback mechanism
        System.out.println("Ascending by year using inline comparator");
        System.out.println(Arrays.toString(movies));
    }
}
