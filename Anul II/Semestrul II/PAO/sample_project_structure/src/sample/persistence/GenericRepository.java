package sample.persistence;

import java.util.List;
import java.util.Optional;

/**
 * @author cvoinea
 * <p>
 * This is a generic contract for repositories.
 * <p>
 * Repositories are contracts between the domain layer and the persistence layer.
 * All the CRUD operations (Create, read, update, and delete) can be implemented with the help of a repository interface.
 */
public interface GenericRepository<T> {

    T save(T entity);

    List<T> findAll();

    Optional<T> findById(String id);

    void update(T entity);

    void delete(T entity);
}
