package repositories;

import models.Employee;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class EmployeeRepository extends BaseRepository implements GenericRepository<Employee> {

    private final String insertSql = "INSERT INTO employee (name, email, phone, position, salary) VALUES (?, ?, ?, ?, ?)";
    private final String updateSql = "UPDATE employee SET name = ?, email = ?, phone = ?, position = ?, salary = ? WHERE id = ?";
    private final String selectSql = "SELECT * FROM employee WHERE id = ?";
    private final String selectAllSql = "SELECT * FROM employee";
    private final String deleteSql = "DELETE FROM employee WHERE id = ?";

    public EmployeeRepository() {
    }

    public void insert(Employee employee) {
        try {
            PreparedStatement statement = db.prepareStatement(insertSql);
            statement.setString(1, employee.getName());
            statement.setString(2, employee.getEmail());
            statement.setString(3, employee.getPhone());
            statement.setString(4, employee.getPosition());
            statement.setInt(5, employee.getSalary());
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Employee select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(selectSql);
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Employee(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("email"),
                        resultSet.getString("phone"),
                        resultSet.getString("position"),
                        resultSet.getInt("salary")
                );
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return null;
    }

    public void update(Employee employee, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(updateSql);
            statement.setString(1, employee.getName());
            statement.setString(2, employee.getEmail());
            statement.setString(3, employee.getPhone());
            statement.setString(4, employee.getPosition());
            statement.setInt(5, employee.getSalary());
            statement.setInt(6, id);
            statement.executeUpdate();
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

    public List<Employee> selectAll() {
        List<Employee> employees = new ArrayList<>();
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                employees.add(new Employee(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("email"),
                        resultSet.getString("phone"),
                        resultSet.getString("position"),
                        resultSet.getInt("salary")
                ));
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return employees;
    }

    public Map<Integer, Employee> selectAllIdModel() {
        Map<Integer, Employee> employees = new HashMap<>();
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                employees.put(resultSet.getInt("id"), new Employee(
                        resultSet.getString("name"),
                        resultSet.getString("email"),
                        resultSet.getString("phone"),
                        resultSet.getString("position"),
                        resultSet.getInt("salary")
                ));
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return employees;
    }
}
