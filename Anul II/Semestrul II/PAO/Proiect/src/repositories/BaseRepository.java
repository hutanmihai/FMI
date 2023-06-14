package repositories;

import database.DbConnection;

import java.sql.Connection;
import java.sql.SQLException;

public class BaseRepository {
    protected Connection db;

    public BaseRepository() {
        try {
            this.db = DbConnection.getSession();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }
    }
}
