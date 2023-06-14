package services;

import models.Employee;
import repositories.EmployeeRepository;

import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class EmployeeService {

    private EmployeeRepository employeeRepository;

    private static final EmployeeService INSTANCE = new EmployeeService();

    private EmployeeService() {
        this.employeeRepository = new EmployeeRepository();
    }

    public static EmployeeService getInstance() {
        return INSTANCE;
    }

    public void addEmployee(Scanner scanner) {
        Employee employee = buildEmployee(scanner);
        employeeRepository.insert(employee);
    }

    public void deleteEmployee(Integer id) {
        employeeRepository.delete(id);
    }

    public void updateEmployee(Integer id, Scanner scanner) {
        Employee employee = buildEmployee(scanner);
        employeeRepository.update(employee, id);
    }

    public Employee getEmployeeById(Integer id) {
        return employeeRepository.select(id);
    }

    public List<Employee> getAllEmployees() {
        return employeeRepository.selectAll();
    }

    public Map<Integer, Employee> getAllEmployeesMap() {
        return employeeRepository.selectAllIdModel();
    }

    public Employee buildEmployee(Scanner scanner) {
        System.out.println("Enter the employee's name: ");
        String name = scanner.nextLine();
        System.out.println("Enter the employee's email:");
        String email = scanner.nextLine();
        System.out.println("Enter the employee's phone number: ");
        String phone = scanner.nextLine();
        System.out.println("Enter the employee's position: ");
        String position = scanner.nextLine();
        System.out.println("Enter the employee's salary: ");
        Integer salary = scanner.nextInt();
        scanner.nextLine();

        return new Employee(name, email, phone, position, salary);
    }
}
