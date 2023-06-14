package sample.service;

import sample.domain.Employee;
import sample.exceptions.CustomException;
import sample.persistence.EmployeeRepository;

import java.util.List;
import java.util.Optional;

/**
 * @author cvoinea
 * <p>
 * Services expose the actions to support the application business.
 * Similar functionalities should be grouped in corresponding services.
 */
public class EmployeeService {

    /**
     * Services have a way of obtaining backing repositories.
     * One service can use multiple (or no) repositories.
     */
    private final EmployeeRepository employeeRepository = EmployeeRepository.getInstance();

    /**
     * Registers a new employee in the system.
     * Performs the validation on cnp, firstName and lastName fields
     *
     * @param cnp       national identification number
     * @param firstName employee's first name
     * @param lastName  employee's last name
     * @param age       employee's age
     * @return the employee object
     * @throws CustomException if particular validations fail
     */
    public Employee registerNewEmployee(String cnp, String firstName, String lastName, int age) throws CustomException {
        if (cnp == null || cnp.length() != 13 || cnp.chars().anyMatch(asciiCode -> (asciiCode < 48 || asciiCode > 57))) {
            throw new CustomException("Invalid national identification number: " + cnp);
        }
        if (firstName == null || firstName.isEmpty()) {
            throw new CustomException("Invalid employee firstname: " + firstName);
        }
        if (lastName == null || lastName.isEmpty()) {
            throw new CustomException("Invalid employee lastname: " + lastName);
        }
        if (age <= 18 || age >= 70) {
            throw new CustomException("Invalid employee age: " + age);
        }
        Employee employee = new Employee(cnp, firstName, lastName, age);
        return employeeRepository.save(employee);
    }

    /**
     * Returns a list of existing employees
     *
     * @return the list of existing employees
     */
    public List<Employee> getAllEmployees() {
        return employeeRepository.findAll();
    }

    /**
     * Returns an employee based on his cnp
     *
     * @param cnp the national identification number for an employee
     * @return the employee associated with the provided cnp
     * @throws CustomException if no employees associated to this cnp
     */
    public Employee getEmployeeByCnp(String cnp) throws CustomException {
        Optional<Employee> employee = employeeRepository.findById(cnp);
        return employee.orElseThrow(() -> new CustomException("Cannot find an employee having the provided cnp: " + cnp));
    }

    /**
     * Updates the details for an existing employee
     *
     * @param employee the entity to update
     * @throws CustomException if the provided employee entity does not exist
     */
    public void updateDetailsForEmployee(Employee employee) throws CustomException {
        employeeRepository.findById(employee.getCnp())
                .orElseThrow(() -> new CustomException("Cannot update provided entity: " + employee + " It does not exist!"));
        employeeRepository.update(employee);
    }

    /**
     * Removes an existing employee
     *
     * @param employee the entity to remove
     * @throws CustomException if the provided entity does not exist
     */
    public void removeEmployee(Employee employee) throws CustomException {
        employeeRepository.findById(employee.getCnp())
                .orElseThrow(() -> new CustomException("Cannot delete the provided entity: " + employee + " It does not exist!"));
        employeeRepository.delete(employee);
    }
}
