package repositories;

import java.util.List;
import java.util.Map;

public interface GenericRepository<T> {
    void insert(T model);

    T select(int id);

    void update(T model, int id);

    void delete(int id);

    List<T> selectAll();

    Map<Integer, T> selectAllIdModel();
}