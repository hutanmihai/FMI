package models;

import java.util.Objects;

public class Ticket extends BaseModel implements Comparable<Ticket>{
    private Showtime showtime;
    private Client client;
    private Employee employee;
    private Double price;
    private Integer seat;

    public Ticket() {
    }

    public Ticket(Showtime showtime, Client client, Employee employee, Double price, Integer seat) {
        this.showtime = showtime;
        this.client = client;
        this.employee = employee;
        this.price = price;
        this.seat = seat;
    }

    public Ticket(Integer id, Showtime showtime, Client client, Employee employee, Double price, Integer seat) {
        super(id);
        this.showtime = showtime;
        this.client = client;
        this.employee = employee;
        this.price = price;
        this.seat = seat;
    }

    public Showtime getShowtime() {
        return showtime;
    }

    public void setShowtime(Showtime showtime) {
        this.showtime = showtime;
    }

    public Client getClient() {
        return client;
    }

    public void setClient(Client client) {
        this.client = client;
    }

    public Employee getEmployee() {
        return employee;
    }

    public void setEmployee(Employee employee) {
        this.employee = employee;
    }

    public Double getPrice() {
        return price;
    }

    public void setPrice(Double price) {
        this.price = price;
    }

    public Integer getSeat() {
        return seat;
    }

    public void setSeat(Integer seat) {
        this.seat = seat;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Ticket ticket)) return false;
        return getShowtime().equals(ticket.getShowtime()) && getClient().equals(ticket.getClient()) && getEmployee().equals(ticket.getEmployee()) && getPrice().equals(ticket.getPrice()) && getSeat().equals(ticket.getSeat());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getShowtime(), getClient(), getEmployee(), getPrice(), getSeat());
    }

    @Override
    public String toString() {
        return
                "Showtime: \n" +
                        "Movie: " + this.getShowtime().getMovie() + "\n" +
                        "Theater: " + this.getShowtime().getTheater() + "\n" +
                        "Date: " + this.getShowtime().getShowingDate() + "\n" +
                        "Client: " + this.getClient().getName() + "\n" +
                        "Employee: " + this.getEmployee().getName() + "\n" +
                        "Price: " + this.getPrice() + "\n" +
                        "Seat: " + this.getSeat() + "\n";
    }

    @Override
    public int compareTo(Ticket o) {
        return this.getShowtime().compareTo(o.getShowtime());
    }
}
