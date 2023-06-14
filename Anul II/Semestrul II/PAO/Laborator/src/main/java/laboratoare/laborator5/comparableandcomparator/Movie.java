package main.java.laboratoare.laborator5.comparableandcomparator;


/**
 * @author cvoinea
 *
 * use Comparable interface when sorting in a natural order
 */
public class Movie implements Comparable<Movie>{

    private String name;
    private int year;
    private double rating;

    public Movie(String name, int year, double rating) {
        this.name = name;
        this.year = year;
        this.rating = rating;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public double getRating() {
        return rating;
    }

    public void setRating(double rating) {
        this.rating = rating;
    }

    @Override
    public String toString() {
        return "Movie{" +
                "name='" + name + '\'' +
                ", year=" + year +
                ", rating=" + rating +
                '}';
    }

    // this implementation must be consistent with equals() implementation
    @Override
    public int compareTo(Movie o) {
        return this.getYear() - o.getYear();
    }

    // same field used to determine if 2 Movie objects are equal
    @Override
    public boolean equals(Object obj) {
        if (obj instanceof Movie) {
            Movie movie = (Movie) obj;
            return this.getYear() == movie.getYear();
        }
        return false;
    }
}
