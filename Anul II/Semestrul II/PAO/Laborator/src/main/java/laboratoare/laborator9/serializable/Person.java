package src.main.java.laboratoare.laborator9.serializable;

import java.io.Serializable;
import java.util.Objects;

/**
 * @author cvoinea
 *
 * marker interfaces (Cloneable, Serializable)
 * java.io.Serializable --> marker interface that classes must implement if they are to be serialized and deserialized
 *
 * if the parent class of a serialized subclass object is not serializable, inherited members are not serialized
 * in the previous scenario, in order to deserialize an object of a subclass, the superclass must have a no-args constructor available
 */
public class Person implements Serializable {

    private String name;
    private int age;

    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Person{" +
                "name='" + name + '\'' +
                ", age=" + age +
                '}';
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Person person = (Person) o;
        return age == person.age && Objects.equals(name, person.name);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, age);
    }
}
