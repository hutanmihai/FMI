package sample.view;

import sample.domain.Employee;
import sample.exceptions.CustomException;
import sample.service.EmployeeService;

import java.util.List;
import java.util.Scanner;

public class ClientApp {

    private final Scanner scanner = new Scanner(System.in);
    private final EmployeeService employeeService = new EmployeeService();

    public static void main(String[] args) {
        ClientApp clientApp = new ClientApp();
        while (true) {
            clientApp.showMenu();
            int option = clientApp.readOption();
            clientApp.execute(option);
        }
    }

    private void showMenu() {
        System.out.println("------------------------------------------------------------------------------");
        System.out.println("Welcome to Employee Management Platform (EMP)");
        System.out.println("What do you want to do?");
        System.out.println("1. add employee");
        System.out.println("2. show all employees");
        System.out.println("3. find employee by CNP");
        System.out.println("4. update employee details");
        System.out.println("5. remove employee");
        System.out.println("0. exit");
    }

    private void execute(int option) {
        switch (option) {
            case 1: {
                // add employee
                addEmployee();
                break;
            }
            case 2: {
                // list all employees
                listAllEmployees();
                break;
            }
            case 3: {
                // find employee by cnp
                findEmployeeById();
                break;
            }
            case 4: {
                // update employee details
                updateDetails();
                break;
            }
            case 5: {
                // remove employee
                removeEmployee();
                break;
            }
            case 0: {
                scanner.close();
                System.exit(0);
            }
        }
    }

    private void removeEmployee() {
        Employee employee = readEmployeeDetails();
        try {
            employeeService.removeEmployee(employee);
            System.out.println("Removed employee: " + employee);
        } catch (CustomException e) {
            System.out.println(e.getMessage());
        }
    }

    private void updateDetails() {
        Employee employee = readEmployeeDetails();
        try {
            employeeService.updateDetailsForEmployee(employee);
            System.out.println("Updated employee: " + employee);
        } catch (CustomException e) {
            System.out.println(e.getMessage());
        }
    }

    private void listAllEmployees() {
        System.out.println("Currently registered employees: ");
        List<Employee> employees = employeeService.getAllEmployees();
        if (employees.isEmpty()) {
            System.out.println("No employees registered yet!");
        } else {
            employees.forEach(System.out::println);
        }
    }

    private void addEmployee() {
        Employee employee = readEmployeeDetails();
        try {
            employeeService.registerNewEmployee(employee.getCnp(), employee.getFirstName(), employee.getLastName(), employee.getAge());
            System.out.println("Registered new employee: " + employee);
        } catch (CustomException customException) {
            System.out.println(customException.getMessage());
        }
    }

    private void findEmployeeById() {
        System.out.print("Employee CNP: ");
        String cnp = scanner.next();
        try {
            Employee employee = employeeService.getEmployeeByCnp(cnp);
            System.out.println("Found employee: " + employee);
        } catch (CustomException customException) {
            System.out.println(customException.getMessage());
        }
    }

    private Employee readEmployeeDetails() {
        System.out.print("Employee CNP: ");
        String cnp = scanner.next();
        System.out.print("Employee firstname: ");
        String firstName = scanner.next();
        System.out.print("Employee lastname: ");
        String lastName = scanner.next();
        System.out.println("Employee age: ");
        int age = readAge();
        return new Employee(cnp, firstName, lastName, age);
    }

    private int readAge() {
        int age = -1;
        do {
            try {
                age = readInt();
            } catch (CustomException exception) {
                System.out.println("Invalid input for employee age! Try again!");
            }
        } while (age < 0);
        return age;
    }

    private int readOption() {
        int option = -1;
        do {
            try {
                option = readInt();
            } catch (CustomException exception) {
                System.out.println("Invalid option! Try again!");
            }
        } while (option < 0 || option > 5);
        return option;
    }

    private int readInt() throws CustomException {
        String line = scanner.next();
        if (line.matches("^\\d+$")) {
            return Integer.parseInt(line);
        } else {
            throw new CustomException("Invalid number");
        }
    }
}
