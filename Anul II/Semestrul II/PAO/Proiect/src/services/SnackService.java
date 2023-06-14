package services;

import models.Snack;
import repositories.SnackRepository;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class SnackService {

    private SnackRepository snackRepository;

    private static final SnackService INSTANCE = new SnackService();

    private SnackService() {
        this.snackRepository = new SnackRepository();
    }

    public static SnackService getInstance() {
        return INSTANCE;
    }

    public void addSnack(Scanner scanner) {
        Snack snack = buildSnack(scanner);
        snackRepository.insert(snack);
    }

    public void deleteSnack(Integer id) {
        snackRepository.delete(id);
    }

    public void updateSnack(Integer id, Scanner scanner) {
        Snack snack = buildSnack(scanner);
        snackRepository.update(snack, id);
    }

    public Snack getSnackById(Integer id) {
        return snackRepository.select(id);
    }

    public List<Snack> getAllSnacks() {
        return snackRepository.selectAll();
    }

    public Map<Integer, Snack> getAllSnacksMap() {
        return snackRepository.selectAllIdModel();
    }

    public Snack buildSnack(Scanner scanner) {
        System.out.println("Enter the snack's name: ");
        String name = scanner.nextLine();
        System.out.println("Enter the snack's description: ");
        String description = scanner.nextLine();
        System.out.println("Enter the snack's quantity: ");
        Integer quantity = scanner.nextInt();
        scanner.nextLine();
        System.out.println("Enter the snack's price: ");
        Double price = scanner.nextDouble();
        scanner.nextLine();
        System.out.println("Enter the snack's type: ");
        String type = scanner.nextLine();
        System.out.println("Enter the snack's size: ");
        String size = scanner.nextLine();

        return new Snack(name, description, quantity, price, type, size);
    }

    public void updateSnackNoBuild(Snack snack, int id) {
        snackRepository.update(snack, id);
        System.out.println("Snack updated successfully!");
    }
}
