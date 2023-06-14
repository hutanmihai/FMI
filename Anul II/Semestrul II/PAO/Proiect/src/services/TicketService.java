package services;

import models.Client;
import models.Employee;
import models.Showtime;
import models.Ticket;
import repositories.ClientRepository;
import repositories.EmployeeRepository;
import repositories.ShowtimeRepository;
import repositories.TicketRepository;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class TicketService {

    private TicketRepository ticketRepository;
    private ShowtimeRepository showtimeRepository;
    private ClientRepository clientRepository;
    private EmployeeRepository employeeRepository;

    private static final TicketService INSTANCE = new TicketService();

    private TicketService() {
        this.ticketRepository = new TicketRepository();
        this.showtimeRepository = new ShowtimeRepository();
        this.clientRepository = new ClientRepository();
        this.employeeRepository = new EmployeeRepository();
        this.showtimeRepository = new ShowtimeRepository();
    }

    public static TicketService getInstance() {
        return INSTANCE;
    }

    private static <K, V> String beautifyMap(Map<K, V> map) {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<K, V> entry : map.entrySet()) {
            sb.append(entry.getKey()).append(". ").append(entry.getValue().toString());
        }
        return sb.toString();
    }

    public void addTicket(Scanner scanner) {
        Ticket ticket = buildTicket(scanner);
        Showtime showtime = showtimeRepository.select(ticket.getShowtime().getId());
        List<Integer> seats = showtime.getSeats();
        if (seats.get(ticket.getSeat()) == 1) {
            System.out.println("Seat already taken!");
            return;
        }
        seats.set(ticket.getSeat(), 1);
        showtime.setSeats(seats);
        showtimeRepository.update(showtime, showtime.getId());
        ticketRepository.insert(ticket);
    }

    public void deleteTicket(Integer id) {
        ticketRepository.delete(id);
    }

    public void updateTicket(Integer id, Scanner scanner) {
        Ticket ticket = buildTicket(scanner);
        ticketRepository.update(ticket, id);
    }

    public Ticket getTicketById(Integer id) {
        return ticketRepository.select(id);
    }

    public List<Ticket> getAllTickets() {
        return ticketRepository.selectAll();
    }

    public Map<Integer, Ticket> getAllTicketsMap() {
        return ticketRepository.selectAllIdModel();
    }

    public Ticket buildTicket(Scanner scanner) {
        System.out.println("Would you like to use an existing showtime or create a new one? (existing/new)");
        String answer = scanner.nextLine();
        ShowtimeService showtimeService = ShowtimeService.getInstance();
        if (answer.equals("new")) {
            showtimeService.addShowtime(scanner);
        }
        System.out.println(beautifyMap(showtimeService.getAllShowtimesMap()));
        System.out.println("Enter the showtime id: ");
        Integer showtimeId = Integer.parseInt(scanner.nextLine());

        System.out.println("Would you like to use an existing client or create a new one? (existing/new)");
        answer = scanner.nextLine();
        ClientService clientService = ClientService.getInstance();
        if (answer.equals("new")) {
            clientService.createClient(scanner);
        }
        System.out.println(beautifyMap(clientService.getAllClientsMap()));
        System.out.println("Enter the client id: ");
        Integer clientId = Integer.parseInt(scanner.nextLine());

        System.out.println("Would you like to use an existing employee or create a new one? (existing/new)");
        answer = scanner.nextLine();
        EmployeeService employeeService = EmployeeService.getInstance();
        if (answer.equals("new")) {
            employeeService.addEmployee(scanner);
        }
        System.out.println(beautifyMap(employeeService.getAllEmployeesMap()));
        System.out.println("Enter the employee id: ");
        Integer employeeId = Integer.parseInt(scanner.nextLine());

        System.out.println("Enter the price: ");
        Double price = scanner.nextDouble();
        scanner.nextLine();

        System.out.println("Enter the seat number: ");
        Integer seatNumber = scanner.nextInt();
        scanner.nextLine();

        Showtime showtime = showtimeRepository.select(showtimeId);
        Client client = clientRepository.select(clientId);
        Employee employee = employeeRepository.select(employeeId);

        return new Ticket(showtime, client, employee, price, seatNumber);
    }
}
