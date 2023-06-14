--6
SELECT DISTINCT t.title                  AS titlu,
                tc.copy_id               AS nr_exemplar,
                tc.status                AS status_setat,
                CASE
                    WHEN act_ret_date IS NULL THEN 'RENTED'
                    WHEN exp_ret_date > SYSDATE THEN 'AVAILABLE'
                    ELSE 'AVAILABLE' END AS status_corect
FROM title t
         JOIN title_copy tc ON
    t.title_id = tc.title_id
         JOIN rental r ON
            t.title_id = r.title_id
        AND r.copy_id = tc.copy_id;
-------------------------------------------------------------------------------------------------------------------

--7
--a
SELECT COUNT(*) AS nr_exemplare_status_eronat
FROM (SELECT DISTINCT t.title
                    , tc.copy_id                                                        AS exemplar
                    , tc.status                                                         AS status_setat
                    , CASE WHEN act_ret_date IS NULL THEN 'RENTED' ELSE 'AVAILABLE' END AS status_corect
      FROM title t
               JOIN title_copy tc ON
          t.title_id = tc.title_id
               JOIN rental r ON
                  t.title_id = r.title_id
              AND r.copy_id = tc.copy_id)
WHERE status_setat != status_corect;

--b
CREATE TABLE title_copy_mhutan AS
SELECT *
FROM title_copy;

UPDATE title_copy_mhutan
SET status = 'RENTED'
WHERE copy_id IN (SELECT copy_id
                  FROM (SELECT DISTINCT t.title
                                      , tc.copy_id                                                        AS exemplar
                                      , tc.status                                                         AS status_setat
                                      , CASE WHEN act_ret_date IS NULL THEN 'RENTED' ELSE 'AVAILABLE' END AS status_corect
                        FROM title t
                                 JOIN title_copy tc ON
                            t.title_id = tc.title_id
                                 JOIN rental r ON
                                    t.title_id = r.title_id
                                AND r.copy_id = tc.copy_id)
                  WHERE status_setat != status_corect AND status_corect = 'RENTED');

UPDATE title_copy_mhutan
SET status = 'AVAILABLE'
WHERE copy_id IN (SELECT copy_id
                  FROM (SELECT DISTINCT t.title
                                      , tc.copy_id                                                        AS exemplar
                                      , tc.status                                                         AS status_setat
                                      , CASE WHEN act_ret_date IS NULL THEN 'RENTED' ELSE 'AVAILABLE' END AS status_corect
                        FROM title t
                                 JOIN title_copy tc ON
                            t.title_id = tc.title_id
                                 JOIN rental r ON
                                    t.title_id = r.title_id
                                AND r.copy_id = tc.copy_id)
                  WHERE status_setat != status_corect AND status_corect = 'AVAILABLE');
-------------------------------------------------------------------------------------------------------------------

--8
SELECT CASE
           WHEN COUNT(*) = 0
               THEN 'Da'
           ELSE 'Nu'
           END AS toate_imprumuturile_corecte
FROM (SELECT DISTINCT res.title_id, res.res_date, r.book_date
      FROM reservation res
               JOIN rental r ON (r.title_id = res.title_id AND r.member_id = res.member_id)
      WHERE res.res_date = r.book_date);
-------------------------------------------------------------------------------------------------------------------

--9
WITH tbl AS (SELECT mem.last_name, mem.first_name, tit.title, mem.member_id, tit.title_id
             FROM member mem,
                  title tit
                      JOIN rental ren ON (tit.title_id = ren.title_id)
             WHERE mem.member_id = ren.member_id)
SELECT DISTINCT CONCAT(CONCAT(tb.last_name, ' '), tb.first_name) AS membru,
                tb.title                                         AS titlu,
                (SELECT COUNT(*)
                 FROM rental
                 WHERE tb.member_id = member_id
                   AND tb.title_id = title_id)                   AS nr_imprumuturi
FROM tbl tb;
-------------------------------------------------------------------------------------------------------------------

--10
WITH tbl AS (SELECT mem.last_name, mem.first_name, tit.title, mem.member_id, tit.title_id, tc.copy_id
             FROM member mem,
                  title tit
                      JOIN rental ren ON (tit.title_id = ren.title_id)
                      JOIN title_copy tc ON (tc.title_id = tit.title_id)
             WHERE mem.member_id = ren.member_id
               AND ren.copy_id = tc.copy_id)
SELECT DISTINCT CONCAT(CONCAT(tb.last_name, ' '), tb.first_name) AS membru,
                tb.title                                         AS titlu,
                tb.copy_id                                       AS copie_id,
                (SELECT COUNT(*)
                 FROM rental
                 WHERE tb.member_id = member_id
                   AND tb.title_id = title_id
                   AND tb.copy_id = copy_id)                     AS nr_imprumuturi
FROM tbl tb;
-------------------------------------------------------------------------------------------------------------------

--11
WITH numar_exemplare AS (SELECT title_id, copy_id, COUNT(*) AS numar_titlu
                         FROM rental ex
                         GROUP BY title_id, copy_id
                         HAVING COUNT(*) = (SELECT MAX(numar_titlu)
                                            FROM (SELECT title_id, copy_id, COUNT(*) AS numar_titlu
                                                  FROM rental
                                                  GROUP BY title_id, copy_id) maxim
                                            WHERE ex.title_id = maxim.title_id
                                            GROUP BY ex.title_id))
SELECT UNIQUE tc.title_id AS id, tc.copy_id AS copie_id, nr.numar_titlu AS numar_titlu, tc.status AS status
FROM title_copy_mhutan tc,
     numar_exemplare nr
WHERE tc.title_id = nr.title_id
  AND nr.copy_id = tc.copy_id
ORDER BY 1;
-------------------------------------------------------------------------------------------------------------------

--12
--a
SELECT TO_CHAR(act_ret_date, 'dd') zi, COUNT(act_ret_date) imprumuturi
FROM rental
WHERE TO_CHAR(act_ret_date, 'dd-mm-yyyy') = '01-' || TO_CHAR(SYSDATE, 'mm-yyyy')
   OR TO_CHAR(act_ret_date, 'dd-mm-yyyy') = '02-' || TO_CHAR(SYSDATE, 'mm-yyyy')
GROUP BY act_ret_date;

--b
SELECT TO_CHAR(act_ret_date, 'dd') zi, COUNT(act_ret_date) imprumuturi
FROM rental
WHERE TO_CHAR(act_ret_date, 'mm-yyyy') = TO_CHAR(SYSDATE, 'mm-yyyy')
GROUP BY act_ret_date;


--c
SELECT TO_CHAR(zi_luna, 'dd')         zi,
       (SELECT COUNT(act_ret_date)
        FROM rental
        WHERE act_ret_date = zi_luna) imprumuturi
FROM (SELECT TO_DATE('01-' || TO_CHAR(SYSDATE, 'mon-yyyy')) + level - 1 zi_luna
      FROM dual
      CONNECT BY level <=
                 TO_DATE('01-' || TO_CHAR(SYSDATE + 31, 'mon-yyyy')) - TO_DATE('01-' || TO_CHAR(SYSDATE, 'mon-yyyy')))
GROUP BY zi_luna
ORDER BY zi;
-------------------------------------------------------------------------------------------------------------------