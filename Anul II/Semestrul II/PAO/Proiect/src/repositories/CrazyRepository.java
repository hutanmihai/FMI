package repositories;

import database.DbConnection;

import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.*;
import java.util.stream.Collectors;

/**
 * UNUSED REPOSITORY, TRIED TO MAKE IT GENERIC BUT FAILED
 */
public class CrazyRepository<T> {

    protected Connection db;
    private final Class<T> type;
    private final Map<String, Method> getters;
    private final Map<String, Method> setters;
    private final List<Field> fields;
    private final String insertSql;
    private final String updateSql;
    private final String deleteSql;
    private final String selectSql;
    private final String selectAllSql;


    public CrazyRepository(Class<T> type) {
        try {
            this.db = DbConnection.getSession();
        } catch (SQLException e) {
            throw new RuntimeException(e);
        }

        this.type = type;
        String tableName = type.getSimpleName().toLowerCase();

        this.getters = new HashMap<>();
        this.setters = new HashMap<>();

        this.fields = new ArrayList<>();
        for (Class<?> sclass = type; sclass != null; sclass = sclass.getSuperclass()) {
            fields.addAll(Arrays.asList(sclass.getDeclaredFields()));
        }

        ArrayList<Method> methods = new ArrayList<>();
        methods.addAll(Arrays.asList(type.getMethods()));

        for (Field field : fields) {
            String fieldName = field.getName();
            String getterName = "get" + Character.toUpperCase(fieldName.charAt(0)) + fieldName.substring(1);
            String setterName = "set" + Character.toUpperCase(fieldName.charAt(0)) + fieldName.substring(1);

            Method getter = methods.stream().filter(method -> method.getName().equals(getterName)).findFirst().get();
            Method setter = methods.stream().filter(method -> method.getName().equals(setterName)).findFirst().get();
            this.getters.put(fieldName, getter);
            this.setters.put(fieldName, setter);
        }

        String columnList = getters.keySet().stream().filter(
                name -> !name.equals("id")).collect(Collectors.joining(", "));
        String placeholderList = getters.keySet().stream().filter(
                name -> !name.equals("id")).map(name -> "?").collect(Collectors.joining(", "));
        this.insertSql = "INSERT INTO " + tableName + " (" + columnList + ") VALUES (" + placeholderList + ")";
        this.updateSql = "UPDATE " + tableName + " SET " + columnList.replace(", ", "=?, ") + "=? WHERE id=?";
        this.deleteSql = "DELETE FROM " + tableName + " WHERE id=?";
        this.selectSql = "SELECT * FROM " + tableName + " WHERE id=?";
        this.selectAllSql = "SELECT * FROM " + tableName;
    }

    public void insert(T model) {
        try {
            PreparedStatement statement = db.prepareStatement(this.insertSql);
            int i = 1;
            for (Method getter : getters.values()) {
                if (getter.getName().equals("getId")) {
                    continue;
                }
                Object value = getter.invoke(model);
                statement.setObject(i++, value);
            }
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void update(T model, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(this.updateSql);
            int i = 1;
            for (Method getter : getters.values()) {
                if (getter.getName().equals("getId")) {
                    continue;
                }
                Object value = getter.invoke(model);
                statement.setObject(i++, value);
            }
            statement.setInt(i++, id);
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void delete(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(this.deleteSql);
            statement.setInt(1, id);
            statement.executeQuery();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public T select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(this.selectSql);
            statement.setInt(1, id);
            T result = this.type.getConstructor().newInstance();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                for (Field field : this.fields) {
                    String fieldName = field.getName();
                    Method setter = setters.get(fieldName);
                    setter.invoke(result, resultSet.getObject(fieldName));
                }
            }
            return result;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public List<T> selectAll() {
        try {
            PreparedStatement statement = db.prepareStatement(this.selectAllSql);
            List<T> result = new ArrayList<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                T model = this.type.getConstructor().newInstance();
                for (Field field : this.fields) {
                    String fieldName = field.getName();
                    Method setter = setters.get(fieldName);
                    setter.invoke(model, resultSet.getObject(fieldName));
                }
                result.add(model);
            }
            return result;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Map<Integer, T> selectAllIdModel() {
        try {
            PreparedStatement statement = db.prepareStatement(this.selectAllSql);
            Map<Integer, T> result = new HashMap<>();
            ResultSet resultSet = statement.executeQuery();
            while (resultSet.next()) {
                T model = this.type.getConstructor().newInstance();
                for (Field field : this.fields) {
                    String fieldName = field.getName();
                    Method setter = setters.get(fieldName);
                    setter.invoke(model, resultSet.getObject(fieldName));
                }
                int id = resultSet.getInt("id");
                result.put(id, model);
            }
            return result;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
