package services;

import models.Soda;
import repositories.SodaRepository;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class SodaService {

    private final SodaRepository sodaRepository;

    private static final SodaService INSTANCE = new SodaService();

    private SodaService() {
        this.sodaRepository = new SodaRepository();
    }

    public static SodaService getInstance() {
        return INSTANCE;
    }

    public void addSoda(Scanner scanner) {
        Soda soda = buildSoda(scanner);
        sodaRepository.insert(soda);
    }

    public void deleteSoda(Integer id) {
        sodaRepository.delete(id);
    }

    public void updateSoda(Integer id, Scanner scanner) {
        Soda soda = buildSoda(scanner);
        sodaRepository.update(soda, id);
    }

    public Soda getSodaById(Integer id) {
        return sodaRepository.select(id);
    }

    public List<Soda> getAllSodas() {
        return sodaRepository.selectAll();
    }

    public Map<Integer, Soda> getAllSodasMap() {
        return sodaRepository.selectAllIdModel();
    }

    public Soda buildSoda(Scanner scanner) {

        System.out.println("Enter the soda's name: ");
        String name = scanner.nextLine();
        System.out.println("Enter the soda's description: ");
        String description = scanner.nextLine();
        System.out.println("Enter the soda's quantity: ");
        Integer quantity = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Enter the soda's price: ");
        Double price = scanner.nextDouble();
        scanner.nextLine();
        System.out.println("Enter the soda's brand: ");
        String brand = scanner.nextLine();
        System.out.println("Enter the soda's flavor: ");
        String flavor = scanner.nextLine();
        System.out.println("Enter the soda's volume: ");
        Double volume = scanner.nextDouble();
        scanner.nextLine();

        return new Soda(name, description, quantity, price, brand, flavor, volume);
    }

    public void updateSodaNoBuild(Soda soda, int id) {
        sodaRepository.update(soda, id);
        System.out.println("Soda updated successfully!");
    }
}
