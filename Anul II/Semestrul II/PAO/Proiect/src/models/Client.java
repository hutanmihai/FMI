package models;

import java.util.Objects;

public class Client extends Person {
    private String membership;

    private Integer loyaltyPoints;

    public Client() {
    }

    public Client(String name, String email, String phoneNumber, String membership, Integer loyaltyPoints) {
        super(name, email, phoneNumber);
        this.membership = membership;
        this.loyaltyPoints = loyaltyPoints;
    }

    public Client(Integer id, String name, String email, String phoneNumber, String membership, Integer loyaltyPoints) {
        super(id, name, email, phoneNumber);
        this.membership = membership;
        this.loyaltyPoints = loyaltyPoints;
    }

    public String getMembership() {
        return membership;
    }

    public void setMembership(String membership) {
        this.membership = membership;
    }

    public Integer getLoyaltyPoints() {
        return loyaltyPoints;
    }

    public void setLoyaltyPoints(Integer loyaltyPoints) {
        this.loyaltyPoints = loyaltyPoints;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Client client)) return false;
        return getMembership().equals(client.getMembership()) && getLoyaltyPoints().equals(client.getLoyaltyPoints());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getMembership(), getLoyaltyPoints());
    }

    @Override
    public String toString() {
        return
                "Name: " + this.getName() + "\n" +
                        "Email: " + this.getEmail() + "\n" +
                        "Phone number: " + this.getPhone() + "\n" +
                        "Membership: " + this.getMembership() + "\n" +
                        "Loyalty points: " + this.getLoyaltyPoints() + "\n";
    }
}
