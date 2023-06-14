package services;

import models.Theater;
import repositories.TheaterRepository;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class TheaterService {

    private TheaterRepository theaterRepository;

    private static final TheaterService INSTANCE = new TheaterService();

    private TheaterService() {
        this.theaterRepository = new TheaterRepository();
    }

    public static TheaterService getInstance() {
        return INSTANCE;
    }

    public void addTheater(Scanner scanner) {
        Theater theater = buildTheater(scanner);
        theaterRepository.insert(theater);
    }

    public void deleteTheater(Integer id) {
        theaterRepository.delete(id);
    }

    public void updateTheater(Integer id, Scanner scanner) {
        Theater theater = buildTheater(scanner);
        theaterRepository.update(theater, id);
    }

    public Theater getTheaterById(Integer id) {
        return theaterRepository.select(id);
    }

    public List<Theater> getAllTheaters() {
        return theaterRepository.selectAll();
    }

    public Map<Integer, Theater> getAllTheatersMap() {
        return theaterRepository.selectAllIdModel();
    }

    public Theater buildTheater(Scanner scanner) {
        System.out.println("Enter the theater's name: ");
        String name = scanner.nextLine();
        System.out.println("Enter the theater's capacity: ");
        Integer seats = scanner.nextInt();
        scanner.nextLine();

        return new Theater(name, seats);
    }
}
