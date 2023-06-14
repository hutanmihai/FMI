package repositories;

import models.Client;
import models.Employee;
import models.Showtime;
import models.Ticket;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TicketRepository extends BaseRepository implements GenericRepository<Ticket> {
    private final String insertSql = "INSERT INTO ticket (showtimeId, clientId, employeeId, price, seat) VALUES (?, ?, ?, ?, ?)";
    private final String updateSql = "UPDATE ticket SET showtimeId = ?, clientId = ?, employeeId = ?, price = ?, seat = ? WHERE id = ?";
    private final String selectSql = "SELECT * FROM ticket WHERE id = ?";
    private final String selectAllSql = "SELECT * FROM ticket";
    private final String deleteSql = "DELETE FROM ticket WHERE id = ?";

    public TicketRepository() {
    }

    private Integer getShowtimeId(Showtime showtime) {
        if (showtime == null) {
            return null;
        }
        return showtime.getId();
    }

    private Integer getClientId(Client client) {
        if (client == null) {
            return null;
        }
        return client.getId();
    }

    private Integer getEmployeeId(Employee employee) {
        if (employee == null) {
            return null;
        }
        return employee.getId();
    }


    public void insert(Ticket ticket) {
        try {
            PreparedStatement statement = db.prepareStatement(insertSql);
            statement.setInt(1, this.getShowtimeId(ticket.getShowtime()));
            statement.setInt(2, this.getClientId(ticket.getClient()));
            statement.setInt(3, this.getEmployeeId(ticket.getEmployee()));
            statement.setDouble(4, ticket.getPrice());
            statement.setInt(5, ticket.getSeat());
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


    public void update(Ticket ticket, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(updateSql);
            statement.setInt(1, this.getShowtimeId(ticket.getShowtime()));
            statement.setInt(2, this.getClientId(ticket.getClient()));
            statement.setInt(3, this.getEmployeeId(ticket.getEmployee()));
            statement.setDouble(4, ticket.getPrice());
            statement.setInt(5, ticket.getSeat());
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


    public Ticket select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(selectSql);
            statement.setInt(1, id);
            statement.executeQuery();
            ResultSet resultSet = statement.getResultSet();
            Ticket ticket = new Ticket();
            while (resultSet.next()) {
                ticket.setId(resultSet.getInt("id"));
                ticket.setShowtime(new ShowtimeRepository().select(resultSet.getInt("showtimeId")));
                ticket.setClient(new ClientRepository().select(resultSet.getInt("clientId")));
                ticket.setEmployee(new EmployeeRepository().select(resultSet.getInt("employeeId")));
                ticket.setPrice(resultSet.getDouble("price"));
                ticket.setSeat(resultSet.getInt("seat"));
            }
            return ticket;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


    public List<Ticket> selectAll() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            statement.executeQuery();
            ResultSet resultSet = statement.getResultSet();
            List<Ticket> tickets = new ArrayList<>();
            while (resultSet.next()) {
                Ticket ticket = new Ticket();
                ticket.setId(resultSet.getInt("id"));
                ticket.setShowtime(new ShowtimeRepository().select(resultSet.getInt("showtimeId")));
                ticket.setClient(new ClientRepository().select(resultSet.getInt("clientId")));
                ticket.setEmployee(new EmployeeRepository().select(resultSet.getInt("employeeId")));
                ticket.setPrice(resultSet.getDouble("price"));
                ticket.setSeat(resultSet.getInt("seat"));
                tickets.add(ticket);
            }
            return tickets;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void delete(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(deleteSql);
            statement.setInt(1, id);
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }


    public Map<Integer, Ticket> selectAllIdModel() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            statement.executeQuery();
            ResultSet resultSet = statement.getResultSet();
            Map<Integer, Ticket> tickets = new HashMap<>();
            while (resultSet.next()) {
                Ticket ticket = new Ticket();
                ticket.setId(resultSet.getInt("id"));
                ticket.setShowtime(new ShowtimeRepository().select(resultSet.getInt("showtimeId")));
                ticket.setClient(new ClientRepository().select(resultSet.getInt("clientId")));
                ticket.setEmployee(new EmployeeRepository().select(resultSet.getInt("employeeId")));
                ticket.setPrice(resultSet.getDouble("price"));
                ticket.setSeat(resultSet.getInt("seat"));
                tickets.put(ticket.getId(), ticket);
            }
            return tickets;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
