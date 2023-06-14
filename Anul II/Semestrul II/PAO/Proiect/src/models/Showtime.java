package models;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Showtime extends BaseModel implements Comparable<Showtime>{
    private Theater theater;
    private Movie movie;
    private LocalDate showingDate;
    private List<Integer> seats;

    public Showtime() {
    }

    public Showtime(Theater theater, Movie movie, LocalDate showingDate) {
        this.theater = theater;
        this.movie = movie;
        this.showingDate = showingDate;
        this.seats = new ArrayList<>();
        for (int i = 0; i < theater.getNumberOfSeats(); i++) {
            this.seats.add(0);
        }
    }

    public Showtime(Integer id, Theater theater, Movie movie, LocalDate showingDate) {
        super(id);
        this.theater = theater;
        this.movie = movie;
        this.showingDate = showingDate;
        this.seats = new ArrayList<>();
        for (int i = 0; i < theater.getNumberOfSeats(); i++) {
            this.seats.add(0);
        }
    }

    public Theater getTheater() {
        return theater;
    }

    public void setTheater(Theater theater) {
        this.theater = theater;
    }

    public Movie getMovie() {
        return movie;
    }

    public void setMovie(Movie movie) {
        this.movie = movie;
    }

    public LocalDate getShowingDate() {
        return showingDate;
    }

    public void setShowingDate(LocalDate showingDate) {
        this.showingDate = showingDate;
    }

    public List<Integer> getSeats() {
        return seats;
    }

    public void setSeats(List<Integer> seats) {
        this.seats = seats;
    }

    public void occupySeat(Integer seatNumber) {
        this.seats.set(seatNumber, 1);
    }

    public void freeSeat(Integer seatNumber) {
        this.seats.set(seatNumber, 0);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Showtime showtime)) return false;
        return getTheater().equals(showtime.getTheater()) && getMovie().equals(showtime.getMovie()) && getShowingDate().equals(showtime.getShowingDate()) && getSeats().equals(showtime.getSeats());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getTheater(), getMovie(), getShowingDate(), getSeats());
    }

    @Override
    public String toString() {
        return
                "Theater: " + this.getTheater().getName() + "\n" +
                        "Movie: " + this.getMovie().getTitle() + "\n" +
                        "Showing date: " + this.getShowingDate() + "\n" +
                        "Seats: " + this.getSeats() + "\n";
    }

    @Override
    public int compareTo(Showtime showtime) {
        return this.getShowingDate().compareTo(showtime.getShowingDate());
    }
}
