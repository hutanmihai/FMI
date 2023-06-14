package main;

import models.*;
import services.*;

import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.*;

public class Main {

    private static <K, V> String beautifyMap(Map<K, V> map) {
        StringBuilder sb = new StringBuilder();
        for (Map.Entry<K, V> entry : map.entrySet()) {
            sb.append(entry.getKey()).append(". ").append(entry.getValue().toString());
        }
        return sb.toString();
    }

    private static <T> String beautifyList(List<T> list) {
        StringBuilder sb = new StringBuilder();
        for (T t : list) {
            sb.append(t.toString()).append("\n");
        }
        return sb.toString();
    }

    public static void main(String[] args) throws IOException, NoSuchMethodException {

        Scanner scanner = new Scanner(System.in);

        ClientService clientService = ClientService.getInstance();
        EmployeeService employeeService = EmployeeService.getInstance();
        TheaterService theaterService = TheaterService.getInstance();
        MovieService movieService = MovieService.getInstance();
        TicketService ticketService = TicketService.getInstance();
        SodaService sodaService = SodaService.getInstance();
        SnackService snackService = SnackService.getInstance();
        ShowtimeService showtimeService = ShowtimeService.getInstance();
        CSVService csvService = CSVService.getInstance();

        Map<Integer, Client> clients = clientService.getAllClientsMap();
        Map<Integer, Employee> employees = employeeService.getAllEmployeesMap();
        Map<Integer, Theater> theaters = theaterService.getAllTheatersMap();
        Map<Integer, Movie> movies = movieService.getAllMoviesMap();
        Map<Integer, Soda> sodas = sodaService.getAllSodasMap();
        Map<Integer, Snack> snacks = snackService.getAllSnacksMap();
        Map<Integer, Showtime> showtimes = showtimeService.getAllShowtimesMap();
        Map<Integer, Ticket> tickets = ticketService.getAllTicketsMap();

        List<Showtime> showtimesList = showtimeService.getAllShowtimes();
        List<Ticket> ticketsList = ticketService.getAllTickets();

        System.out.println("Welcome to the Cinema Management System!");

        while (true) {
            System.out.println();
            System.out.println();
            System.out.println("------------------------------------");
            System.out.println("------------------------------------");
            System.out.println("MAIN DASHBOARD");
            System.out.println();
            System.out.println("0. Exit");
            System.out.println("1. Create Menu");
            System.out.println("2. Read Menu");
            System.out.println("3. Update Menu");
            System.out.println("4. Delete Menu");
            System.out.println("5. Special Menu");
            System.out.println();
            System.out.println("Choose an option: ");

            int option = scanner.nextInt();
            scanner.nextLine();

            switch (option) {
                case 0 -> {
                    System.out.println("Exiting...");
                    csvService.close();
                    System.exit(0);
                }
                case 1 -> {
                    int optionCreate = 1;
                    while (optionCreate != 0) {
                        System.out.println();
                        System.out.println();
                        System.out.println("------------------------------------");
                        System.out.println("------------------------------------");
                        System.out.println("CREATE MENU");
                        System.out.println();
                        System.out.println("0. Back");
                        System.out.println("1. Create Client");
                        System.out.println("2. Create Employee");
                        System.out.println("3. Create Theater");
                        System.out.println("4. Create Movie");
                        System.out.println("5. Create Ticket");
                        System.out.println("6. Create Showtime");
                        System.out.println("7. Create Soda");
                        System.out.println("8. Create Snack");
                        System.out.println();
                        System.out.println("Choose an option: ");

                        optionCreate = scanner.nextInt();
                        scanner.nextLine();

                        switch (optionCreate) {
                            case 0 -> System.out.println("Going back to MAIN MENU...");
                            case 1 -> {
                                clientService.createClient(scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                clients = clientService.getAllClientsMap();
                                csvService.addLine("Create Client");
                            }
                            case 2 -> {
                                employeeService.addEmployee(scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                employees = employeeService.getAllEmployeesMap();
                                csvService.addLine("Create Employee");
                            }
                            case 3 -> {
                                theaterService.addTheater(scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                theaters = theaterService.getAllTheatersMap();
                                csvService.addLine("Create Theater");
                            }
                            case 4 -> {
                                movieService.addMovie(scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                movies = movieService.getAllMoviesMap();
                                csvService.addLine("Create Movie");
                            }
                            case 5 -> {
                                ticketService.addTicket(scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                tickets = ticketService.getAllTicketsMap();
                                ticketsList = ticketService.getAllTickets();
                                showtimes = showtimeService.getAllShowtimesMap();
                                showtimesList = showtimeService.getAllShowtimes();
                                csvService.addLine("Create Ticket");
                            }
                            case 6 -> {
                                showtimeService.addShowtime(scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                showtimes = showtimeService.getAllShowtimesMap();
                                showtimesList = showtimeService.getAllShowtimes();
                                csvService.addLine("Create Showtime");
                            }
                            case 7 -> {
                                sodaService.addSoda(scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                sodas = sodaService.getAllSodasMap();
                                csvService.addLine("Create Soda");
                            }
                            case 8 -> {
                                snackService.addSnack(scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                snacks = snackService.getAllSnacksMap();
                                csvService.addLine("Create Snack");
                            }
                            default -> {
                                System.out.println("Invalid option!");
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                            }
                        }
                    }
                }
                case 2 -> {
                    int optionRead = 1;
                    while (optionRead != 0) {
                        System.out.println();
                        System.out.println();
                        System.out.println("------------------------------------");
                        System.out.println("------------------------------------");
                        System.out.println("READ MENU");
                        System.out.println();
                        System.out.println("0. Back");
                        System.out.println("1. Read All Clients");
                        System.out.println("2. Read All Employees");
                        System.out.println("3. Read All Theaters");
                        System.out.println("4. Read All Movies");
                        System.out.println("5. Read All Tickets");
                        System.out.println("6. Read All Showtimes");
                        System.out.println("7. Read All Sodas");
                        System.out.println("8. Read All Snacks");
                        System.out.println();
                        System.out.println("Choose an option: ");

                        optionRead = scanner.nextInt();
                        scanner.nextLine();

                        switch (optionRead) {
                            case 0 -> System.out.println("Going back to MAIN MENU...");
                            case 1 -> {
                                clients = clientService.getAllClientsMap();
                                if (clients.isEmpty()) {
                                    System.out.println("There are no clients in the database!");
                                } else {
                                    System.out.println(beautifyMap(clients));
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Read All Clients");
                            }
                            case 2 -> {
                                employees = employeeService.getAllEmployeesMap();
                                if (employees.isEmpty()) {
                                    System.out.println("There are no employees in the database!");
                                } else {
                                    System.out.println(beautifyMap(employees));
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Read All Employees");
                            }
                            case 3 -> {
                                theaters = theaterService.getAllTheatersMap();
                                if (theaters.isEmpty()) {
                                    System.out.println("There are no theaters in the database!");
                                } else {
                                    System.out.println(beautifyMap(theaters));
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Read All Theaters");
                            }
                            case 4 -> {
                                movies = movieService.getAllMoviesMap();
                                if (movies.isEmpty()) {
                                    System.out.println("There are no movies in the database!");
                                } else {
                                    System.out.println(beautifyMap(movies));
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Read All Movies");
                            }
                            case 5 -> {
                                tickets = ticketService.getAllTicketsMap();
                                if (tickets.isEmpty()) {
                                    System.out.println("There are no tickets in the database!");
                                } else {
                                    System.out.println(beautifyMap(tickets));
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Read All Tickets");
                            }
                            case 6 -> {
                                showtimes = showtimeService.getAllShowtimesMap();
                                if (showtimes.isEmpty()) {
                                    System.out.println("There are no showtimes in the database!");
                                } else {
                                    System.out.println(beautifyMap(showtimes));
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Read All Showtimes");
                            }
                            case 7 -> {
                                sodas = sodaService.getAllSodasMap();
                                if (sodas.isEmpty()) {
                                    System.out.println("There are no sodas in the database!");
                                } else {
                                    System.out.println(beautifyMap(sodas));
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Read All Sodas");
                            }
                            case 8 -> {
                                snacks = snackService.getAllSnacksMap();
                                if (snacks.isEmpty()) {
                                    System.out.println("There are no snacks in the database!");
                                } else {
                                    System.out.println(beautifyMap(snacks));
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Read All Snacks");
                            }
                            default -> {
                                System.out.println("Invalid option!");
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                            }
                        }
                    }
                }
                case 3 -> {
                    int optionUpdate = 1;
                    while (optionUpdate != 0) {
                        System.out.println();
                        System.out.println();
                        System.out.println("------------------------------------");
                        System.out.println("------------------------------------");
                        System.out.println("UPDATE MENU");
                        System.out.println();
                        System.out.println("0. Back");
                        System.out.println("1. Update Client");
                        System.out.println("2. Update Employee");
                        System.out.println("3. Update Theater");
                        System.out.println("4. Update Movie");
                        System.out.println("5. Update Ticket");
                        System.out.println("6. Update Showtime");
                        System.out.println("7. Update Soda");
                        System.out.println("8. Update Snack");
                        System.out.println();
                        System.out.println("Choose an option: ");

                        optionUpdate = scanner.nextInt();
                        scanner.nextLine();

                        switch (optionUpdate) {
                            case 0:
                                System.out.println("Going back to MAIN MENU...");
                                break;
                            case 1:
                                if (clients.isEmpty()) {
                                    System.out.println("There are no clients in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(clientService.getAllClients());
                                System.out.println("Choose the client you want to update (id): ");
                                int id = scanner.nextInt();
                                scanner.nextLine();
                                clientService.updateClient(id, scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                clients = clientService.getAllClientsMap();
                                csvService.addLine("Update Client");
                                break;
                            case 2:
                                if (employees.isEmpty()) {
                                    System.out.println("There are no employees in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(employeeService.getAllEmployees());
                                System.out.println("Choose the employee you want to update (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                employeeService.updateEmployee(id, scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                employees = employeeService.getAllEmployeesMap();
                                csvService.addLine("Update Employee");
                                break;
                            case 3:
                                if (theaters.isEmpty()) {
                                    System.out.println("There are no theaters in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(theaterService.getAllTheaters());
                                System.out.println("Choose the theater you want to update (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                theaterService.updateTheater(id, scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                theaters = theaterService.getAllTheatersMap();
                                csvService.addLine("Update Theater");
                                break;
                            case 4:
                                if (movies.isEmpty()) {
                                    System.out.println("There are no movies in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(movieService.getAllMovies());
                                System.out.println("Choose the movie you want to update (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                movieService.updateMovie(id, scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                movies = movieService.getAllMoviesMap();
                                csvService.addLine("Update Movie");
                                break;
                            case 5:
                                if (tickets.isEmpty()) {
                                    System.out.println("There are no tickets in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(ticketService.getAllTickets());
                                System.out.println("Choose the ticket you want to update (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                ticketService.updateTicket(id, scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                tickets = ticketService.getAllTicketsMap();
                                ticketsList = ticketService.getAllTickets();
                                csvService.addLine("Update Ticket");
                                break;
                            case 6:
                                if (showtimes.isEmpty()) {
                                    System.out.println("There are no showtimes in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(showtimeService.getAllShowtimes());
                                System.out.println("Choose the showtime you want to update (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                showtimeService.updateShowtime(id, scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                showtimes = showtimeService.getAllShowtimesMap();
                                showtimesList = showtimeService.getAllShowtimes();
                                csvService.addLine("Update Showtime");
                                break;
                            case 7:
                                if (sodas.isEmpty()) {
                                    System.out.println("There are no sodas in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(sodaService.getAllSodas());
                                System.out.println("Choose the soda you want to update (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                sodaService.updateSoda(id, scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                sodas = sodaService.getAllSodasMap();
                                csvService.addLine("Update Soda");
                                break;
                            case 8:
                                if (snacks.isEmpty()) {
                                    System.out.println("There are no snacks in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(snackService.getAllSnacks());
                                System.out.println("Choose the snack you want to update (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                snackService.updateSnack(id, scanner);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                snacks = snackService.getAllSnacksMap();
                                csvService.addLine("Update Snack");
                                break;
                            default: {
                                System.out.println("Invalid option!");
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                break;
                            }
                        }
                    }
                }
                case 4 -> {
                    int optionDelete = 1;
                    while (optionDelete != 0) {
                        System.out.println();
                        System.out.println();
                        System.out.println("------------------------------------");
                        System.out.println("------------------------------------");
                        System.out.println("DELETE MENU");
                        System.out.println();
                        System.out.println("0. Back");
                        System.out.println("1. Delete Client");
                        System.out.println("2. Delete Employee");
                        System.out.println("3. Delete Theater");
                        System.out.println("4. Delete Movie");
                        System.out.println("5. Delete Ticket");
                        System.out.println("6. Delete Showtime");
                        System.out.println("7. Delete Soda");
                        System.out.println("8. Delete Snack");
                        System.out.println();
                        System.out.println("Choose an option: ");

                        optionDelete = scanner.nextInt();
                        scanner.nextLine();

                        switch (optionDelete) {
                            case 0:
                                System.out.println("Going back to MAIN MENU...");
                                break;
                            case 1:
                                if (clients.isEmpty()) {
                                    System.out.println("There are no clients in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(clientService.getAllClients());
                                System.out.println("Choose the client you want to delete (id): ");
                                int id = scanner.nextInt();
                                scanner.nextLine();
                                clientService.deleteClient(id);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                clients = clientService.getAllClientsMap();
                                csvService.addLine("Delete Client");
                                break;
                            case 2:
                                if (employees.isEmpty()) {
                                    System.out.println("There are no employees in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(employeeService.getAllEmployees());
                                System.out.println("Choose the employee you want to delete (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                employeeService.deleteEmployee(id);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                employees = employeeService.getAllEmployeesMap();
                                csvService.addLine("Delete Employee");
                                break;
                            case 3:
                                if (theaters.isEmpty()) {
                                    System.out.println("There are no theaters in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(theaterService.getAllTheaters());
                                System.out.println("Choose the theater you want to delete (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                theaterService.deleteTheater(id);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                theaters = theaterService.getAllTheatersMap();
                                csvService.addLine("Delete Theater");
                                break;
                            case 4:
                                if (movies.isEmpty()) {
                                    System.out.println("There are no movies in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(movieService.getAllMovies());
                                System.out.println("Choose the movie you want to delete (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                movieService.deleteMovie(id);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                movies = movieService.getAllMoviesMap();
                                csvService.addLine("Delete Movie");
                                break;
                            case 5:
                                if (tickets.isEmpty()) {
                                    System.out.println("There are no tickets in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(ticketService.getAllTickets());
                                System.out.println("Choose the ticket you want to delete (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                ticketService.deleteTicket(id);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                tickets = ticketService.getAllTicketsMap();
                                ticketsList = ticketService.getAllTickets();
                                csvService.addLine("Delete Ticket");
                                break;
                            case 6:
                                if (showtimes.isEmpty()) {
                                    System.out.println("There are no showtimes in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(showtimeService.getAllShowtimes());
                                System.out.println("Choose the showtime you want to delete (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                showtimeService.deleteShowtime(id);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                showtimes = showtimeService.getAllShowtimesMap();
                                showtimesList = showtimeService.getAllShowtimes();
                                csvService.addLine("Delete Showtime");
                                break;
                            case 7:
                                if (sodas.isEmpty()) {
                                    System.out.println("There are no sodas in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(sodaService.getAllSodas());
                                System.out.println("Choose the soda you want to delete (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                sodaService.deleteSoda(id);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                sodas = sodaService.getAllSodasMap();
                                csvService.addLine("Delete Soda");
                                break;
                            case 8:
                                if (snacks.isEmpty()) {
                                    System.out.println("There are no snacks in the database!");
                                    System.out.println("Press enter to continue...");
                                    scanner.nextLine();
                                    break;
                                }
                                System.out.println(snackService.getAllSnacks());
                                System.out.println("Choose the snack you want to delete (id): ");
                                id = scanner.nextInt();
                                scanner.nextLine();
                                snackService.deleteSnack(id);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                snacks = snackService.getAllSnacksMap();
                                csvService.addLine("Delete Snack");
                                break;
                            default:
                                System.out.println("Invalid option!");
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                break;
                        }
                    }
                }
                case 5 -> {
                    int specialOption = 1;
                    while (specialOption != 0) {
                        System.out.println();
                        System.out.println();
                        System.out.println("------------------------------------");
                        System.out.println("------------------------------------");
                        System.out.println("SPECIAL MENU");
                        System.out.println();
                        System.out.println("0. Back");
                        System.out.println("1. Show all showtimes sorted by date");
                        System.out.println("2. Show all tickets sorted by their showtimes");
                        System.out.println("3. Show all showtimes for a movie");
                        System.out.println("4. Show how many seats are available for a showtime");
                        System.out.println("5. View how many tickets a user has bought");
                        System.out.println("6. Check if a Movie is available in any Theater and show them");
                        System.out.println("7. Update a client's email and/or phone number");
                        System.out.println("8. Change quantity of existing products");
                        System.out.println("9. Show all Movies that are available in a Theater");
                        System.out.println("10. Show all Movies that are available in a Theater on a specific date");

                        specialOption = scanner.nextInt();
                        scanner.nextLine();

                        switch (specialOption) {
                            case 0 -> {
                                System.out.println("Going back to MAIN MENU...");
                            }
                            case 1 -> {
                                System.out.println(showtimesList);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                List<Showtime> sortedShowtimes = showtimeService.getAllShowtimes();
                                sortedShowtimes.sort(Comparator.comparing(Showtime::getShowingDate));
                                System.out.println(sortedShowtimes);
                                csvService.addLine("Show all showtimes sorted by date");
                            }
                            case 2 -> {
                                System.out.println(ticketsList);
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                List<Ticket> sortedTickets = ticketService.getAllTickets();
                                sortedTickets.sort(Comparator.comparing(Ticket::getShowtime));
                                System.out.println(sortedTickets);
                                csvService.addLine("Show all tickets sorted by their showtimes");
                            }
                            case 3 -> {
                                System.out.println(beautifyMap(movies));
                                System.out.println("Choose the movie you want to see the showtimes for (id): ");
                                int id = scanner.nextInt();
                                scanner.nextLine();
                                for (Showtime showtime : showtimesList) {
                                    if (showtime.getMovie().getId() == id) {
                                        System.out.println(showtime);
                                    }
                                }
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Show all showtimes for a movie");
                            }
                            case 4 -> {
                                System.out.println(beautifyMap(showtimes));
                                System.out.println("Choose the showtime you want to see the available seats for (id): ");
                                int id = scanner.nextInt();
                                scanner.nextLine();

                                Showtime showtime = showtimes.get(id);

                                List<Integer> showtimeSeats = showtime.getSeats();
                                List<Integer> indexes = new ArrayList<>();
                                for (int i = 0; i < showtimeSeats.size(); i++) {
                                    if (showtimeSeats.get(i) == 0) {
                                        indexes.add(i);
                                    }
                                }
                                Integer[] indexArray = indexes.toArray(new Integer[indexes.size()]);

                                System.out.println("The showtime with id " + id + " has " + indexArray.length + " available seats!");
                                System.out.println("The available seats are: " + Arrays.toString(indexArray));

                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Show how many seats are available for a showtime");
                            }
                            case 5 -> {
                                System.out.println(beautifyMap(clients));
                                System.out.println("Choose the client you want to see the number of tickets for (id): ");
                                int id = scanner.nextInt();
                                scanner.nextLine();

                                int counter = 0;

                                for (Ticket ticket : ticketsList) {
                                    if (ticket.getClient().getId() == id) {
                                        counter++;
                                    }
                                }

                                System.out.println("The client with id " + id + " has bought " + counter + " tickets!");
                                System.out.println("Press enter to continue...");

                                scanner.nextLine();
                                csvService.addLine("View how many tickets a user has bought");
                            }
                            case 6 -> {
                                System.out.println(beautifyMap(movies));
                                System.out.println("Choose the movie you want to see the theaters for (id): ");
                                int id = scanner.nextInt();
                                scanner.nextLine();

                                List<Theater> uniqueTheaters = new ArrayList<>();

                                for (Showtime showtime : showtimesList) {
                                    if (showtime.getMovie().getId() == id) {
                                        if (!uniqueTheaters.contains(showtime.getTheater())) {
                                            uniqueTheaters.add(showtime.getTheater());
                                        }
                                    }
                                }
                                System.out.println("The movie with id " + id + " is available in the following theaters: ");
                                System.out.println(beautifyList(uniqueTheaters));
                                System.out.println("Press enter to continue...");
                                scanner.nextLine();
                                csvService.addLine("Check if a Movie is available in any Theater and show them");
                            }
                            case 7 -> {
                                System.out.println(beautifyMap(clients));
                                System.out.println("Choose the client you want to update (id): ");
                                int id = scanner.nextInt();
                                scanner.nextLine();

                                System.out.println("Choose what you want to update: ");
                                System.out.println("1. Phone number");
                                System.out.println("2. Email");
                                System.out.println("3. Both");

                                int updateOption = scanner.nextInt();
                                scanner.nextLine();

                                Client client = clients.get(id);

                                switch (updateOption) {
                                    case 1 -> {
                                        System.out.println("Enter the new phone number: ");
                                        String phoneNumber = scanner.nextLine();
                                        client.setPhone(phoneNumber);
                                        clientService.updateClientNoBuild(client, id);
                                    }
                                    case 2 -> {
                                        System.out.println("Enter the new email: ");
                                        String email = scanner.nextLine();
                                        client.setEmail(email);
                                        clientService.updateClientNoBuild(client, id);
                                    }
                                    case 3 -> {
                                        System.out.println("Enter the new phone number: ");
                                        String phoneNumber = scanner.nextLine();
                                        System.out.println("Enter the new email: ");
                                        String email = scanner.nextLine();

                                        client.setPhone(phoneNumber);
                                        client.setEmail(email);

                                        clientService.updateClientNoBuild(client, id);
                                    }
                                    default -> {
                                        System.out.println("Invalid option!");
                                    }
                                }
                                clients = clientService.getAllClientsMap();
                                csvService.addLine("Update a client's email and/or phone number");
                            }
                            case 8 -> {
                                System.out.println("Choose what type of product you want to update: ");
                                System.out.println("1. Snack");
                                System.out.println("2. Soda");

                                int productType = scanner.nextInt();
                                scanner.nextLine();

                                switch (productType) {
                                    case 1 -> {
                                        System.out.println(beautifyMap(snacks));
                                        System.out.println("Choose the snack you want to update (id): ");
                                        int id = scanner.nextInt();
                                        scanner.nextLine();

                                        System.out.println("Enter the new quantity: ");
                                        int quantity = scanner.nextInt();
                                        scanner.nextLine();

                                        Snack snack = snacks.get(id);
                                        snack.setQuantity(quantity);

                                        snackService.updateSnackNoBuild(snack, id);
                                        snacks = snackService.getAllSnacksMap();
                                    }
                                    case 2 -> {
                                        System.out.println(beautifyMap(sodas));
                                        System.out.println("Choose the soda you want to update (id): ");
                                        int id = scanner.nextInt();
                                        scanner.nextLine();

                                        System.out.println("Enter the new quantity: ");
                                        int quantity = scanner.nextInt();
                                        scanner.nextLine();

                                        Soda soda = sodas.get(id);
                                        soda.setQuantity(quantity);

                                        sodaService.updateSodaNoBuild(soda, id);
                                        sodas = sodaService.getAllSodasMap();
                                    }
                                    default -> {
                                        System.out.println("Invalid option!");
                                    }
                                }
                                csvService.addLine("Change quantity of existing products");
                            }
                            case 9 -> {
                                System.out.println(beautifyMap(movies));
                                System.out.println("Choose the theater you want to see all movies for: ");
                                int id = scanner.nextInt();
                                scanner.nextLine();
                                List<Movie> uniqueMovies = new ArrayList<>();
                                Theater theater = theaters.get(id);
                                for (Showtime showtime : showtimesList) {
                                    if (showtime.getTheater().getId() == id) {
                                        if (!uniqueMovies.contains(showtime.getMovie())) {
                                            uniqueMovies.add(showtime.getMovie());
                                        }
                                    }
                                }
                                System.out.println("The following movies are available in the " + theater.getName() + " theater: ");
                                System.out.println(beautifyList(uniqueMovies));
                                csvService.addLine("Show all Movies that are available in a Theater");
                            }
                            case 10 -> {
                                System.out.println(beautifyMap(theaters));
                                System.out.println("Choose the theater you want to see all movies for: ");
                                int id = scanner.nextInt();
                                scanner.nextLine();
                                System.out.println("Type the date you want to see all movies for (dd/MM/yyyy): ");
                                LocalDate date = LocalDate.parse(scanner.nextLine(), DateTimeFormatter.ofPattern("dd/MM/yyyy"));

                                List<Movie> uniqueMovies = new ArrayList<>();

                                for (Showtime showtime : showtimesList) {
                                    if (showtime.getTheater().getId() == id && showtime.getShowingDate().equals(date)) {
                                        if (!uniqueMovies.contains(showtime.getMovie())) {
                                            uniqueMovies.add(showtime.getMovie());
                                        }
                                    }
                                }
                                System.out.println("The following movies are available in the " + theaters.get(id).getName() + " theater on " + date + ": ");
                                System.out.println(beautifyList(uniqueMovies));
                                csvService.addLine("Show all Movies that are available in a Theater on a specific date");
                            }
                            default -> {
                                System.out.println("Invalid option!");
                                scanner.nextLine();
                            }
                        }
                    }
                }
                default -> {
                    System.out.println("Invalid option!");
                }
            }
        }
    }
}
