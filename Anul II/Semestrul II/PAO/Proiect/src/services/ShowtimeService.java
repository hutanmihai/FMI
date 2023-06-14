package services;

import models.Movie;
import models.Showtime;
import models.Theater;
import repositories.MovieRepository;
import repositories.ShowtimeRepository;
import repositories.TheaterRepository;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class ShowtimeService {
    private ShowtimeRepository showtimeRepository;
    private TheaterRepository theaterRepository;
    private MovieRepository movieRepository;

    private static final ShowtimeService INSTANCE = new ShowtimeService();

    private ShowtimeService() {
        this.showtimeRepository = new ShowtimeRepository();
        this.theaterRepository = new TheaterRepository();
        this.movieRepository = new MovieRepository();
    }

    public static ShowtimeService getInstance() {
        return INSTANCE;
    }

    private static <K, V> String beautifyMap(Map<K, V> map) {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<K, V> entry : map.entrySet()) {
            sb.append(entry.getKey()).append(". ").append(entry.getValue().toString());
        }
        return sb.toString();
    }

    public void addShowtime(Scanner scanner) {
        Showtime showtime = buildShowtime(scanner);
        showtimeRepository.insert(showtime);
    }

    public void deleteShowtime(Integer id) {
        showtimeRepository.delete(id);
    }

    public void updateShowtime(Integer id, Scanner scanner) {
        Showtime showtime = buildShowtime(scanner);
        showtimeRepository.update(showtime, id);
    }

    public Showtime getShowtimeById(Integer id) {
        return showtimeRepository.select(id);
    }

    public List<Showtime> getAllShowtimes() {
        return showtimeRepository.selectAll();
    }

    public Map<Integer, Showtime> getAllShowtimesMap() {
        return showtimeRepository.selectAllIdModel();
    }

    public Showtime buildShowtime(Scanner scanner) {

        System.out.println("Would you like to use an existing theater or create a new one? (existing/new)");
        String answer = scanner.nextLine();
        TheaterService theaterService = TheaterService.getInstance();
        if (answer.equals("new")) {
            theaterService.addTheater(scanner);
        }
        System.out.println(beautifyMap(theaterService.getAllTheatersMap()));
        System.out.println("Enter the theater's id: ");
        int theaterId = scanner.nextInt();
        scanner.nextLine();

        System.out.println("Would you like to use an existing movie or create a new one? (existing/new)");
        answer = scanner.nextLine();
        MovieService movieService = MovieService.getInstance();
        if (answer.equals("new")) {
            movieService.addMovie(scanner);
        }
        System.out.println(beautifyMap(movieService.getAllMoviesMap()));
        System.out.println("Enter the movie's id: ");
        int movieId = scanner.nextInt();
        scanner.nextLine();

        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        System.out.println("Enter the date (dd/MM/yyyy): ");
        String date = scanner.nextLine();
        LocalDate localDate = LocalDate.parse(date, formatter);

        Theater theater = theaterRepository.select(theaterId);
        Movie movie = movieRepository.select(movieId);

        return new Showtime(theater, movie, localDate);
    }
}
