package repositories;

import models.Theater;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class TheaterRepository extends BaseRepository implements GenericRepository<Theater> {
    private final String insertSql = "INSERT INTO theater (name, numberofseats) VALUES (?, ?)";
    private final String updateSql = "UPDATE theater SET name = ?, numberofseats = ? WHERE id = ?";
    private final String selectSql = "SELECT * FROM theater WHERE id = ?";
    private final String selectAllSql = "SELECT * FROM theater";
    private final String deleteSql = "DELETE FROM theater WHERE id = ?";

    public TheaterRepository() {
    }

    public void insert(Theater theater) {
        try {
            PreparedStatement statement = db.prepareStatement(insertSql);
            statement.setString(1, theater.getName());
            statement.setInt(2, theater.getNumberOfSeats());
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Theater select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(selectSql);
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Theater(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getInt("numberofseats")
                );
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return null;
    }

    public void update(Theater theater, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(updateSql);
            statement.setString(1, theater.getName());
            statement.setInt(2, theater.getNumberOfSeats());
            statement.setInt(3, id);
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

    public List<Theater> selectAll() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            List<Theater> theaters = new ArrayList<>();
            while (resultSet.next()) {
                theaters.add(new Theater(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getInt("numberofseats")
                ));
            }
            return theaters;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Map<Integer, Theater> selectAllIdModel() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            Map<Integer, Theater> theaters = new HashMap<>();
            while (resultSet.next()) {
                theaters.put(resultSet.getInt("id"), new Theater(
                        resultSet.getString("name"),
                        resultSet.getInt("numberofseats")
                ));
            }
            return theaters;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
