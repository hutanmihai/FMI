--4

SELECT category, COUNT(*)
FROM rental r,
     title t
WHERE r.title_id = t.title_id
GROUP BY category
HAVING COUNT(*) = (SELECT MAX(COUNT(*))
                   FROM rental r,
                        title t
                   WHERE r.title_id = t.title_id
                   GROUP BY category);

-- 5 Gheorghe Robert-Mihai

SELECT title.title_id, COUNT(title_copy.copy_id) AS numar_copii
FROM title,
     title_copy
WHERE title.title_id = title_copy.title_id
  AND title_copy.status = 'AVAILABLE'

GROUP BY title.title_id

ORDER BY title.title_id;


--alta idee de solutie

SELECT title_id, COUNT(copy_id)
FROM rental
WHERE act_ret_date IS NOT NULL
GROUP BY title_id;
--putem avea copii care nu au fost vreodata rented, deci poate nu apar in rental
--putem avea aceeasi copie rented de mai multe ori?
--putem avea aceeasi copie rented si returned in trecut, dar in prezent rented?
