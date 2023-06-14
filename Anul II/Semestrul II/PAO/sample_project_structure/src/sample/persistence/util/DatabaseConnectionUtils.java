package sample.persistence.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

/**
 * @author cvoinea
 */
public class DatabaseConnectionUtils {

    private static final String MYSQL_JDBC_DRIVER = "com.mysql.cj.jdbc.Driver";
    private static final String DB_URL = "jdbc:mysql://localhost/laborator10";
    private static final String USERNAME = "root";
    private static final String PASSWORD = "root";


    private Connection connection;

    private static volatile DatabaseConnectionUtils instance;

    private DatabaseConnectionUtils() {
        try {
            Class.forName(MYSQL_JDBC_DRIVER);
            connection = DriverManager.getConnection(DB_URL, USERNAME, PASSWORD);
        } catch (ClassNotFoundException e) {
            System.out.println("MySQL driver not available: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("Could not connect to database: " + e.getMessage());
        }
        System.out.println("MySQL connection available");
    }


    public static Connection getDatabaseConnection() {
        if (instance == null) {
            synchronized (DatabaseConnectionUtils.class) {
                if (instance == null) {
                    instance = new DatabaseConnectionUtils();
                }
            }
        }
        return instance.connection;
    }


}
