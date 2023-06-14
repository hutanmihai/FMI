package repositories;

import models.Movie;
import models.Showtime;
import models.Theater;

import java.sql.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class ShowtimeRepository extends BaseRepository implements GenericRepository<Showtime> {
    private final String insertSql = "INSERT INTO showtime (theaterId, movieId, showingdate, seats) VALUES (?, ?, ?, ?)";
    private final String updateSql = "UPDATE showtime SET theaterId = ?, movieId = ?, showingdate = ?, seats = ? WHERE id = ?";
    private final String selectSql = "SELECT * FROM showtime WHERE id = ?";
    private final String selectAllSql = "SELECT * FROM showtime";
    private final String deleteSql = "DELETE FROM showtime WHERE id = ?";

    public ShowtimeRepository() {
    }

    private Integer getTheaterId(Theater theater) {
        if (theater == null) {
            return null;
        }
        return theater.getId();
    }

    private Integer getMovieId(Movie movie) {
        if (movie == null) {
            return null;
        }
        return movie.getId();
    }

    public void insert(Showtime showtime) {
        try {
            PreparedStatement statement = db.prepareStatement(insertSql);
            statement.setInt(1, this.getTheaterId(showtime.getTheater()));
            statement.setInt(2, this.getMovieId(showtime.getMovie()));
            statement.setDate(3, Date.valueOf(showtime.getShowingDate()));
            statement.setArray(4, db.createArrayOf("int", showtime.getSeats().toArray()));
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public void update(Showtime showtime, int id) {
        try {
            PreparedStatement statement = db.prepareStatement(updateSql);
            statement.setInt(1, this.getTheaterId(showtime.getTheater()));
            statement.setInt(2, this.getMovieId(showtime.getMovie()));
            statement.setDate(3, Date.valueOf(showtime.getShowingDate()));
            statement.setArray(4, db.createArrayOf("int", showtime.getSeats().toArray()));
            statement.setInt(5, id);
            statement.executeUpdate();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Showtime select(int id) {
        try {
            PreparedStatement statement = db.prepareStatement(selectSql);
            statement.setInt(1, id);
            ResultSet resultSet = statement.executeQuery();
            Showtime showtime = new Showtime();
            while (resultSet.next()) {
                showtime.setId(resultSet.getInt("id"));
                showtime.setTheater(new TheaterRepository().select(resultSet.getInt("theaterId")));
                showtime.setMovie(new MovieRepository().select(resultSet.getInt("movieId")));
                showtime.setShowingDate(resultSet.getDate("showingdate").toLocalDate());
                Array seatsArray = resultSet.getArray("seats");
                Integer[] seats = (Integer[]) seatsArray.getArray();
                List<Integer> seatsList = new ArrayList<Integer>();
                for (Object seat : seats) {
                    seatsList.add((Integer) seat);
                }
                showtime.setSeats(seatsList);
            }
            return showtime;
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

    public List<Showtime> selectAll() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            List<Showtime> showtimes = new ArrayList<>();
            while (resultSet.next()) {
                Showtime showtime = new Showtime();
                showtime.setId(resultSet.getInt("id"));
                showtime.setTheater(new TheaterRepository().select(resultSet.getInt("theaterId")));
                showtime.setMovie(new MovieRepository().select(resultSet.getInt("movieId")));
                showtime.setShowingDate(resultSet.getDate("showingdate").toLocalDate());
                Array seatsArray = resultSet.getArray("seats");
                Integer[] seats = (Integer[]) seatsArray.getArray();
                List<Integer> seatsList = new ArrayList<Integer>();
                for (Object seat : seats) {
                    seatsList.add((Integer) seat);
                }
                showtime.setSeats(seatsList);
                showtimes.add(showtime);
            }
            return showtimes;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    public Map<Integer, Showtime> selectAllIdModel() {
        try {
            PreparedStatement statement = db.prepareStatement(selectAllSql);
            ResultSet resultSet = statement.executeQuery();
            Map<Integer, Showtime> showtimes = new HashMap<>();
            while (resultSet.next()) {
                Showtime showtime = new Showtime();
                showtime.setId(resultSet.getInt("id"));
                showtime.setTheater(new TheaterRepository().select(resultSet.getInt("theaterId")));
                showtime.setMovie(new MovieRepository().select(resultSet.getInt("movieId")));
                showtime.setShowingDate(resultSet.getDate("showingdate").toLocalDate());
                Array seatsArray = resultSet.getArray("seats");
                Integer[] seats = (Integer[]) seatsArray.getArray();
                List<Integer> seatsList = new ArrayList<Integer>();
                for (Object seat : seats) {
                    seatsList.add((Integer) seat);
                }
                showtime.setSeats(seatsList);
                showtimes.put(showtime.getId(), showtime);
            }
            return showtimes;
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
