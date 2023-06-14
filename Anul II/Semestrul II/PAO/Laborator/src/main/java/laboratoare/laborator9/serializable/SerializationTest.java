package src.main.java.laboratoare.laborator9.serializable;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.time.LocalDateTime;

/**
 * @author cvoinea
 *
 * NotSerializableException is thrown if the object being serialized/deserialized contains references to other objects not declared Serializable
 *
 * many Java projects serialize Java objects using different mechanisms, other than the Java serialization mechanism
 * e.g., Java objects are serialized into JSON, BSON (binary encoded JSON) or other more optimized binary formats
 * advantage - the objects are also readable by non-Java applications (JavaScript running in a web browser
 *              can natively serialize and deserialize objects to and from JSON)
 *
 * JSON APIs: Jackson, GSON, JSON.org, JSONP
 */
public class SerializationTest {

    private static final String BASE_PATH = "src/main/java/laboratoare/laborator9/serializable";

    public static void main(String[] args) {

        // test serialization/ deserialization on Person class
        Person p1 = new Person("John", 20);
        System.out.println("person before serialization: " + p1);

        serializePerson(p1, "p1");

        Person p2 = deserializePerson("p1");
        System.out.println("deserialized object: " + p2);
        System.out.println("is same Person object: " + p1.equals(p2));

        // test serialization/ deserialization for Student subclass
        Address a1 = new Address("Maniu", 33);
        Student s1 = new Student("student 1", 20, 232, new int[]{8, 9, 10}, a1);
        System.out.println("student before serialization: " + s1);

        serializePerson(s1, "s1");
        // change static/instance fields on the initial Student instance
        // static fields are not serialized, therefore this new value is reflected in the object after deserialization
        Student.setFaculty("abc");
        // serializable instance fields will be overwritten at deserialization
        s1.setCurrentTime(LocalDateTime.now());
        s1.setAddress(new Address("Victoriei", 22));
        System.out.println("student after changing some attributes: " + s1);

        s1 = (Student) deserializePerson("s1");
        // only the static field gets changed since it was NOT serialized
        System.out.println("deserialized student: " + s1);
    }

    private static void serializePerson(Person person, String destinationFileName) {
        try (FileOutputStream fileOutputStream = new FileOutputStream(new File(BASE_PATH, destinationFileName));
                ObjectOutputStream objectOutputStream = new ObjectOutputStream(fileOutputStream)){
            objectOutputStream.writeObject(person);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static Person deserializePerson(String sourceFileName) {
        try (FileInputStream fileInputStream = new FileInputStream(new File(BASE_PATH, sourceFileName));
             ObjectInputStream objectInputStream = new ObjectInputStream(fileInputStream)){
            return (Person) objectInputStream.readObject();

        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
            throw new RuntimeException(e.getCause());
        }

    }

}
