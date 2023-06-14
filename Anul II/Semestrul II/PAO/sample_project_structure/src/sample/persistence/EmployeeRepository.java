package sample.persistence;

import sample.domain.Employee;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;

import static sample.persistence.util.DatabaseConnectionUtils.getDatabaseConnection;

/**
 * @author cvoinea
 * <p>
 * Repositories define an elegant method for storing, updating, and extracting the data stored from JAVA applications.
 * Usually they have a 1-to-1 relation with the entities. Any entity that should be persisted should have a repository
 *
 *
 * CRUD -> create read update delete
 */
public class EmployeeRepository implements GenericRepository<Employee> {

    private final Map<String, Employee> storage = new HashMap<>();
    private static final String INSERT_EMPLOYEE_SQL = "INSERT INTO employee (cnp, first_name, last_name, age) VALUES (?, ?, ?, ?)";

    private final Connection connection;

    private static volatile EmployeeRepository instance;

    private EmployeeRepository() {
        this.connection = getDatabaseConnection();
    }

    public static EmployeeRepository getInstance() {
        if (instance == null) {
            synchronized (EmployeeRepository.class) {
                if (instance == null) {
                    instance = new EmployeeRepository();
                }
            }
        }
        return instance;
    }

    @Override
    public Employee save(Employee entity) {
        storage.put(entity.getCnp(), entity);

        try {
            PreparedStatement preparedStatement = connection.prepareStatement(INSERT_EMPLOYEE_SQL);
            preparedStatement.setString(1, entity.getCnp());
            preparedStatement.setString(2, entity.getFirstName());
            preparedStatement.setString(3, entity.getLastName());
            preparedStatement.setInt(4, entity.getAge());
            preparedStatement.execute();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        return entity;
    }

    @Override
    public List<Employee> findAll() {
        return new ArrayList<>(storage.values());
    }

    @Override
    public Optional<Employee> findById(String id) {
        return Optional.ofNullable(storage.get(id));
    }

    @Override
    public void update(Employee entity) {
        storage.put(entity.getCnp(), entity);
    }

    @Override
    public void delete(Employee entity) {
        storage.remove(entity.getCnp());
    }
}
