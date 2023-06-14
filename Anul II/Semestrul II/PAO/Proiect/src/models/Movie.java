package models;

import java.util.Objects;

public class Movie extends BaseModel {

    private String title;
    private String genre;
    private Integer year;
    private Integer duration;

    public Movie() {
    }

    public Movie(String title, String genre, Integer year, Integer duration) {
        this.title = title;
        this.genre = genre;
        this.year = year;
        this.duration = duration;
    }

    public Movie(Integer id, String title, String genre, Integer year, Integer duration) {
        super(id);
        this.title = title;
        this.genre = genre;
        this.year = year;
        this.duration = duration;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getGenre() {
        return genre;
    }

    public void setGenre(String genre) {
        this.genre = genre;
    }

    public Integer getYear() {
        return year;
    }

    public void setYear(Integer year) {
        this.year = year;
    }

    public Integer getDuration() {
        return duration;
    }

    public void setDuration(Integer duration) {
        this.duration = duration;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Movie movie)) return false;
        return getTitle().equals(movie.getTitle()) && getGenre().equals(movie.getGenre()) && getYear().equals(movie.getYear()) && getDuration().equals(movie.getDuration());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getTitle(), getGenre(), getYear(), getDuration());
    }

    @Override
    public String toString() {
        return
                "Title: " + this.getTitle() + "\n" +
                        "Genre: " + this.getGenre() + "\n" +
                        "Year: " + this.getYear() + "\n" +
                        "Duration: " + this.getDuration() + "\n";
    }
}
