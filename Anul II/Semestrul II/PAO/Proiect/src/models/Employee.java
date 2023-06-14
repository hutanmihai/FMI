package models;

import java.util.Objects;

public class Employee extends Person {

    private String position;
    private Integer salary;

    public Employee() {
    }

    public Employee(String name, String email, String phoneNumber, String position, Integer salary) {
        super(name, email, phoneNumber);
        this.position = position;
        this.salary = salary;
    }

    public Employee(Integer id, String name, String email, String phoneNumber, String position, Integer salary) {
        super(id, name, email, phoneNumber);
        this.position = position;
        this.salary = salary;
    }

    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }

    public Integer getSalary() {
        return salary;
    }

    public void setSalary(Integer salary) {
        this.salary = salary;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (!(o instanceof Employee employee)) return false;
        return getPosition().equals(employee.getPosition()) && getSalary().equals(employee.getSalary());
    }

    @Override
    public int hashCode() {
        return Objects.hash(getPosition(), getSalary());
    }

    @Override
    public String toString() {
        return
                "Name: " + this.getName() + "\n" +
                        "Email: " + this.getEmail() + "\n" +
                        "Phone number: " + this.getPhone() + "\n" +
                        "Position: " + this.getPosition() + "\n" +
                        "Salary: " + this.getSalary() + "\n";
    }
}
