package database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class DbConnection {
    private static Connection connection;

    private static final String URL = "jdbc:postgresql://localhost:5441/postgres";

    private static final String userName = "postgres";

    private static final String password = "postgres";

    private DbConnection() {
    }

    public static Connection getSession() throws SQLException {
        if (connection == null) {
            connection = DriverManager.getConnection(URL, userName, password);
        }
        return connection;
    }
}
