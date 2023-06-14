package sample.domain;

import java.time.LocalDate;
import java.util.Objects;

/**
 * @author cvoinea
 * <p>
 * This package should hold simple POJOs (Plain Old Java Objects)
 */
public class Employee {

    /**
     * private fields
     */
    private String cnp;
    private String firstName;
    private String lastName;
    private int age;
    private final LocalDate startDate = LocalDate.now();

    /**
     * public constructor
     */
    public Employee(String cnp, String firstName, String lastName, int age) {
        this.cnp = cnp;
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    /**
     * public getters and setters
     */
    public String getCnp() {
        return cnp;
    }

    public void setCnp(String cnp) {
        this.cnp = cnp;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public LocalDate getStartDate() {
        return startDate;
    }

    /**
     * override toString()
     */
    @Override
    public String toString() {
        return "Employee{" +
                "cnp='" + cnp + '\'' +
                ", firstName='" + firstName + '\'' +
                ", lastName='" + lastName + '\'' +
                ", age=" + age +
                ", startDate=" + startDate +
                '}';
    }

    /**
     * override equals() in order to define the important fields used to check objects equality in data
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Employee employee = (Employee) o;
        return cnp.equals(employee.cnp)
                && firstName.equals(employee.firstName)
                && lastName.equals(employee.lastName);
    }

    /**
     * override hashCode() in order to avoid using different hashCode for equal objects
     */
    @Override
    public int hashCode() {
        return Objects.hash(cnp, firstName, lastName);
    }
}
