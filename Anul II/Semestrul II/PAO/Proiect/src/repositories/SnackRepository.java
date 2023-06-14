package repositories;

import models.Snack;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SnackRepository extends BaseRepository implements GenericRepository<Snack> {
    private final String insertSql = "INSERT INTO snack (name, description, quantity, price, type, size) VALUES (?, ?, ?, ?, ?, ?)";
    private final String updateSql = "UPDATE snack SET name = ?, description = ?, quantity = ?, price = ?, type = ?, size = ? WHERE id = ?";
    private final String selectSql = "SELECT * FROM snack WHERE id = ?";
    private final String selectAllSql = "SELECT * FROM snack";
    private final String deleteSql = "DELETE FROM snack WHERE id = ?";

    public SnackRepository() {
    }

    public void insert(Snack snack) {
        try {
            PreparedStatement statement = db.prepareStatement(insertSql);
            statement.setString(1, snack.getName());
            statement.setString(2, snack.getDescription());
            statement.setInt(3, snack.getQuantity());
            statement.setDouble(4, snack.getPrice());
            statement.setString(5, snack.getType());
            statement.setString(6, snack.getSize());
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Snack select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(selectSql);
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Snack(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("description"),
                        resultSet.getInt("quantity"),
                        resultSet.getDouble("price"),
                        resultSet.getString("type"),
                        resultSet.getString("size")
                );
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return null;
    }

    public void update(Snack snack, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(updateSql);
            statement.setString(1, snack.getName());
            statement.setString(2, snack.getDescription());
            statement.setInt(3, snack.getQuantity());
            statement.setDouble(4, snack.getPrice());
            statement.setString(5, snack.getType());
            statement.setString(6, snack.getSize());
            statement.setInt(7, id);
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

    public List<Snack> selectAll() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            List<Snack> snacks = new ArrayList<>();
            while (resultSet.next()) {
                snacks.add(new Snack(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("description"),
                        resultSet.getInt("quantity"),
                        resultSet.getDouble("price"),
                        resultSet.getString("type"),
                        resultSet.getString("size")
                ));
            }
            return snacks;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Map<Integer, Snack> selectAllIdModel() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            Map<Integer, Snack> snacks = new HashMap<>();
            while (resultSet.next()) {
                snacks.put(resultSet.getInt("id"), new Snack(
                        resultSet.getString("name"),
                        resultSet.getString("description"),
                        resultSet.getInt("quantity"),
                        resultSet.getDouble("price"),
                        resultSet.getString("type"),
                        resultSet.getString("size")
                ));
            }
            return snacks;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
