package services;

import models.Movie;
import repositories.MovieRepository;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class MovieService {

    private MovieRepository movieRepository;

    private static final MovieService INSTANCE = new MovieService();

    private MovieService() {
        this.movieRepository = new MovieRepository();
    }

    public static MovieService getInstance() {
        return INSTANCE;
    }

    public void addMovie(Scanner scanner) {
        Movie movie = buildMovie(scanner);
        movieRepository.insert(movie);
    }

    public void deleteMovie(Integer id) {
        movieRepository.delete(id);
    }

    public void updateMovie(Integer id, Scanner scanner) {
        Movie movie = buildMovie(scanner);
        movieRepository.update(movie, id);
    }

    public Movie getMovieById(Integer id) {
        return movieRepository.select(id);
    }

    public List<Movie> getAllMovies() {
        return movieRepository.selectAll();
    }

    public Map<Integer, Movie> getAllMoviesMap() {
        return movieRepository.selectAllIdModel();
    }

    public Movie buildMovie(Scanner scanner) {
        System.out.println("Enter the movie's title: ");
        String title = scanner.nextLine();
        System.out.println("Enter the movie's genre: ");
        String genre = scanner.nextLine();
        System.out.println("Enter the movie's year: ");
        Integer year = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Enter the movie's duration in minutes: ");
        Integer duration = scanner.nextInt();
        scanner.nextLine();

        return new Movie(title, genre, year, duration);
    }
}
