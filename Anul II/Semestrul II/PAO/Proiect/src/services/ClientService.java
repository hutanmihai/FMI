package services;

import models.Client;
import repositories.ClientRepository;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class ClientService {

    private ClientRepository clientRepository;

    private static final ClientService INSTANCE = new ClientService();

    private ClientService() {
        this.clientRepository = new ClientRepository();
    }

    public static ClientService getInstance() {
        return INSTANCE;
    }


    public List<Client> getAllClients() {
        return this.clientRepository.selectAll();
    }

    public Client getClientById(Integer id) {
        return this.clientRepository.select(id);
    }

    public void createClient(Scanner scanner) {
        Client client = buildClient(scanner);
        this.clientRepository.insert(client);
        System.out.println("Client created successfully!");
    }

    public void deleteClient(Integer id) {
        this.clientRepository.delete(id);
        System.out.println("Client deleted successfully!");
    }

    public void updateClient(Integer id, Scanner scanner) {
        Client client = buildClient(scanner);
        this.clientRepository.update(client, id);
        System.out.println("Client updated successfully!");
    }

    public Map<Integer, Client> getAllClientsMap() {
        return this.clientRepository.selectAllIdModel();
    }

    public Client buildClient(Scanner scanner) {
        System.out.println("Enter the client's name: ");
        String name = scanner.nextLine();
        System.out.println("Enter the client's email:");
        String email = scanner.nextLine();
        System.out.println("Enter the client's phone number: ");
        String phone = scanner.nextLine();
        System.out.println("Enter the client's membership: ");
        String membership = scanner.nextLine();
        System.out.println("Enter the client's loyalty points: ");
        Integer loyaltyPoints = scanner.nextInt();
        scanner.nextLine();

        return new Client(name, email, phone, membership, loyaltyPoints);
    }

    public void updateClientNoBuild(Client client, int id) {
        this.clientRepository.update(client, id);
        System.out.println("Client updated successfully!");
    }
}
