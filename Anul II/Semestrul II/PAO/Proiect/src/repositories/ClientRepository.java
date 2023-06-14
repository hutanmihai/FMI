package repositories;

import models.Client;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ClientRepository extends BaseRepository implements GenericRepository<Client> {

    private final String insertSql = "INSERT INTO client (name, email, phone, membership, loyaltypoints) VALUES (?, ?, ?, ?, ?)";

    private final String updateSql = "UPDATE client SET name = ?, email = ?, phone = ?, membership = ?, loyaltypoints = ? WHERE id = ?";

    private final String selectSql = "SELECT * FROM client WHERE id = ?";

    private final String selectAllSql = "SELECT * FROM client";

    private final String deleteSql = "DELETE FROM client WHERE id = ?";

    public ClientRepository() {
    }

    public void insert(Client client) {
        try {
            PreparedStatement statement = db.prepareStatement(insertSql);
            statement.setString(1, client.getName());
            statement.setString(2, client.getEmail());
            statement.setString(3, client.getPhone());
            statement.setString(4, client.getMembership());
            statement.setInt(5, client.getLoyaltyPoints());
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Client select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(selectSql);
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Client(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("email"),
                        resultSet.getString("phone"),
                        resultSet.getString("membership"),
                        resultSet.getInt("loyaltypoints")
                );
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return null;
    }

    public void update(Client client, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(updateSql);
            statement.setString(1, client.getName());
            statement.setString(2, client.getEmail());
            statement.setString(3, client.getPhone());
            statement.setString(4, client.getMembership());
            statement.setInt(5, client.getLoyaltyPoints());
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

    public List<Client> selectAll() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            List<Client> clients = new ArrayList<>();
            if (resultSet.next()) {
                Client client = new Client(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("email"),
                        resultSet.getString("phone"),
                        resultSet.getString("membership"),
                        resultSet.getInt("loyaltypoints")
                );
                clients.add(client);
            }
            return clients;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Map<Integer, Client> selectAllIdModel() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            Map<Integer, Client> clients = new HashMap<>();
            if (resultSet.next()) {
                Client client = new Client(
                        resultSet.getInt("id"),
                        resultSet.getString("name"),
                        resultSet.getString("email"),
                        resultSet.getString("phone"),
                        resultSet.getString("membership"),
                        resultSet.getInt("loyaltypoints")
                );
                clients.put(client.getId(), client);
            }
            return clients;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
