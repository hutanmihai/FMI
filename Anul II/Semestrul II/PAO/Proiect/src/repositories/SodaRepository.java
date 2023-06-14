package repositories;

import models.Soda;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class SodaRepository extends BaseRepository implements GenericRepository<Soda> {
    private final String insertSql = "INSERT INTO soda (name, description, quantity, price, brand, flavor, volume) VALUES (?, ?, ?, ?, ?, ?, ?)";
    private final String updateSql = "UPDATE soda SET name = ?, description = ?, quantity = ?, price = ?, brand = ?, flavor = ?, volume = ? WHERE id = ?";
    private final String selectSql = "SELECT * FROM soda WHERE id = ?";
    private final String selectAllSql = "SELECT * FROM soda";
    private final String deleteSql = "DELETE FROM soda WHERE id = ?";

    public SodaRepository() {
    }

    public void insert(Soda soda) {
        try {
            PreparedStatement statement = db.prepareStatement(insertSql);
            statement.setString(1, soda.getName());
            statement.setString(2, soda.getDescription());
            statement.setInt(3, soda.getQuantity());
            statement.setDouble(4, soda.getPrice());
            statement.setString(5, soda.getBrand());
            statement.setString(6, soda.getFlavor());
            statement.setDouble(7, soda.getVolume());
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Soda select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(selectSql);
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Soda(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("description"),
                        resultSet.getInt("quantity"),
                        resultSet.getDouble("price"),
                        resultSet.getString("brand"),
                        resultSet.getString("flavor"),
                        resultSet.getDouble("volume")
                );
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return null;
    }

    public void update(Soda soda, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(updateSql);
            statement.setString(1, soda.getName());
            statement.setString(2, soda.getDescription());
            statement.setInt(3, soda.getQuantity());
            statement.setDouble(4, soda.getPrice());
            statement.setString(5, soda.getBrand());
            statement.setString(6, soda.getFlavor());
            statement.setDouble(7, soda.getVolume());
            statement.setInt(8, id);
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

    public List<Soda> selectAll() {
        List<Soda> sodas = new ArrayList<>();
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                sodas.add(new Soda(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("description"),
                        resultSet.getInt("quantity"),
                        resultSet.getDouble("price"),
                        resultSet.getString("brand"),
                        resultSet.getString("flavor"),
                        resultSet.getDouble("volume")
                ));
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return sodas;
    }

    public Map<Integer, Soda> selectAllIdModel() {
        Map<Integer, Soda> sodas = new HashMap<>();
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                sodas.put(resultSet.getInt("id"), new Soda(
                        resultSet.getString("name"),
                        resultSet.getString("description"),
                        resultSet.getInt("quantity"),
                        resultSet.getDouble("price"),
                        resultSet.getString("brand"),
                        resultSet.getString("flavor"),
                        resultSet.getDouble("volume")
                ));
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return sodas;
    }
}
