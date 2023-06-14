package repositories;

import models.Movie;

import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class MovieRepository extends BaseRepository implements GenericRepository<Movie> {
    private final String insertSql = "INSERT INTO movie (title, genre, year, duration) VALUES (?, ?, ?, ?)";
    private final String updateSql = "UPDATE movie SET title = ?, genre = ?, year = ?, duration = ? WHERE id = ?";
    private final String selectSql = "SELECT * FROM movie WHERE id = ?";
    private final String selectAllSql = "SELECT * FROM movie";
    private final String deleteSql = "DELETE FROM movie WHERE id = ?";

    public MovieRepository() {
    }

    public void insert(Movie movie) {
        try {
            PreparedStatement statement = db.prepareStatement(insertSql);
            statement.setString(1, movie.getTitle());
            statement.setString(2, movie.getGenre());
            statement.setInt(3, movie.getYear());
            statement.setInt(4, movie.getDuration());
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Movie select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(selectSql);
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            if (resultSet.next()) {
                return new Movie(
                        resultSet.getInt("id"),
                        resultSet.getString("title"),
                        resultSet.getString("genre"),
                        resultSet.getInt("year"),
                        resultSet.getInt("duration")
                );
            }
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
        return null;
    }

    public void update(Movie movie, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(updateSql);
            statement.setString(1, movie.getTitle());
            statement.setString(2, movie.getGenre());
            statement.setInt(3, movie.getYear());
            statement.setInt(4, movie.getDuration());
            statement.setInt(5, id);
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

    public List<Movie> selectAll() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            List<Movie> movies = new ArrayList<>();
            while (resultSet.next()) {
                movies.add(new Movie(
                        resultSet.getInt("id"),
                        resultSet.getString("title"),
                        resultSet.getString("genre"),
                        resultSet.getInt("year"),
                        resultSet.getInt("duration")
                ));
            }
            return movies;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Map<Integer, Movie> selectAllIdModel() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            Map<Integer, Movie> movies = new HashMap<>();
            while (resultSet.next()) {
                movies.put(resultSet.getInt("id"), new Movie(
                        resultSet.getString("title"),
                        resultSet.getString("genre"),
                        resultSet.getInt("year"),
                        resultSet.getInt("duration")
                ));
            }
            return movies;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
